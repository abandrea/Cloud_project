from locust import HttpUser, task, between

class NextcloudUser(HttpUser): # first test
    wait_time = between(1, 5) # wait time between 5 and 9 seconds before executing the next task

    def on_start(self):
        self.login() # call the login function

    def login(self): # login function
        response = self.client.post("/login", data={"username": "ab_andrea", "password": "@PFLX9HDSZrhjt3"})
        if response.status_code != 200:
            print("Login failed")

    @task # task decorator
    def upload_file(self): # upload_file function
        self.client.post(
            #"/upload", # path to upload file
                         files={"file": open("test.txt", "rb")})

    @task
    def download_file(self): # download_file function
        self.client.get("/download/test.txt")

# this test will simulate login, upload and download of a file