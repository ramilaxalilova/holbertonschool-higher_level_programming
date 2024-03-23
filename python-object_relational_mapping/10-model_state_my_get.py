#!/usr/bin/python3
"""
prints the State object
with the name passed as argument
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def main():
    usrname = sys.argv[1]
    pswd = sys.argv[2]
    db = sys.argv[3]
    arg = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(usrname, pswd, db))

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == "{}".format(arg)).first()

    if state:
        print(state.id)
    else:
        print("Not found")


if __name__ == "__main__":
    main()
