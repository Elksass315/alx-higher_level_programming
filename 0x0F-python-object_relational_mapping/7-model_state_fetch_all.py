#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""
if __name__ == '__main__':
    from model_state import Base, State
    import sys
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    conn = f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}'
    engine = create_engine(conn, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for stateId, state in session.query(State.id, State.name):
        print(f"{stateId}: {state}")
