"""empty message

Revision ID: a75e5712bea1
Revises: 34f0bdbb3013
Create Date: 2017-08-27 14:32:13.066466

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a75e5712bea1'
down_revision = '34f0bdbb3013'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_file', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'user_file', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_file', type_='foreignkey')
    op.drop_column('user_file', 'user_id')
    # ### end Alembic commands ###
