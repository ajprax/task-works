CREATE TABLE groups (
  id INT NOT NULL AUTO_INCREMENT,
  user_id INT,
  name TINYTEXT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id)
)
