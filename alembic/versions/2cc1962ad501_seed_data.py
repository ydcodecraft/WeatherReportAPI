"""seed data

Revision ID: 2cc1962ad501
Revises: c05f99e7c2a0
Create Date: 2024-09-12 17:20:45.171135

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import Session
from app.models import City

# revision identifiers, used by Alembic.
revision: str = '2cc1962ad501'
down_revision: Union[str, None] = 'c05f99e7c2a0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()
    session = Session(bind=bind)

    edmonton = City(name="Edmonton")
    london = City(name="London")
    newYork = City(name="New York")
    sydney = City(name="Syndey")

    session.add_all([edmonton, london, newYork,sydney])
    session.commit()


def downgrade() -> None:
    bind = op.get_bind()
    session = Session(bind=bind)

    session.query(City).delete()
    session.commit()