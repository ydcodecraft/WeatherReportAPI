# to use alembic autogenerate feature, need to import all the tables and the db connection in this init file

from .accessHistory import AccessHistory
from .city import City

from database import Base