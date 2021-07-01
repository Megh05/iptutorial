"""Adding conetent table

Revision ID: 9802f18c14af
Revises: 50b4ce1e4826
Create Date: 2021-06-17 16:56:40.388722

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9802f18c14af'
down_revision = '50b4ce1e4826'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('content',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=300), nullable=True),
    sa.Column('file', sa.LargeBinary(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('content')
    # ### end Alembic commands ###