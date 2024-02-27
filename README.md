## NBKR Forex Rates Parser

This project demonstrates the use of FastAPI with MongoDB to fetch and store foreign exchange rates from 
the National Bank of the Kyrgyz Republic (NBKR) for **USD**, **EUR**, **RUB** and **KZT** currencies. It showcases how to structure a FastAPI project, perform 
asynchronous HTTP requests, parse HTML content, and interact with MongoDB.


## Features

- Fetch foreign exchange rates for specified currencies and date ranges from NBKR.
- Store rates in MongoDB with unique constraints to avoid duplicates.
- Retrieve historical rate data through a RESTful API endpoint.

## Requirements

- Python 3.10+
- MongoDB instance (local or cloud)
- Docker and Docker Compose (optional for containerization)

## Setup

1. **Clone the Repository**

```bash
git clone https://github.com/nurai5/nbkr_forex_rates_parser.git
cd nbkr_forex_rates_parser
```

2. **Start Docker-Compose File**

**For Local MongoDB Instance In Container:**
```bash
docker-compose -f docker-compose.local.yml up --build
```

**For Remote MongoDB Instance:**
```bash
docker-compose -f docker-compose.prod.yml up --build
```

## Fetching Historical Exchange Rates

To retrieve historical exchange rate data between two currencies for a specified period, use the following request:
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/historical-rate/?base_currency=KGS&target_currency=USD&start_date=2022-12-10&end_date=2022-12-12' \
  -H 'accept: application/json'
```

**Response**

Upon successful request, you will receive a JSON response with the historical exchange rates for the specified period. Here's an example of what the response might look like:

```json
[
  {
    "id": "65dd45d466a806ad5a6013d6",
    "base_currency": "KGS",
    "target_currency": "USD",
    "rate": 84.95,
    "date": "2022-12-10T00:00:00"
  },
  {
    "id": "65dd45d466a806ad5a6013d5",
    "base_currency": "KGS",
    "target_currency": "USD",
    "rate": 84.95,
    "date": "2022-12-11T00:00:00"
  },
  {
    "id": "65dd45d466a806ad5a6013d4",
    "base_currency": "KGS",
    "target_currency": "USD",
    "rate": 84.95,
    "date": "2022-12-12T00:00:00"
  }
]
```
