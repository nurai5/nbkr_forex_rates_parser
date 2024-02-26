## NBKR Forex Rates Parser

This project demonstrates the use of FastAPI with MongoDB to fetch and store foreign exchange rates from 
the National Bank of the Kyrgyz Republic (NBKR). It showcases how to structure a FastAPI project, perform 
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

```bash
docker-compose up --build
```
