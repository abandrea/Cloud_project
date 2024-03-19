import os
from locust import HttpUser, task, between
import random
import logging

logging.basicConfig(level=logging.INFO)

class NextcloudUser(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        # Initialize user credentials
        user_index = random.randint(1, 5)  # Randomly pick a user between user1 and user5
        self.username = f"user{user_index}"
        self.password = f"password{user_index}"
        self.auth = (self.username, self.password)
        self.login()

    def login(self):
        # Perform login for each user
        self.client.post("/login", {
            "user": self.username,
            "password": self.password
        })

    @task(1)
    def upload_file(self):
        # Simulate file upload
        with open( "test.txt", "rb") as file:
            response = self.client.put(f"/remote.php/dav/files/{self.username}/test.txt", 
                            data=file, 
                            auth=self.auth)
            logging.info(f"Upload Response: {response.status_code} - {response.text}")

    @task(1)
    def download_file(self):
        # Simulate file download
        response = self.client.get(f"/remote.php/dav/files/{self.username}/test.txt", 
                        auth=self.auth)
        logging.info(f"Download Response: {response.status_code} - {response.text}")


# this test will simulate login, upload and download of a file
