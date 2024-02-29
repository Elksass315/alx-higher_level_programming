#!/usr/bin/python3
"""prints the first State object from the database hbtn_0e_6_usa"""
if __name__ == '__main__':
    from model_state import Base, State
    import sys
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    co = f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}'
    engine = create_engine(co, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(State).where(State.id == 2)\
        .update({'name': 'New Mexico'})
    session.commit()
    session.close()
