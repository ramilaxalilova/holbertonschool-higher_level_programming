#!/usr/bin/python3
"""
lists all State objects
that contain the letter a
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def main():
    usrname = sys.argv[1]
    pswd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(usrname, pswd, db))

    Session = sessionmaker(bind=engine)
    session = Session()

    s = session.query(State).filter(State.name.like('%a%')).order_by(State.id)
    for state in s:
        print("{}: {}".format(state.id, state.name))


if __name__ == "__main__":
    main()
