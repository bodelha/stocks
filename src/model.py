from pydantic import BaseModel
from typing import List
from datetime import date


class CompetitorMarketCap(BaseModel):
    currency: str
    value: float


class Competitor(BaseModel):
    name: str
    market_cap: List[CompetitorMarketCap]


class StockValues(BaseModel):
    open: float
    high: float
    low: float
    close: float


class PerformanceData(BaseModel):
    five_days: float
    one_month: float
    three_months: float
    year_to_date: float
    one_year: float


class Stock(BaseModel):
    status: str
    purchased_amount: int
    purchased_status: str
    request_data: date
    company_code: str
    company_name: str
    stock_values: StockValues
    performance_data: PerformanceData
    competitors: List[Competitor]
