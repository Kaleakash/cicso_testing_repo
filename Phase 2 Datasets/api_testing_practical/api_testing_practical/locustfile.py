from locust import HttpUser, between, task


class DeviceAPIUser(HttpUser):
    # Each virtual user waits 1 to 3 seconds between tasks.
    wait_time = between(1, 3)

    @task(3)
    def list_devices(self):
        self.client.get("/devices", name="GET /devices")

    @task(1)
    def get_existing_device(self):
        self.client.get("/devices/101", name="GET /devices/{device_id}")
