"""Foreign key to post/users

Revision ID: 14779fa86750
Revises: ff15ced15dfe
Create Date: 2022-11-17 10:28:08.069965

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14779fa86750'
down_revision = 'ff15ced15dfe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('poster_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'users', ['poster_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('poster_id')

    # ### end Alembic commands ###
