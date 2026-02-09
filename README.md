# Ingestion Preparation

- **PgAdmin 4 Database name:** `my_database`
Small demo project for ingesting product data via FastAPI and storing raw JSON in PostgreSQL.
Used later as a base for ETL and Pandas exercises.

# Restarting Vscode Operaitons
## Activate venv
- `source .venv/Scripts/activate`
- validate: `where python`

Run the API:
```bash
uv run uvicorn app.main:app --reload
```

- Expected Output:
```
INFO:     Started server process [3716]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

## Open the localhost
- `http://127.0.0.1:8000/docs`
- **Check the terminal for any errors**
- Open: POST /products
- Press Try it out.

------------------------------------------------

# First time creation

## Fork and Clone
```bash
git clone <REPO_URL>
cd <REPO_NAME>
```

## Environment (uv + .venv)
- This project uses uv and a local virtual environment.

```bash
uv sync
```

------------------------------------------------

## Activate venv
- `source .venv/Scripts/activate`
- validate: `where python`

Run the API:
```bash
uv run uvicorn app.main:app --reload
```
- If this fails, follow the **Activate venv to restart Vscode venv**

## Database configuration
Open `app/main.py` and update the connection string:

```python
DATABASE_URL = "postgresql://postgres:DB_PASSWORD@localhost:5432/DB_NAME"
```

#### MY PSQL PASSWORD: `Akina1996!`

Example:
```python
DATABASE_URL = "postgresql://postgres:secret@localhost:5432/my_database"
```

-----------------------------------------------
# If first time creating the repo
## Activate venv
- `source .venv/Scripts/activate`
- validate: `where python`

## Install dependencies
- `pip install fastapi uvicorn psycopg[binary] psycopg_pool`

- Expected output: `Successfully installed fastapi-0.128.5 psycopg-3.3.2 psycopg-binary-3.3.2 psycopg_pool-3.3.0`

- Install the requirements `pip install -r requirements.txt`
- * Does not exists here

## Sanity check for 
```
pip list | findstr fastapi
pip list | findstr psycopg
```

## Restart VS Code kernel / interpreter
- Very important.
- Ctrl + Shift + P → Python: Select Interpreter → choose the one inside `.\.venv.\Scripts\python.exe`
- Then reload the window.
- Yellow warnings usually disappear immediately.

## Run uvicorn
Run the API:
```bash
uv run uvicorn app.main:app --reload
```

------------------------------------------------------------------------------------------------------------------------
#  PgAdmin4
- Open pgAdmin4
![Create database and table pgadmin setup](assets/1.png)

## Database setup (pgAdmin4)
Create a new database, then run:

```sql
CREATE TABLE IF NOT EXISTS products_raw (
    id BIGSERIAL PRIMARY KEY,
    ingested_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    payload JSONB NOT NULL
);
```

## Open the localhost
- `http://127.0.0.1:8000/docs`
- Open: POST /products
- Press Try it out.


## API usage
- Use:
- POST /products
```json
{
  "name": "USB-C Cable",
  "price": 149.0,
  "quantity": 120,
  "currency": "SEK"
}
```
- Expected KPI: `201 Created`

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
- Expected KPI: `201 Created`

## Now confirm the data actually landed
- Go to pgAdmin → open Query Tool → run:

```
SELECT id, ingested_at, payload
FROM products_raw
ORDER BY id DESC;
```
- Expected Output: 
![Confirm by querying a sample](assets/2.png)

## Notes
Raw data is stored unchanged in products_raw.payload (JSONB).
This project is intentionally simple and used as a starting point for ETL.

## References
- (Parquet File Format)[https://motherduck.com/learn-more/why-choose-parquet-table-file-format/]'

- (Columnar Storage Guide)[https://motherduck.com/learn-more/columnar-storage-guide/]