from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from user import User
from group import Group

engine = create_engine('mysql+mysqldb://root:aj00prax@localhost:3306/taskworks?charset=utf8')
user = User("notme", "hoop")

Session = sessionmaker(bind=engine)
session = Session()

session.add(user)

our_user = session.query(User).filter_by(login='notme').all()
print(our_user)

session.commit()

group = Group(2, "ajprax")
print(group)
session.add(group)

session.commit()
