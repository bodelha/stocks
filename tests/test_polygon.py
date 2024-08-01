from src.polygon import *


def test_assemble_url():

    response = assemble(
        base_url="https://api.polygon.io/v1/open-close",
        ticker="AAPL",
        date="2023-01-09",
        adjusted=True,
        api_key="5G75jgQPqz7tV_UjWhC2Fu5iQyTVW2hS",
    )

    assert (
        response
        == "https://api.polygon.io/v1/open-close/AAPL/2023-01-09?adjusted=true&apiKey=5G75jgQPqz7tV_UjWhC2Fu5iQyTVW2hS"
    )


def test_collect():
    response = collect(
        "https://api.polygon.io/v1/open-close/AAPL/2023-01-09?adjusted=true&apiKey=5G75jgQPqz7tV_UjWhC2Fu5iQyTVW2hS"
    )
    assert response.status_code == 200
