"""Create address table

Revision ID: d870184d7bef
Revises: 2dbee0b873ae
Create Date: 2023-05-31 08:01:03.020558

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd870184d7bef'
down_revision = '2dbee0b873ae'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('address', sa.Column('id', sa.Integer() , nullable=False , primary_key=True),
                               sa.Column('address1', sa.String(), nullable=False),
                               sa.Column('address2', sa.String(), nullable=False),
                               sa.Column('city', sa.String(), nullable=False),
                               sa.Column('state', sa.String(), nullable=False),
                               sa.Column('country', sa.String(), nullable=False),
                               sa.Column('postal_code', sa.String(), nullable=False)
                    )


def downgrade():
    op.drop_table('address')
