#!/bin/bash

# This script is used to test the nextcloud-docker project.

# define some variables
URL="http://localhost:8080/ocs/v1.php/cloud/users"
USERNAME="ab_andrea"
PASSWORD="H#8@$rkBvFVj9t"

# Function to create users
create_users() {
  for i in {1..5}
  do 
    echo "Creating user user$i"
    docker exec -u www-data -e OC_PASS="password$i" nextcloud-docker-nextcloud-1 php occ user:add --password-from-env "user$i"
  done
}

# Function to delete users
delete_users() {
  for i in {1..5}
  do 
    echo "Deleting user: user$i"
    docker exec -u www-data nextcloud-docker-nextcloud-1 php occ user:delete "user$i"
  done
}

# create users
create_users

#Run the locust test
locust -f test_two.py --host http://localhost:8080

# cleanup
echo "Cleaning up"
delete_users

echo "Test and cleanup complete."

# end!
 
