"""empty message

Revision ID: 2244025d3925
Revises: 94fe231fb1ca
Create Date: 2025-06-07 19:09:44.774899

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2244025d3925'
down_revision = '94fe231fb1ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('urodzenia_woj',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('wojewodztwa', sa.String(), nullable=True),
    sa.Column('rok', sa.Integer(), nullable=True),
    sa.Column('liczba_ogolem', sa.Integer(), nullable=True),
    sa.Column('chlopcy', sa.Integer(), nullable=True),
    sa.Column('dzieczeta', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_urodzenia_woj_id'), 'urodzenia_woj', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_urodzenia_woj_id'), table_name='urodzenia_woj')
    op.drop_table('urodzenia_woj')
    # ### end Alembic commands ###
