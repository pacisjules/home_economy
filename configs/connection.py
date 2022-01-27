import databases
import sqlalchemy
from functools import lru_cache
from configs import dbinfo
from db.table import metadata


import os
import re

uri = os.getenv("postgres://lrcbqxortfgumm:4ef5aae613c7e2caaf6bc39ae950e9d670e401a4d6af5a866c5fa5ee5abaf7f6@ec2-34-233-157-189.compute-1.amazonaws.com:5432/d655pfbfgl0o78")  # or other relevant config var
if uri.startswith("postgres://lrcbqxortfgumm:4ef5aae613c7e2caaf6bc39ae950e9d670e401a4d6af5a866c5fa5ee5abaf7f6@ec2-34-233-157-189.compute-1.amazonaws.com:5432/d655pfbfgl0o78"):
    uri = uri.replace("postgres://lrcbqxortfgumm:4ef5aae613c7e2caaf6bc39ae950e9d670e401a4d6af5a866c5fa5ee5abaf7f6@ec2-34-233-157-189.compute-1.amazonaws.com:5432/d655pfbfgl0o78", "postgresql://lrcbqxortfgumm:4ef5aae613c7e2caaf6bc39ae950e9d670e401a4d6af5a866c5fa5ee5abaf7f6@ec2-34-233-157-189.compute-1.amazonaws.com:5432/d655pfbfgl0o78", 1)
# rest of connection code using the connection string `uri`



""" @lru_cache()
def db_config():
    return dbinfo.Setting()

def DATABASE_URL(
    connection: str = "postgres",
    username: str   = "lrcbqxortfgumm",
    password: str   = "4ef5aae613c7e2caaf6bc39ae950e9d670e401a4d6af5a866c5fa5ee5abaf7f6",
    host: str       = "ec2-34-233-157-189.compute-1.amazonaws.com",
    port: str       = "5432",
    database: str   = "d655pfbfgl0o78"
):
    return str("postgres://lrcbqxortfgumm:4ef5aae613c7e2caaf6bc39ae950e9d670e401a4d6af5a866c5fa5ee5abaf7f6@ec2-34-233-157-189.compute-1.amazonaws.com:5432/d655pfbfgl0o78")

database = databases.Database(DATABASE_URL())

engine = sqlalchemy.create_engine(
    DATABASE_URL()
) """





metadata.create_all(engine)