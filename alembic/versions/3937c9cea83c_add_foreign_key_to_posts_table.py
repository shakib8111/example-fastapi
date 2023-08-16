"""add foreign key to posts table

Revision ID: 3937c9cea83c
Revises: 367e28e234a5
Create Date: 2023-08-10 11:55:13.189415

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3937c9cea83c'
down_revision: Union[str, None] = '367e28e234a5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("posts_users_fk", source_table="posts", referent_table="users",
                          local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint("posts_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
