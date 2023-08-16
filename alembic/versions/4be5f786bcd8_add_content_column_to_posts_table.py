"""add content column to posts table

Revision ID: 4be5f786bcd8
Revises: 6b18ea056ba4
Create Date: 2023-08-10 11:30:19.873255

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4be5f786bcd8'
down_revision: Union[str, None] = '6b18ea056ba4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
