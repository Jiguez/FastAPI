"""Create address_id to users

Revision ID: 0a992c15035f
Revises: d870184d7bef
Create Date: 2023-05-31 08:26:03.328885

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a992c15035f'
down_revision = 'd870184d7bef'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('address_id', sa.Integer(), nullable=True))
    op.create_foreign_key('address_users_fk', source_table='users',referent_table='address',local_cols=['address_id'], remote_cols=["id"], ondelete="CASCADE")


def downgrade():
    op.drop_constraint('address_users_fk', table_name="users")
    op.drop_constraint('users', 'address_id')

