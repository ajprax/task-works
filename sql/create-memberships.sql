CREATE TABLE memberships (
  group_id1 INT NOT NULL,
  group_id2 INT NOT NULL,
  PRIMARY KEY (group_id1),
  FOREIGN KEY (group_id1) REFERENCES groups(id),
  FOREIGN KEY (group_id2) REFERENCES groups(id)
)
