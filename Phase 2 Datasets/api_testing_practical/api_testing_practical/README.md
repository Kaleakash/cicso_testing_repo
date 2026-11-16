# API Testing Practical Project


- **Functional API testing:** `pytest` + `httpx`
- **Load testing:** `Locust`
- **API application:** FastAPI

The sample API manages devices. The project demonstrates successful requests, missing resources, JSON validation, POST requests, a protected endpoint, automated assertions, virtual users, task execution, wait time, response time, requests per second (RPS), and failures.

## 1. Project structure

```text
api_testing_practical/
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   ├── test_devices.py
│   └── test_auth.py
├── locustfile.py
├── requirements.txt
└── README.md
```

## 2. Prerequisites


```bash
python3 --version
python3 -m pip --version
```


## 3. Create and activate a virtual environment

Open a terminal in the `api_testing_practical` folder.

## Linux 

```bash
python3 -m venv .venv
source .venv/bin/activate
```

When activated, the terminal normally displays `(.venv)`.

## 4. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The dependencies are:

- `fastapi` – builds the sample REST API.
- `uvicorn` – runs the API server.
- `pytest` – discovers and executes automated tests.
- `httpx` – sends HTTP requests from test code.
- `locust` – simulates virtual users for load testing.

## 5. Start the API application

From the project root, run:

```bash
uvicorn app.main:app --reload
```

Expected startup address:

```text
http://127.0.0.1:8000
```

Keep this terminal running.

Open the interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

Useful endpoints:

| Method  | Endpoint              | Purpose                       | Expected result |
|---      |---                    |---                            |---              |
| GET     | `/`                   | Health check                  | 200             |
| GET     | `/devices`            | List devices                  | 200             |
| GET     | `/devices/101`        | Get an existing device        | 200             |
| GET     | `/devices/99999`      | Get a missing device          | 404             |
| POST    | `/devices`            | Create a device               | 201             |
| POST    | `/auth/token`         | Get the demo token            | 200             |
| GET     | `/protected/devices`  | Access protected device list  | 200 with token; 401 without token |

### Sample GET response

`GET http://127.0.0.1:8000/devices`

```json
[
  {
    "device_id": 101,
    "hostname": "edge-01",
    "status": "online"
  },
  {
    "device_id": 102,
    "hostname": "edge-02",
    "status": "offline"
  }
]
```

### Sample POST request

`POST http://127.0.0.1:8000/devices`

Body → raw → JSON:

```json
{
  "hostname": "edge-03",
  "status": "online"
}
```

Expected status: `201 Created`.

## 6. Run functional API tests with pytest and httpx

Open a **second terminal** in the project root. Activate the same virtual environment in this terminal.

### Run all tests

```bash
pytest -v
```

### Run one test file

```bash
pytest -v tests/test_devices.py
```

```bash
pytest -v tests/test_auth.py
```

### Run one test by name

```bash
pytest -v tests/test_devices.py::test_get_existing_device
```

The API server from Step 5 must remain running while tests execute.

### What the tests demonstrate

| Test                                      | Scenario              | Expected behavior       |
|---                                        |---                    |                ---      |
| `test_get_devices`                        | List devices          | 200 and JSON array      |
| `test_get_existing_device`                | Existing device 101   | 200 and expected fields |
| `test_get_missing_device`                 | Unknown device 99999  | 404                     |
| `test_create_device`                      | Create a device       | 201 and created data    |
| `test_protected_devices_with_valid_token` | Valid bearer token    | 200                     |
| `test_protected_devices_without_token`    | Missing token         | 401                     |

**Important:** A negative test can PASS when the API correctly returns an expected error such as 404 or 401. The test result is about whether actual behavior matches expected behavior.

### Change the API base URL (optional)

By default, tests use:

```text
http://127.0.0.1:8000
```

Linux 

```bash
export BASE_URL="http://127.0.0.1:8000"
pytest -v
```

## 7. Run load testing with Locust

Keep the API server running.

Open a **third terminal** in the project root, activate the virtual environment, and run:

```bash
locust -f locustfile.py
```

Open the Locust web interface:

```text
http://localhost:8089
```

On the Locust start page, enter:

- **Number of users:** `10`
- **Spawn rate:** `2` users per second
- **Host:** `http://127.0.0.1:8000`

Click **Start**.

Locust will create simulated users. Each user repeatedly calls the sample GET endpoints and waits between tasks.

### Suggested classroom experiments

Run separate experiments and compare the results:

| Experiment  | Users | Spawn rate  |
|---          |---:   |---        : |
| 1           | 1     | 1           |
| 2           | 10    | 2           |
| 3           | 20    | 5           |
| 4           | 50    | 5           |

These are demonstration settings, not performance targets. Run only against this local training API or another system for which you have explicit permission to perform load testing. Avoid sending high load to shared or production systems.

### Locust metrics to observe

- **Users:** active simulated users.
- **Requests:** total requests executed.
- **Failures:** requests that did not succeed.
- **Median / response time:** how long requests take.
- **RPS:** requests completed per second.

Do not judge performance from RPS alone. Compare response time and failures as the user count increases.

### Stop the test

Click **Stop** in the Locust UI. Stop the API server with `Ctrl + C` in its terminal when finished.

## 8. Run Locust in headless mode (optional)

This runs without opening the web UI:

```bash
locust -f locustfile.py --host http://127.0.0.1:8000 --headless -u 10 -r 2 -t 1m
```

Options:

- `-u 10` – total number of simulated users.
- `-r 2` – spawn two users per second.
- `-t 1m` – run for one minute.
- `--headless` – run from the terminal without the web UI.

## 9. Troubleshooting

### `Connection refused` or `ConnectError`

- Confirm the API server is running.
- Confirm the terminal shows `http://127.0.0.1:8000`.
- Check that `BASE_URL` points to the same host and port.

### `pytest: command not found`

Activate the virtual environment and install dependencies:

```bash
python -m pip install -r requirements.txt
```

You can also run:

```bash
python -m pytest -v
```

### `locust: command not found`

Activate the virtual environment and install dependencies:

```bash
python -m pip install locust
```

Then run:

```bash
python -m locust -f locustfile.py
```

### Port 8000 is already in use

Run the API on another port:

```bash
uvicorn app.main:app --reload --port 8001
```

