import databases
import sqlalchemy
from functools import lru_cache
from configs import dbinfo
from db.table import metadata
from pydantic import BaseSettings

class Setting(BaseSettings):
    db_connection: str
    db_host: str
    db_port: str
    db_database: str
    db_username: str
    db_password: str


@lru_cache()
def db_config():
    return dbinfo.Setting()

def DATABASE_URL(
    connection: str = "postgresql",
    username: str   = "pacis",
    password: str   = "123",
    host: str       = "127.0.0.1",
    port: str       = "5432",
    database: str   = "Home_economy"
):
    return str(connection+"://lrcbqxortfgumm:4ef5aae613c7e2caaf6bc39ae950e9d670e401a4d6af5a866c5fa5ee5abaf7f6@ec2-34-233-157-189.compute-1.amazonaws.com:5432/d655pfbfgl0o78")


database = databases.Database(DATABASE_URL())

engine = sqlalchemy.create_engine(
    DATABASE_URL()
)

metadata.create_all(engine)