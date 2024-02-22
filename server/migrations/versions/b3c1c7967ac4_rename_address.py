"""rename address

Revision ID: b3c1c7967ac4
Revises: 025adea1fdce
Create Date: 2024-02-21 17:19:49.508120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3c1c7967ac4'
down_revision = '025adea1fdce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.add_column('departments', sa.Column('location', sa.String(), nullable=True))
    # op.drop_column('departments', 'address')
    op.alter_column('departments', 'address',  new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.add_column('departments', sa.Column('address', sa.VARCHAR(), nullable=True))
    # op.drop_column('departments', 'location')
    op.alter_column('departments', 'location',  new_column_name='address')
    # ### end Alembic commands ###
