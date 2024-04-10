"""alter type

Revision ID: 4a46ba54a3f3
Revises: c97c445e2bdb
Create Date: 2022-03-27 21:50:10.911649

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "4a46ba54a3f3"
down_revision = "c97c445e2bdb"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("subscribe", schema=None) as batch_op:
        batch_op.alter_column(
            "categories",
            existing_type=sa.VARCHAR(length=1024),
            type_=sa.JSON(),
            existing_nullable=True,
            postgresql_using="categories::json",
        )
        batch_op.alter_column(
            "tags",
            existing_type=sa.VARCHAR(length=1024),
            type_=sa.JSON(),
            existing_nullable=True,
            postgresql_using="tags::json",
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("subscribe", schema=None) as batch_op:
        batch_op.alter_column(
            "tags",
            existing_type=sa.JSON(),
            type_=sa.VARCHAR(length=1024),
            existing_nullable=True,
        )
        batch_op.alter_column(
            "categories",
            existing_type=sa.JSON(),
            type_=sa.VARCHAR(length=1024),
            existing_nullable=True,
        )

    # ### end Alembic commands ###
