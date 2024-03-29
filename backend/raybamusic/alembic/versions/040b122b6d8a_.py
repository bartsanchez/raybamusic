"""empty message

Revision ID: 040b122b6d8a
Revises: 
Create Date: 2021-06-24 11:09:18.847643

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '040b122b6d8a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('songs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('release', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_songs_id'), 'songs', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_songs_id'), table_name='songs')
    op.drop_table('songs')
    # ### end Alembic commands ###
