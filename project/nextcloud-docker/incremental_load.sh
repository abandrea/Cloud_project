#!/bin/bash

# This script is used to test the nextcloud-docker project incrementally.

# define some variables
HOST="http://localhost:8080"
LOCUST_FILE="test_two.py" # make sure this is the correct path to your locust file

# Initial number of users
INITIAL_USERS=1

# Users to add each increment
USER_INCREMENT=10

# Maximum number of users
MAX_USERS=50

# Hatch rate (users spawned per second)
HATCH_RATE=5

# Duration for each step of the test
STEP_DURATION="30s"

# Locust command (without the number of users and hatch rate)
LOCUST_CMD="locust -f $LOCUST_FILE --headless --host $HOST"

# Function to create users
create_users() {
  for i in {1..10}
  do 
    echo "Creating user user$i"
    docker exec -u www-data -e OC_PASS="password$i" nextcloud-docker-nextcloud-1 php occ user:add --password-from-env "user$i"
  done
}

# Function to delete users
delete_users() {
  for i in {1..10}
  do 
    echo "Deleting user: user$i"
    docker exec -u www-data nextcloud-docker-nextcloud-1 php occ user:delete "user$i"
  done
}

# create users
create_users

# Incrementally run the load test
current_users=$INITIAL_USERS
while [ $current_users -le $MAX_USERS ]; do
  echo "Running test with $current_users users..."
  $LOCUST_CMD -u $current_users -r $HATCH_RATE --run-time $STEP_DURATION
  
  # Increase the number of users for the next increment
  let current_users+=$USER_INCREMENT
  
  # Short delay to let the system stabilize before the next increment
  echo "Waiting for system to stabilize..."
  sleep 30
done

# cleanup
echo "Cleaning up..."
delete_users

echo "Incremental load test complete."
