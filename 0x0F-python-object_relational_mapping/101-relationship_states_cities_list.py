#!/usr/bin/python3
"""
lists all State objects and corresponding Cities using cities relationship
using SQLAlchemy and importing State and Base from relationship_state
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]), pool_pre_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        for instance in session.query(State).order_by(State.id):
                print("{}: {}".format(instance.id, instance.name))
                for inst in instance.cities:
                        print("\t{}: {}".format(inst.id, inst.name))
        session.close()
