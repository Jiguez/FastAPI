"""create phone number for user col

Revision ID: 2dbee0b873ae
Revises: 
Create Date: 2023-05-31 07:22:52.508318

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2dbee0b873ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))


def downgrade():
    op.drop_column('users','phone_number')
