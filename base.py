from sqlalchemy import MetaData
from sqlalchemy import create_engine


def connect_database(ulr):
    engine = create_engine(ulr)
    metadata = MetaData()
    metadata.reflect(engine)
    return engine, metadata

