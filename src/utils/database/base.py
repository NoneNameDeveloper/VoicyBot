from data import config

import sqlalchemy

import databases
import ormar


database = databases.Database(config.DATABASE_URL)

metadata = sqlalchemy.MetaData()


# meta class
class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database



# creating engine
engine = sqlalchemy.create_engine(config.DATABASE_URL)
metadata.bind = engine

# table creating
metadata.create_all(engine)