#!/usr/bin/python3
"""
prints the first State object from the database without fetch all states
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
        try:
                for instance in session.query(State).filter_by(id=1):
                        print("{}: {}", State.id, State.name)
        except:
                print("Nothing")
        session.close()
