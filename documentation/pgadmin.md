# Workflow in PgAdmin4

## 1. Open PgAdmin4 
- Open `my_database`, `Schema`, `Tables`
- `Query Tool` to `CREATE TABLE`
    -  No need to do if `products_raw` table already exists
- Navigate to the Table, RIGHT CLICK, EDIT/VIEW, ALL ROWS
![3](assets/3.png)

## 2.A Postman
- Open Postman **APP** POST -> `localhost:8000/products/bulk` -> BODY -> PASTE the Insert from the README -> `SEND`
![4](assets/4.png)

## 2.B Thundercloud
- Same steps as Postman. Open the extension. 
- POST -> `localhost:8000/products/bulk` -> BODY -> PASTE the Insert from the README -> `SEND`
![5](assets/5.png)

- Expected Output should be: `INFO:     127.0.0.1:50776 - "POST /products/bulk HTTP/1.1" 201 Created`