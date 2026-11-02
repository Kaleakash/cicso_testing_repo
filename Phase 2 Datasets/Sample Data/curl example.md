
npx -y json-server@0.17.4 --watch devices.json --routes routes.json --port 3000

API V1 – cURL commands


Meaning of cURL options
Option	    Full meaning	Purpose
-i	        Include	        Displays HTTP response headers along with the response body.
-X	        Request	        Specifies the HTTP method (GET, POST, PUT, PATCH, DELETE).
-H	        Header	        Adds HTTP request headers.
-d	        Data	        Sends data (usually JSON) in the request body.

1. GET – Retrieve all devices
curl -i http://localhost:3000/api/v1/devices


2. GET – Retrieve device by ID
curl -i http://localhost:3000/api/v1/devices/DEV-101


3. GET – Filter offline devices
curl -i "http://localhost:3000/api/v1/devices?status=offline"


4. POST – Register new device
curl -i -X POST http://localhost:3000/api/v1/devices `
-H "Content-Type: application/json" `
-H "Accept: application/json" `
-d '{ "id": "DEV-116", "hostname": "blr-router-03", "ip_address": "10.10.3.10", "device_type": "router", "status": "online", "location": "Bengaluru" }'


5. PUT – Replace device details
curl -i -X PUT http://localhost:3000/api/v1/devices/DEV-101 `
-H "Content-Type: application/json" `
-d '{ "id": "DEV-101", "hostname": "blr-router-updated", "ip_address": "10.10.1.15", "device_type": "router", "status": "online", "location": "Bengaluru" }'


6. PATCH – Update only status
curl -i -X PATCH http://localhost:3000/api/v1/devices/DEV-101 `
-H "Content-Type: application/json" `
-d '{ "status": "offline" }'


7. DELETE – Remove device
curl -i -X DELETE http://localhost:3000/api/v1/devices/DEV-116


2. API V2 – cURL commands

1. GET – Retrieve all devices
curl -i http://localhost:3000/api/v2/devices


2. GET – Retrieve device by ID
curl -i http://localhost:3000/api/v2/devices/DEV-101


3. GET – Filter offline devices
curl -i "http://localhost:3000/api/v2/devices?device_state=offline"


4. POST – Register new device
curl -i -X POST http://localhost:3000/api/v2/devices `
-H "Content-Type: application/json" `
-H "Accept: application/json" `
-d '{ "id": "DEV-116", "hostname": "blr-router-03", "ip_address": "10.10.3.10", "device_type": "router", "device_state": "online", "location": { "city": "Bengaluru", "region": "Karnataka", "country": "India" }, "latency_ms": 15, "managed": true, "firmware_version": "18.0", "interfaces": [{ "name": "Gig0/0", "status": "up" }] }'


5. PUT – Replace device details
curl -i -X PUT http://localhost:3000/api/v2/devices/DEV-101 `
-H "Content-Type: application/json" `
-d '{ "id": "DEV-101", "hostname": "blr-router-updated", "ip_address": "10.10.1.15", "device_type": "router", "device_state": "online", "location": { "city": "Bengaluru", "region": "Karnataka", "country": "India" }, "latency_ms": 12, "managed": true, "firmware_version": "18.0", "interfaces": [{ "name": "Gig0/0", "status": "up" }] }'


6. PATCH – Update only device state
curl -i -X PATCH http://localhost:3000/api/v2/devices/DEV-101 `
-H "Content-Type: application/json" `
-d '{ "device_state": "offline" }'


7. DELETE – Remove device
curl -i -X DELETE http://localhost:3000/api/v2/devices/DEV-116