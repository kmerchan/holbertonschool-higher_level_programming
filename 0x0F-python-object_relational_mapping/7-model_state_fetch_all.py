#!/usr/bin/python3
"""
lists all State objects from the database in ascending order
using SQLAlchemy and importing State and Base from model_state
"""
from sys import argv
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]), pool_pre_ping=True)
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)
        for instance in session.query(State).order_by(State.id):
                print("{}: {}", State.id, State.name)
        session.close()
