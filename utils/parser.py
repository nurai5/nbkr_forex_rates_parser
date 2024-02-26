import httpx
from fastapi import HTTPException
from datetime import date, datetime
from bs4 import BeautifulSoup
import re


async def get_NBKR_forex_rates(
        base_currency: str,
        target_currency: str,
        start_date: date,
        end_date: date
) -> list:
    """
    Get NBKR forex rates from start date to end date
    :param base_currency:
    :param target_currency:
    :param start_date:
    :param end_date:
    :return list:
    """
    currency_ids = {
        "USD": 15,
        "EUR": 20,
        "RUB": 44,
        "KZT": 40,
    }

    url = f'https://www.nbkr.kg/index1.jsp?item=1562&lang=RUS&valuta_id={currency_ids[target_currency]}&beg_day={start_date.day}&beg_month={start_date.month}&beg_year={start_date.year}&end_day={end_date.day}&end_month={end_date.month}&end_year={end_date.year}'

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error fetching currency rates")

        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        scripts = soup.find_all('script')
        chart_data_script = None

        for script in scripts:
            if 'var lineChartData =' in script.text:
                chart_data_script = script.text
                break

        if not chart_data_script:
            raise HTTPException(status_code=response.status_code, detail="Chart data not found.")

        labels_regex = r"labels\s*:\s*\[([^\]]+)\]"
        data_regex = r"data\s*:\s*\[([^\]]+)\]"

        labels_match = re.search(labels_regex, chart_data_script)
        data_match = re.search(data_regex, chart_data_script)

        if labels_match and data_match:
            labels = [datetime.strptime(label.strip().strip('"').strip("'"), "%d.%m.%Y") for label in
                      labels_match.group(1).split(",")]
            data = [float(value.strip()) for value in data_match.group(1).split(",")]

            currency_rates = [(label, rate) for label, rate in zip(labels, data)]

    return currency_rates
