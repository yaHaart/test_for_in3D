
from sqlalchemy import (Column, DateTime, Integer, MetaData, String, Table,
                        create_engine)
from sqlalchemy.sql import func
from databases import Database


DATABASE_URL = 'postgresql://haart:keen@localhost:5432/mydb'

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()
managers = Table(
    "managers",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("surname", String(50)),
    Column("job_name", String(50)),
    Column("department", String(50)),
    Column("birthday", String(50)),
)
workers = Table(
    "workers",
    metadata,
    Column("manager_id", Integer),
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("surname", String(50)),
    Column("job_name", String(50)),
    Column("department", String(50)),
    Column("birthday", String(50)),
)

# databases query builder
database = Database(DATABASE_URL)

