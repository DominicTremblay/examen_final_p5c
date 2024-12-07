"""empty message

Revision ID: 4350ddcff5e3
Revises: 25e91fecefdb
Create Date: 2024-11-27 15:43:30.821905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4350ddcff5e3'
down_revision = '25e91fecefdb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('utilisateur', schema=None) as batch_op:
        batch_op.add_column(sa.Column('avatar_url', sa.String(length=200), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('utilisateur', schema=None) as batch_op:
        batch_op.drop_column('avatar_url')

    # ### end Alembic commands ###
