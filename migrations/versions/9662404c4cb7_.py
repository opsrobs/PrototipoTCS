"""empty message

Revision ID: 9662404c4cb7
Revises: 
Create Date: 2023-04-30 15:06:36.753138

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9662404c4cb7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gpt_has_smell',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_gpt', sa.Integer(), nullable=True),
    sa.Column('id_smell', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('historias',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('historia_input', sa.String(length=256), nullable=True),
    sa.Column('historia_output', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('smells',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=80), nullable=True),
    sa.Column('detalhe', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('smells')
    op.drop_table('historias')
    op.drop_table('gpt_has_smell')
    # ### end Alembic commands ###
