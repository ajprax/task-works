CREATE TABLE subtasks (
  task_id1 INT NOT NULL,
  task_id2 INT NOT NULL,
  PRIMARY KEY (task_id1),
  FOREIGN KEY (task_id1) REFERENCES tasks(id),
  FOREIGN KEY (task_id2) REFERENCES tasks(id)
)
