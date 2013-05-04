#!/bin/sh

# List schemas of all the tables.
echo "Describing 'users' table..."
echo "describe users;" | mysql -u root -p taskworks
echo

echo "Describing 'tasks' table..."
echo "describe tasks;" | mysql -u root -p taskworks
echo

echo "Describing 'groups' table..."
echo "describe groups;" | mysql -u root -p taskworks
echo

echo "Describing 'memberships' table..."
echo "describe memberships;" | mysql -u root -p taskworks
echo

echo "Describing 'assignments' table..."
echo "describe assignments;" | mysql -u root -p taskworks
echo

echo "Describing 'subtasks' table..."
echo "describe subtasks;" | mysql -u root -p taskworks
echo
