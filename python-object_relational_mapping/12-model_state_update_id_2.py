#!/usr/bin/python3
""" changes the name of a State object """
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

    updated_row = session.query(State).filter_by(id=2).first()

    updated_row.name = 'New Mexico'
    session.commit()


if __name__ == "__main__":
    main()
