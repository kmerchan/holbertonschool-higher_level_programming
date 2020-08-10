#!/usr/bin/python3
"""
creates State 'California' with City 'San Francisco'
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
        session.add(State(name='California',
                          cities=[City(name='San Francisco')]))
        session.commit()
        session.close()
