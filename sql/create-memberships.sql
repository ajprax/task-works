CREATE TABLE memberships (
  group_parent_id INT NOT NULL,
  group_child_id INT NOT NULL,
  PRIMARY KEY (group_parent_id),
  FOREIGN KEY (group_parent_id) REFERENCES groups(id),
  FOREIGN KEY (group_child_id) REFERENCES groups(id)
)
