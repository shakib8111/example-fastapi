"""create posts table

Revision ID: 6b18ea056ba4
Revises: 
Create Date: 2023-08-09 11:50:36.539022

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b18ea056ba4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("posts",
                    sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
                    sa.Column("title", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
