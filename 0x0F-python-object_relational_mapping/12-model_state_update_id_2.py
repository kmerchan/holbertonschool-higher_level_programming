#!/usr/bin/python3
"""
updates the name of State with id = 2 to be 'New Mexico'
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
        update_state = session.query(State).filter_by(id=2)
        update_state.name = 'New Mexico'
        session.commit()
        session.close()
