import databases
import sqlalchemy
from functools import lru_cache
from configs import dbinfo
from db.table import metadata

@lru_cache()
def db_config():
    return dbinfo.Setting()

def DATABASE_URL(
    connection: str = "postgresql",
    username: str   = "lrcbqxortfgumm",
    password: str   = "4ef5aae613c7e2caaf6bc39ae950e9d670e401a4d6af5a866c5fa5ee5abaf7f6",
    host: str       = "ec2-34-233-157-189.compute-1.amazonaws.com",
    port: str       = "5432",
    database: str   = "d655pfbfgl0o78"
):
    return str(connection+"://"+username+":"+password+"@"+host+":"+port+"/"+database)

database = databases.Database(DATABASE_URL())

engine = sqlalchemy.create_engine(
    DATABASE_URL()
)

metadata.create_all(engine)