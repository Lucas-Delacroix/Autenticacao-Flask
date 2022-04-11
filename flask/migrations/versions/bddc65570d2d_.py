"""empty message

Revision ID: bddc65570d2d
Revises: 4116ea0ad2bc
Create Date: 2022-04-11 01:44:15.583313

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bddc65570d2d'
down_revision = '4116ea0ad2bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('role_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'user', 'role', ['role_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_column('user', 'role_id')
    # ### end Alembic commands ###
