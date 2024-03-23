#!/usr/bin/python3
"""
deletes all State objects
with a name containing the letter a
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def main():
    usrname = sys.argv[1]
    pswd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(usrname, pswd, db))

    Session = sessionmaker(bind=engine)
    session = Session()

    rows_to_delete = session.query(State).filter(State.name.like('%a%'))

    for row in rows_to_delete:
        session.delete(row)

    session.commit()


if __name__ == "__main__":
    main()
