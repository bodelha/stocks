# Stocks REST API #


The objective is to build a web API application that retrieves stock data from an external financial API (Polygon.io) and performs minor data scraping from the MarketWatch financial website.

The application will expose two endpoints:
    * [GET] /stock/{stock_symbol}: returns the stock data for the given symbol.
    * [POST] /stock/{stock_symbol}: update the stock entity with the purchased amount based on received argument: “amount”

FastAPI is used as the framework due to its compatibility with Pydantic for data validation and its ease of assembling documentation in the OpenAPI format.


