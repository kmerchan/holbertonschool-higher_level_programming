#!/usr/bin/python3
"""
lists State object from the database that matches argument given
using SQLAlchemy and importing State and Base from model_state
"""
from sys import argv
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]), pool_pre_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        instance = session.query(State).filter(State.name==argv[4])
        if instance is not None:
                print("{}".format(instance.id))
        else:
                print("Not found")
        session.close()
