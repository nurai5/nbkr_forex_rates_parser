from pydantic import BaseModel
from enum import Enum
from datetime import date


class CurrencyEnum(Enum):
    KGS = "KGS"
    USD = "USD"
    EUR = "EUR"
    RUB = "RUB"
    KZT = "KZT"


class ForexRate(BaseModel):
    base_currency: CurrencyEnum
    target_currency: CurrencyEnum
    rate: float
    date: date
