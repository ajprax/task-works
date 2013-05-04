CREATE TABLE assignments (
  group_id INT NOT NULL,
  task_id INT NOT NULL,
  PRIMARY KEY (group_id),
  FOREIGN KEY (group_id) REFERENCES groups(id),
  FOREIGN KEY (task_id) REFERENCES tasks(id)
)
