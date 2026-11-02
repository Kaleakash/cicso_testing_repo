from fastapi.testclient import TestClient
from main import app

c=TestClient(app)
checks=[]
def check(label, resp, status):
    assert resp.status_code==status, f"{label}: expected {status}, got {resp.status_code} {resp.text}"
    checks.append(label)

check("root", c.get("/"), 200)
check("collection", c.get("/devices"), 200)
check("existing", c.get("/devices/1"), 200)
missing=c.get("/devices/999");check("missing",missing,404)
assert missing.json()["error"]["code"]=="DEVICE_NOT_FOUND"
created=c.post("/devices", json={"name":"Firewall-01","device_type":"firewall","status":"online"});check("create",created,201)
new_id=created.json()["id"]
check("invalid input",c.post("/devices", json={"name":"","device_type":"router","status":"online"}),422)
check("replace",c.put(f"/devices/{new_id}", json={"name":"Firewall-02","device_type":"firewall","status":"offline"}),200)
patched=c.patch(f"/devices/{new_id}",json={"status":"online"});check("patch",patched,200)
assert patched.json()["name"]=="Firewall-02"
check("delete",c.delete(f"/devices/{new_id}"),204)
check("deleted missing",c.get(f"/devices/{new_id}"),404)
check("openapi schema",c.get("/openapi.json"),200)
print(f"PASS: {len(checks)} checks; 0 failed")
