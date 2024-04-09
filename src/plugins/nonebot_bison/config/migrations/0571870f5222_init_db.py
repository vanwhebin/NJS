"""init db

Revision ID: 0571870f5222
Revises:
Create Date: 2022-03-21 19:18:13.762626

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "0571870f5222"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "target",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("platform_name", sa.String(length=20), nullable=False),
        sa.Column("target", sa.String(length=1024), nullable=False),
        sa.Column("target_name", sa.String(length=1024), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("type", sa.String(length=20), nullable=False),
        sa.Column("uid", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "subscribe",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("target_id", sa.Integer(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("categories", sa.String(length=1024), nullable=True),
        sa.Column("tags", sa.String(length=1024), nullable=True),
        sa.ForeignKeyConstraint(
            ["target_id"],
            ["target.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("subscribe")
    op.drop_table("user")
    op.drop_table("target")
    # ### end Alembic commands ###
