# Product API

Run these commands from this directory:

```powershell
python -m pip install -r requirements.txt
python -m uvicorn app:app --reload
```

- `POST /products`: accepts `{"name": "Laptop", "price": 1500}` and returns
  `{"id": 1, "name": "Laptop", "price": 1500}` with status 201.
- `GET /products`: returns all products as a JSON array with a 10% discount,
  without rounding. The example above is returned with price 1350.

The controller handles HTTP validation, and the repository stores products in memory.
The service checks that the product price is greater than 1000
before storage. Prices of 1000 or less are rejected with status 422.
It applies a 10% discount on retrieval without changing stored prices, so repeated
retrieval does not compound the discount. No name normalization is applied.
Data is lost on restart and is not shared between multiple server workers.

Interactive API documentation: http://127.0.0.1:8000/docs

Run the focused tests (httpx is included for FastAPI's test client):

```powershell
python -m unittest test_product_api -v
```
