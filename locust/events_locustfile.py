from locust import HttpUser, task, between

class EventsUser(HttpUser):
    host = "http://localhost:8000"  
    wait_time = between(1, 2)

    @task
    def view_events(self):
        self.client.get("/events?user=locust_user")