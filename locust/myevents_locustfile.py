from locust import HttpUser, task, between

class MyEventsUser(HttpUser):
    host = "http://localhost:8000"  
    wait_time = between(1, 2)

    @task
    def view_my_events(self):
        self.client.get("/my-events?user=locust_user")