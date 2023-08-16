"""add last few columns to the posts table

Revision ID: 54cf10277e9e
Revises: 3937c9cea83c
Create Date: 2023-08-10 12:02:47.762060

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '54cf10277e9e'
down_revision: Union[str, None] = '3937c9cea83c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"))
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False,
                                     server_default=sa.text("NOW()")))
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
