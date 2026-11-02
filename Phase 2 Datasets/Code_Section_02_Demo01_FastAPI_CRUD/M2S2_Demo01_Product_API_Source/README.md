# Cisco — M2S2 Demo 01: FastAPI CRUD Product API

This is **Demo-only** source. It matches the trainer's 16-page demo guide: `/`, GET collection/by ID, POST, PUT, PATCH, DELETE, response models, HTTPException handling, Swagger UI, Postman, and automated validation.

## 1. Folder structure

```text
product-api/
  main.py
  requirements.txt
  validate_m2s2_demo.py
```

## 2. In the Simplilearn Ubuntu sandbox

1. Extract this ZIP and open the `product-api` directory in VS Code.
2. Open a terminal **inside that directory** (VS Code → Terminal → New Terminal).
3. Create and activate a virtual environment (if one does not already exist):

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

4. Run the API:

```bash
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

5. Open `http://127.0.0.1:8000/` (expected: `{"message":"API is running"}`), then `http://127.0.0.1:8000/docs`.
6. In Swagger UI, expand an operation → **Try it out** → enter values where needed → **Execute**. Start with GET `/products` and GET `/products/1`.
7. For POST `/products` enter:

```json
{"name":"Headset","price":75.0,"in_stock":true}
```

8. Invalid POST example (expected **422**, not 201):

```json
{"name":"Invalid Product","price":"not-a-number","in_stock":true}
```

9. Note the `id` returned by POST (initially **3** in a fresh server process). Use that ID for PUT, PATCH, then DELETE.
10. For PUT use `{"name":"Wireless Headset","price":89.0,"in_stock":true}`. For PATCH use `{"price":79.0}`. DELETE returns **204**, then GET that ID returns **404**.
11. In a **separate terminal** while Uvicorn runs, run `python validate_m2s2_demo.py`. This automated test uses an in-process TestClient; it does **not** send network traffic to the running Uvicorn process.

## 3. Postman

Select method **POST**, URL `http://127.0.0.1:8000/products`, Body → raw → JSON, and paste:

```json
{"name":"USB Hub","price":45.0,"in_stock":true}
```

Click Send and confirm **201 Created**. Switch to GET `http://127.0.0.1:8000/products` and confirm **200** and a list that includes the new product. Postman must reach the server from the same network environment. `127.0.0.1` refers to whichever machine Postman is running on; if the sandbox is remote, use its supported port forwarding/access mechanism.

## 4. Important trainer notes

- This is an **in-memory** API; products reset when the server process restarts. There is no database.
- The starting product data are illustrative and consistent with the screenshot's sample behavior; exact screenshot values may differ.
- The document uses `cd /home/ubuntu/phase2-lab` and a nested `module02-rest-services/fastapi/product-api` path. Those commands work **only if** the folder exists there. Run commands in your actual extracted `product-api` folder instead.
- The document shows `python validate_m2s2_demo.py` but the validation script was missing from the shared DOCX. It is supplied here.
- The sample HTTP error body is `{"error":{"message":"Product not found","status":404}}`. FastAPI's built-in 422 validation errors retain the standard `detail` structure.
- The docs list a straightforward root endpoint + 6 CRUD operations; Swagger UI will also display schemas for models.
