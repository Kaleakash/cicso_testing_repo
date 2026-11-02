# NetPulse Devices API — Sample Requests

Public:
- GET /devices
- GET /devices/1

Authentication:
- POST /auth/token using form fields username/password

Protected operations use:
`Authorization: Bearer <token>`

POST /devices:
```json
{"name":"Firewall-01","device_type":"firewall","status":"online","location":"Bangalore-DC"}
```

PUT /devices/{id}:
```json
{"name":"Firewall-Core","device_type":"firewall","status":"maintenance","location":"Bangalore-DC"}
```

PATCH /devices/{id}:
```json
{"status":"online"}
```
