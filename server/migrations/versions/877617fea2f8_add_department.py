"""add Department

Revision ID: 877617fea2f8
Revises: c0bc39646050
Create Date: 2024-02-21 16:26:21.844090

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '877617fea2f8'
down_revision = 'c0bc39646050'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###
