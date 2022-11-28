"""added about author in db

Revision ID: 719b341ee00f
Revises: 14779fa86750
Create Date: 2022-11-21 15:25:05.480361

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '719b341ee00f'
down_revision = '14779fa86750'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_author', sa.String(length=220), nullable=True))
        batch_op.alter_column('favorite_color',
               existing_type=mysql.VARCHAR(length=120),
               type_=sa.Text(length=120),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('favorite_color',
               existing_type=sa.Text(length=120),
               type_=mysql.VARCHAR(length=120),
               existing_nullable=True)
        batch_op.drop_column('about_author')

    # ### end Alembic commands ###
