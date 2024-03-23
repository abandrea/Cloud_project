import os
from locust import HttpUser, task, between
import random
import logging

logging.basicConfig(level=logging.INFO)

class NextcloudUser(HttpUser):
    wait_time = between(1, 5) # Wait time between 1 and 5 seconds

    def on_start(self):
        # Initialize user credentials
        user_index = random.randint(0, 49)  # Randomly pick a user between user1 and user50
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

    @task(1) # Create a small size file (kb) and test load on the server, then delete it
    def upload_file(self):
        # Simulate file upload and delete
        with open("test.txt", "rb") as file:
            self.client.put(f"/remote.php/dav/files/{self.username}/test.txt", 
                            data=file, 
                            auth=self.auth)
            self.client.delete(f"/remote.php/dav/files/{self.username}/test.txt",
                               auth=self.auth)
            
            # logging info is used to log the response of the upload request
            #logging.info(f"Upload Response: {response.status_code} - {response.text}")
    
    @task(1) # Create a medium file (Mb) and test load on the server, then delete it
    def upload_image(self):
        # Simulate image upload
        with open("NGC_2276.jpg", "rb") as file:
            self.client.put(f"/remote.php/dav/files/{self.username}/NGC_2276.jpg", 
                            data=file, 
                            auth=self.auth)
            self.client.delete(f"/remote.php/dav/files/{self.username}/NGC_2276.jpg",
                                auth=self.auth)
            # logging info is used to log the response of the upload request
            #logging.info(f"Upload Response: {response.status_code} - {response.text}")

    @task(1) # Create a large file (Gb) and test load on the server, then delete it
            # Firstly, we need to create a large file to upload
            # since is not possible to upload a large file directly to github,
            # it was created a large file inside the definition of the task
            # and then uploaded to the server
    def upload_large_file(self):
        filename = "large_file.txt"
        # Create a large file
        with open(filename, "wb") as file:
            file.write(b'\0' * (1024 * 1024 * 1024))  # 1 GB file size

        # Initialize the upload, but with try and except to avoid errors in the test
        # try:
        with open(filename, "rb") as file:
            self.client.put(f"/remote.php/dav/files/{self.username}/{filename}", 
                                data=file, 
                                auth=self.auth)
            self.client.delete(f"/remote.php/dav/files/{self.username}/{filename}",
                                   auth=self.auth)
            # # then delete the file
            # self.client.delete(f"/remote.php/dav/files/{self.username}/{filename}",
            #                    auth=self.auth)
            
        # except Exception as e:
        #     logging.error(f"Error uploading large file: {e}")
        
        # finally: # clean up the file from the local storage after the creation if uploaded but not executed try block
        #     if os.path.exists(filename):
        #         os.remove(filename)


# This is the original code before the modification, not used in the extra test    
    # def upload_large_file(self):
    #     # Simulate large file upload
    #     with open("large_file.txt", "wb") as file:
    #         file.seek(1024*1024*1024)
    #         file.write(b"\0")
    #         file.seek(0)
    #         self.client.put(f"/remote.php/dav/files/{self.username}/large_file.txt", 
    #                         data=file, 
    #                         auth=self.auth)
    #         self.client.delete(f"/remote.php/dav/files/{self.username}/large_file.txt",
    #                             auth=self.auth)
    #         # logging info is used to log the response of the upload request
    #         #logging.info(f"Upload Response: {response.status_code} - {response.text}")
