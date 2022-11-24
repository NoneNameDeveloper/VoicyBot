from .base import BaseMeta

import sqlalchemy
import databases
import ormar


# USER MODEL
class User(ormar.Model):
    class Meta(BaseMeta):
        tablename = "user"
    
    user_id = ormar.Integer(primary_key=True)

