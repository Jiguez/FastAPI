"""createapt number for address col

Revision ID: 80b5397070ee
Revises: 0a992c15035f
Create Date: 2023-06-01 09:39:06.516428

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80b5397070ee'
down_revision = '0a992c15035f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('address', sa.Column('apt_number', sa.String(), nullable=True))


def downgrade():
    op.drop_column('address', 'apt_number')
