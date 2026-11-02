"""Run: python validate_m2s2_demo.py (with dependencies installed)."""
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
checks = []

def check(label, response, expected):
    ok = response.status_code == expected
    print(f"[{'PASS' if ok else 'FAIL'}] {label}: HTTP {response.status_code} (expected {expected})")
    checks.append(ok)
    return response

check("Root", client.get("/"), 200)
check("GET collection", client.get("/products"), 200)
check("GET by id", client.get("/products/1"), 200)
check("GET missing", client.get("/products/999"), 404)
created = check("POST", client.post("/products", json={"name":"Headset","price":75.0,"in_stock":True}), 201)
pid = created.json().get("id") if created.status_code == 201 else 999
check("POST invalid price", client.post("/products", json={"name":"Invalid Product","price":"not-a-number","in_stock":True}), 422)
check("PUT", client.put(f"/products/{pid}", json={"name":"Wireless Headset","price":89.0,"in_stock":True}), 200)
patched = check("PATCH", client.patch(f"/products/{pid}", json={"price":79.0}), 200)
checks.append(patched.status_code == 200 and patched.json().get("name") == "Wireless Headset" and patched.json().get("price") == 79.0)
check("DELETE", client.delete(f"/products/{pid}"), 204)
check("GET deleted", client.get(f"/products/{pid}"), 404)
print(f"\nPassed: {sum(checks)} | Failed: {len(checks) - sum(checks)}")
if not all(checks):
    raise SystemExit(1)
