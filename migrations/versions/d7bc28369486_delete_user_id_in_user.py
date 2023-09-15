"""delete user_id in user

Revision ID: d7bc28369486
Revises: bc7488bd1143
Create Date: 2023-09-15 12:02:41.767153

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d7bc28369486"
down_revision: Union[str, None] = "bc7488bd1143"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, "task", ["id"])
    op.drop_constraint("user_user_id_key", "user", type_="unique")
    op.drop_column("user", "user_id")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "user", sa.Column("user_id", sa.UUID(), autoincrement=False, nullable=False)
    )
    op.create_unique_constraint("user_user_id_key", "user", ["user_id"])
    op.drop_constraint(None, "task", type_="unique")
    # ### end Alembic commands ###