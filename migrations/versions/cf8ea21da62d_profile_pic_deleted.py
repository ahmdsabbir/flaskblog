"""Profile Pic deleted

Revision ID: cf8ea21da62d
Revises: 425c70691993
Create Date: 2022-11-29 15:28:31.328282

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cf8ea21da62d'
down_revision = '425c70691993'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('profile_pic')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('profile_pic', mysql.VARCHAR(length=500), nullable=True))

    # ### end Alembic commands ###