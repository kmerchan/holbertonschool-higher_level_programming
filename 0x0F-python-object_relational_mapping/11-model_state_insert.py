#!/usr/bin/python3
"""
adds 'Louisiana' object to the database
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
        session.add(State(name='Louisiana'))
        session.commit()
        for instance in session.query(State).filter_by(name='Louisiana'):
                print(instance.id)
        session.close()
