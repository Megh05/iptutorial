"""tables

Revision ID: f2f28b21fac7
Revises: b7849616cfe1
Create Date: 2021-06-21 16:30:15.715944

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2f28b21fac7'
down_revision = 'b7849616cfe1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users2',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=50), nullable=True),
    sa.Column('surname', sa.String(length=50), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('address', sa.String(length=100), nullable=True),
    sa.Column('town', sa.String(length=100), nullable=True),
    sa.Column('city', sa.String(length=100), nullable=True),
    sa.Column('postcode', sa.String(length=7), nullable=True),
    sa.Column('phone', sa.String(length=11), nullable=True),
    sa.Column('workexperience', sa.String(length=100), nullable=True),
    sa.Column('type', sa.String(length=20), nullable=True),
    sa.Column('confirmed', sa.Boolean(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users2_email'), 'users2', ['email'], unique=True)
    op.create_index(op.f('ix_users2_username'), 'users2', ['username'], unique=True)
    op.create_table('content2',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=300), nullable=True),
    sa.Column('file', sa.LargeBinary(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users2.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('courses2',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('chapters', sa.String(length=200), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users2.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('projects2',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('chapters', sa.String(length=200), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users2.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sessions2',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sessionname', sa.String(length=100), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('time', sa.Time(), nullable=True),
    sa.Column('duration', sa.String(length=100), nullable=True),
    sa.Column('coursename', sa.String(length=200), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users2.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('supporttickets3',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ticketname', sa.String(length=100), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('message', sa.String(length=1000), nullable=True),
    sa.Column('sendername', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.String(length=11), nullable=True),
    sa.Column('response', sa.String(length=1000), nullable=True),
    sa.Column('progress', sa.String(length=50), nullable=True),
    sa.Column('assignedto', sa.String(length=100), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users2.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('supporttickets2')
    op.drop_table('projects')
    op.drop_table('sessions')
    op.drop_table('content')
    op.drop_table('courses')
    op.drop_index('ix_users_email', table_name='users')
    op.drop_index('ix_users_username', table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('firstname', sa.VARCHAR(length=50), nullable=True),
    sa.Column('surname', sa.VARCHAR(length=50), nullable=True),
    sa.Column('username', sa.VARCHAR(length=64), nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), nullable=True),
    sa.Column('password_hash', sa.VARCHAR(length=128), nullable=True),
    sa.Column('address', sa.VARCHAR(length=100), nullable=True),
    sa.Column('town', sa.VARCHAR(length=100), nullable=True),
    sa.Column('city', sa.VARCHAR(length=100), nullable=True),
    sa.Column('postcode', sa.VARCHAR(length=7), nullable=True),
    sa.Column('phone', sa.VARCHAR(length=11), nullable=True),
    sa.Column('workexperience', sa.VARCHAR(length=100), nullable=True),
    sa.Column('type', sa.VARCHAR(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_users_username', 'users', ['username'], unique=False)
    op.create_index('ix_users_email', 'users', ['email'], unique=False)
    op.create_table('courses',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=True),
    sa.Column('description', sa.VARCHAR(length=200), nullable=True),
    sa.Column('chapters', sa.VARCHAR(length=200), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('content',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=300), nullable=True),
    sa.Column('file', sa.BLOB(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sessions',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('sessionname', sa.VARCHAR(length=100), nullable=True),
    sa.Column('date', sa.DATE(), nullable=True),
    sa.Column('time', sa.TIME(), nullable=True),
    sa.Column('duration', sa.VARCHAR(length=100), nullable=True),
    sa.Column('coursename', sa.VARCHAR(length=200), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('projects',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=True),
    sa.Column('description', sa.VARCHAR(length=200), nullable=True),
    sa.Column('chapters', sa.VARCHAR(length=200), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('supporttickets2',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('ticketname', sa.VARCHAR(length=100), nullable=True),
    sa.Column('date', sa.DATE(), nullable=True),
    sa.Column('message', sa.VARCHAR(length=1000), nullable=True),
    sa.Column('sendername', sa.VARCHAR(length=100), nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), nullable=True),
    sa.Column('phone', sa.VARCHAR(length=11), nullable=True),
    sa.Column('response', sa.VARCHAR(length=1000), nullable=True),
    sa.Column('progress', sa.VARCHAR(length=50), nullable=True),
    sa.Column('assignedto', sa.VARCHAR(length=100), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('supporttickets3')
    op.drop_table('sessions2')
    op.drop_table('projects2')
    op.drop_table('courses2')
    op.drop_table('content2')
    op.drop_index(op.f('ix_users2_username'), table_name='users2')
    op.drop_index(op.f('ix_users2_email'), table_name='users2')
    op.drop_table('users2')
    # ### end Alembic commands ###