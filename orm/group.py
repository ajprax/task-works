from __init__ import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
#from user import User

class Group(Base):
  """
  Represents records in the taskworks.groups table.
  """
  __tablename__ = "groups"

  # Columns in the taskworks.groups table.
  id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
  user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
  name = Column(String, nullable=False)

  #user = relationship(User, uselist=False, backref="group")

  def __init__(self, user_id_param, name_param):
    """
    Creates a new group record.

    :param user_id_param the user_id of the owner of this group if it is a singleton.
    :param name_param the name of this group.
    """
    self.user_id = user_id_param
    self.name = name_param

  def __repr__(self):
    return "<Group('%s','%s','%s')>" % (self.id, self.user_id, self.name)
