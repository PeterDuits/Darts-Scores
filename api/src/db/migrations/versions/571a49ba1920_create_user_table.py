"""create_user_table

Revision ID: 571a49ba1920
Revises: 
Create Date: 2019-03-06 14:36:26.666487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '571a49ba1920'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.CHAR(length=36), nullable=True),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_user_created_at'), 'user', ['created_at'], unique=False)
    op.create_index(op.f('ix_user_updated_at'), 'user', ['updated_at'], unique=False)
    op.create_index(op.f('ix_user_user_id'), 'user', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_updated_at'), table_name='user')
    op.drop_index(op.f('ix_user_created_at'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
