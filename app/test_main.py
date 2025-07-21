import datetime
from unittest.mock import patch, MagicMock
from app.main import outdated_products


@patch("app.main.get_today", return_value=datetime.date(2022, 2, 6))
def test_outdated_products(mock_get_today: MagicMock) -> None:
    products = [
        {"name": "salmon", "expiration_date":
            datetime.date(2026, 2, 10), "price": 600},
        {"name": "chicken", "expiration_date":
            datetime.date(2022, 2, 5), "price": 120},
        {"name": "duck", "expiration_date":
            datetime.date(2022, 2, 1), "price": 160}
    ]

    assert outdated_products(products) == ["chicken", "duck"]
