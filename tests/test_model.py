import pytest
from pydantic import ValidationError
from datetime import date
from src.model import (
    Stock,
    StockValues,
    PerformanceData,
    Competitor,
    CompetitorMarketCap,
)


def test_create_competitor_market_cap():
    market_cap_data = {"currency": "USD", "value": 5000000.0}
    competitor_market_cap = CompetitorMarketCap(**market_cap_data)
    assert competitor_market_cap.currency == "USD"
    assert competitor_market_cap.value == 5000000.0


def test_create_competitor():
    competitor_data = {
        "name": "Competitor A",
        "market_cap": [{"currency": "USD", "value": 5000000.0}],
    }
    competitor = Competitor(**competitor_data)
    assert competitor.name == "Competitor A"
    assert len(competitor.market_cap) == 1
    assert competitor.market_cap[0].currency == "USD"


def test_create_stock_values():
    stock_values_data = {"open": 100.0, "high": 110.0, "low": 90.0, "close": 105.0}
    stock_values = StockValues(**stock_values_data)
    assert stock_values.open == 100.0
    assert stock_values.high == 110.0
    assert stock_values.low == 90.0
    assert stock_values.close == 105.0


def test_create_performance_data():
    performance_data_data = {
        "five_days": 0.05,
        "one_month": 0.10,
        "three_months": 0.15,
        "year_to_date": 0.20,
        "one_year": 0.25,
    }
    performance_data = PerformanceData(**performance_data_data)
    assert performance_data.five_days == 0.05
    assert performance_data.one_month == 0.10


def test_create_stock():
    stock_data = {
        "status": "active",
        "purchased_amount": 100,
        "purchased_status": "purchased",
        "request_data": date(2023, 1, 1),
        "company_code": "COMP",
        "company_name": "Company Inc.",
        "stock_values": {"open": 100.0, "high": 110.0, "low": 90.0, "close": 105.0},
        "performance_data": {
            "five_days": 0.05,
            "one_month": 0.10,
            "three_months": 0.15,
            "year_to_date": 0.20,
            "one_year": 0.25,
        },
        "competitors": [
            {
                "name": "Competitor A",
                "market_cap": [{"currency": "USD", "value": 5000000.0}],
            }
        ],
    }
    stock = Stock(**stock_data)
    assert stock.status == "active"
    assert stock.purchased_amount == 100
    assert stock.company_code == "COMP"
    assert stock.company_name == "Company Inc."
    assert stock.stock_values.open == 100.0
    assert stock.performance_data.five_days == 0.05
    assert stock.competitors[0].name == "Competitor A"


def test_create_stock_invalid_data():
    stock_data = {
        "status": "active",
        "purchased_amount": "invalid",
        "purchased_status": "purchased",
        "request_data": date(2023, 1, 1),
        "company_code": "COMP",
        "company_name": "Company Inc.",
        "stock_values": {"open": 100.0, "high": 110.0, "low": 90.0, "close": 105.0},
        "performance_data": {
            "five_days": 0.05,
            "one_month": 0.10,
            "three_months": 0.15,
            "year_to_date": 0.20,
            "one_year": 0.25,
        },
        "competitors": [
            {
                "name": "Competitor A",
                "market_cap": [{"currency": "USD", "value": 5000000.0}],
            }
        ],
    }
    with pytest.raises(ValidationError):
        Stock(**stock_data)
