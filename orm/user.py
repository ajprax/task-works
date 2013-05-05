from __init__ import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from group import Group

class User(Base):
  """
  Represents records in the taskworks.users table.
  """
  __tablename__ = "users"

  # Columns in the taskworks.users table.
  id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
  login = Column(String, nullable=False)
  password = Column(String, nullable=False)

  group = relationship(Group, uselist=False, backref="user")

  def __init__(self, login_param, password_param):
    """
    Creates a new user record.

    :param login_param the login name of the user.
    :param password_param the login password of the user.
    """
    self.login = login_param
    self.password = password_param

  # TODO make this not print passwords
  def __repr__(self):
    return "<User('%s','%s','%s')>" % (self.id, self.login, self.password)
