#!/usr/bin/python3
"""
Prints all City objects from the database `hbtn_0e_14_usa`
"""
from sys import argv
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                           argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in (session.query(State.name, City.id, City.name)
                     .filter(State.id == City.state_id)
                     .order_by(City.id)):
        print(f"{instance[0]}: ({instance[1]}) {instance[2]}")

    session.close()
