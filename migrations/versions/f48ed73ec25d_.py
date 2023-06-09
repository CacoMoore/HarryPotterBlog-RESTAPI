"""empty message

Revision ID: f48ed73ec25d
Revises: 
Create Date: 2023-05-02 10:28:57.077238

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f48ed73ec25d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('alternate_name', sa.String(length=50), nullable=True),
    sa.Column('house', sa.String(length=50), nullable=False),
    sa.Column('species', sa.String(length=50), nullable=True),
    sa.Column('date_of_birth', sa.String(length=50), nullable=True),
    sa.Column('ancestry', sa.String(length=50), nullable=True),
    sa.Column('wand', sa.String(length=200), nullable=True),
    sa.Column('patronus', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=20), nullable=False),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.Integer(), nullable=True),
    sa.Column('chacrater_name', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['chacrater_name'], ['character.id'], ),
    sa.ForeignKeyConstraint(['username'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorite')
    op.drop_table('user')
    op.drop_table('character')
    # ### end Alembic commands ###
