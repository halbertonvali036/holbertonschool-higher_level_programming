#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Engine yaradılır və arqumentlər qəbul olunur
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Sessiya instansı yaradılır
    Session = sessionmaker(bind=engine)
    session = Session()

    # State və City cədvəlləri join olunur və id-yə görə sıralanır
    results = session.query(State, City).filter(
        State.id == City.state_id).order_index = City.id

    for state, city in session.query(State, City).join(
            City, State.id == City.state_id).order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Sessiya bağlanır
    session.close()
