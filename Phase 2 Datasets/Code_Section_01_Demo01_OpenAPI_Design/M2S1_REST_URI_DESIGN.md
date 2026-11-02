# Module 2 Section 1 — REST URI Design

## Requirement
NetPulse needs a Device Management API that allows clients to:
1. List all devices.
2. Create a new device.
3. Retrieve one device by its device ID.

## Resource
devices

## RESTful URI design
| Requirement | Method | URI |
|---|---|---|
| List devices | GET | `/devices` |
| Create a device | POST | `/devices` |
| Retrieve one device by ID | GET | `/devices/{device_id}` |

## Parameter reminder
`/devices/{device_id}` means `{device_id}` is replaced by a real integer, for example `/devices/101`.
