#!/bin/bash

# test.sh
# This script is used to set up users for the nextcloud-docker project and run the Locust test.

# define some variables
URL="http://localhost:8080"
LOCUST_FILE="test_incr.py" 
# Extra test file - it wasn't added to the report
#LOCUST_FILE="extra.py"

# Function to create users
create_users() {
  for i in {1..20}
  do 
    echo "Creating user user$i"
    docker exec -u www-data -e OC_PASS="password$i" nextcloud-docker-nextcloud-1 php occ user:add --password-from-env "user$i"
  done
}

# Function to delete users
delete_users() {
  for i in {1..20}
  do 
    echo "Deleting user: user$i"
    docker exec -u www-data nextcloud-docker-nextcloud-1 php occ user:delete "user$i"
  done
}

# create users
create_users

# Run the locust test with web UI
locust -f $LOCUST_FILE --host=$URL

# The script will pause here, and the user will manually control the test via Locust's web UI.
# After the test is finished and the web UI is closed, the script will resume to clean up.

# cleanup
echo "Cleaning up..."
delete_users

echo "Test and cleanup complete."
