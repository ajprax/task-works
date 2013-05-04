import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="aj00prax", db="taskworks")

# create a cursor
cur = db.cursor()

group_name = raw_input('What is the name of the group?\n')
group_members = []
group_member = raw_input('What is the name of a member to add?\n')
if group_member == "":
  # Assume no more member groups to add, move on.
else:
  cur.execute("SELECT id,name from taskworks.groups")
  member_group_exists = false
  for row in cur.fetchall() :
    if (row[1] == group_member)
      member_group_exists = true
  if (member_group_exists):
    # stage the entry for the relation table to be committed atomically later
    group_members.append(row[0])
  else:
    print("There is no group named: %s" % group_member)
  #ask again.  factor this to a method


cur.execute("INSERT INTO `taskworks`.`groups` (`name`) VALUES ('%s')" % group_name)
for member in group_members:
  # TODO fill out this line for the membership table
  cur.execute("INSERT INTO `taskworks`.`memberships` (`group_parent_id`, `group_child_id`) VALUES ('%s', '%s') % member


cur.execute("SELECT id,name FROM taskworks.groups")
for row in cur.fetchall() :
  print(row)


cur.close()
db.close()
