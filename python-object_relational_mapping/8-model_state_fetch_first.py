#!/usr/bin/python3
""" prints the first State object """
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

    state = session.query(State).first()
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")


if __name__ == "__main__":
    main()
