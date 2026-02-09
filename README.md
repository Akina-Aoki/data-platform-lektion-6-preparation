# Ingestion Preparation

Small demo project for ingesting product data via FastAPI and storing raw JSON in PostgreSQL.
Used later as a base for ETL and Pandas exercises.

## Clone
```bash
git clone <REPO_URL>
cd <REPO_NAME>
```

## Environment (uv + .venv)
This project uses uv and a local virtual environment.

```bash
uv sync
```

Run the API:
```bash
uv run uvicorn app.main:app --reload
```

## Database configuration
Open `app/main.py` and update the connection string:

```python
DATABASE_URL = "postgresql://postgres:DB_PASSWORD@localhost:5432/DB_NAME"
```

Example:
```python
DATABASE_URL = "postgresql://postgres:secret@localhost:5432/my_database"
```

## Database setup (pgAdmin4)
Create a new database, then run:

```sql
CREATE TABLE IF NOT EXISTS products_raw (
    id BIGSERIAL PRIMARY KEY,
    ingested_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    payload JSONB NOT NULL
);
```

## API usage
POST /products
```json
{
  "name": "USB-C Cable",
  "price": 149.0,
  "quantity": 120,
  "currency": "SEK"
}
```

POST /products/bulk
```json
[
  { "name": "USB-C Cable", "price": 149.0, "quantity": 120, "currency": "SEK" },
  { "name": "Wireless Mouse", "price": 299.0, "quantity": 75, "currency": "SEK" },
  { "name": "Mechanical Keyboard", "price": 1299.0, "quantity": 25, "currency": "SEK" },
  { "name": "Laptop Stand", "price": 499.0, "quantity": 40, "currency": "SEK" },
  { "name": "HDMI Adapter", "price": 99.0, "quantity": 200, "currency": "SEK" },
  { "name": "Webcam", "price": 899.0, "quantity": 30, "currency": "SEK" },
  { "name": "Desk Lamp", "price": 349.0, "quantity": 60, "currency": "SEK" },
  { "name": "External SSD 1TB", "price": 1499.0, "quantity": 15, "currency": "SEK" },
  { "name": "Office Chair", "price": 2499.0, "quantity": 10, "currency": "SEK" },
  { "name": "USB Hub", "price": 399.0, "quantity": 50, "currency": "SEK" }
]
```


## Notes
Raw data is stored unchanged in products_raw.payload (JSONB).
This project is intentionally simple and used as a starting point for ETL.

