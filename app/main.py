from fastapi import FastAPI, status
from psycopg.types.json import Json
from psycopg_pool import ConnectionPool

from app.schema.product import ProductSchema

DATABASE_URL = "postgresql://postgres:Akina1996!@localhost:5432/my_database"
app = FastAPI(title="demo_7")
pool = ConnectionPool(DATABASE_URL)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/products", status_code=status.HTTP_201_CREATED, response_model=ProductSchema)
def post_product(product: ProductSchema) -> ProductSchema:

    with pool.connection() as conn:
        with conn.transaction():
            conn.execute(
    "INSERT INTO products_raw (payload) VALUES (%s)",
    (Json(product.model_dump()),),
)


    return product

@app.post("/products/bulk", status_code=status.HTTP_201_CREATED)
def post_products_bulk(products: list[ProductSchema]):
    rows = [(Json(p.model_dump()),) for p in products]

    with pool.connection() as conn:
        with conn.transaction():
            with conn.cursor() as cur:
                cur.executemany(
                    "INSERT INTO products_raw (payload) VALUES (%s)",
                    rows,
                )

    return {"inserted": len(products)}
