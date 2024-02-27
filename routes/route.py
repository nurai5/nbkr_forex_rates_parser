from fastapi import APIRouter, Query, HTTPException
from models.models import CurrencyEnum
from config.database import collection_name
from utils.parser import get_NBKR_forex_rates
from schemas.schema import list_forex_serial
from datetime import date, datetime, timedelta
from typing import List

router = APIRouter()


@router.get('/historical-rate/')
async def get_currency(
        base_currency: CurrencyEnum,
        target_currency: CurrencyEnum,
        start_date: date = Query(..., description="Start date in YYYY-MM-DD format"),
        end_date: date = Query(..., description="End date in YYYY-MM-DD format")
) -> List[dict]:

    start_datetime = datetime.combine(start_date, datetime.min.time())
    end_datetime = datetime.combine(end_date, datetime.max.time())

    total_days = (end_date - start_date).days
    expected_dates = {start_date + timedelta(days=x) for x in range(total_days + 1)}

    existing_data = []
    existing_dates = set()
    cursor = collection_name.find({
        "base_currency": base_currency.value,
        "target_currency": target_currency.value,
        "date": {"$gte": start_datetime, "$lte": end_datetime}
    })
    for doc in cursor:
        existing_data.append(doc)
        existing_dates.add(doc["date"].date())

    missing_dates = expected_dates - existing_dates

    documents = []
    for date in missing_dates:
        max_attempts = 3
        attempts = 0
        while attempts < max_attempts:
            try:
                currency_rates = await get_NBKR_forex_rates(base_currency.value, target_currency.value, date, date)
                document = {
                    "base_currency": base_currency.value,
                    "target_currency": target_currency.value,
                    "date": currency_rates[0][0],
                    "rate": currency_rates[0][1]
                }
                documents.append(document)
                existing_data.append(document)
                break
            except Exception as e:
                attempts += 1
                if attempts == max_attempts:
                    raise HTTPException(status_code=500, detail=f"Error retrieving currency rates: {e}")

    if documents:
        collection_name.insert_many(documents)

    result = list_forex_serial(existing_data)

    return result
