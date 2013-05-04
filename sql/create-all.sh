#!/bin/sh

# Create the database.
echo "Creating 'taskworks' database..."
mysql -u root -p < create-taskworks.sql


# Create the tables.
echo "Creating 'users' table..."
mysql -u root -p taskworks < create-users.sql

echo "Creating 'tasks' table..."
mysql -u root -p taskworks < create-tasks.sql

echo "Creating 'groups' table..."
mysql -u root -p taskworks < create-groups.sql

echo "Creating 'memberships' table..."
mysql -u root -p taskworks < create-memberships.sql

echo "Creating 'assignments' table..."
mysql -u root -p taskworks < create-assignments.sql

echo "Creating 'subtasks' table..."
mysql -u root -p taskworks < create-subtasks.sql

echo "Done!"
