"""Profile Pic added

Revision ID: 425c70691993
Revises: 719b341ee00f
Create Date: 2022-11-29 14:45:26.328682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '425c70691993'
down_revision = '719b341ee00f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('profile_pic', sa.String(500), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('profile_pic')

    # ### end Alembic commands ###
