"""Added dummy model

Revision ID: f9c5d2dba936
Revises:
Create Date: 2020-10-05 23:56:58.658606

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f9c5d2dba936'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dummydbmodel',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('surname', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_dummydbmodel_name'), 'dummydbmodel', ['name'], unique=True)
    op.create_index(op.f('ix_dummydbmodel_surname'), 'dummydbmodel', ['surname'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_dummydbmodel_name'), table_name='dummydbmodel')
    op.drop_index(op.f('ix_dummydbmodel_surname'), table_name='dummydbmodel')
    op.drop_table('dummydbmodel')
    # ### end Alembic commands ###