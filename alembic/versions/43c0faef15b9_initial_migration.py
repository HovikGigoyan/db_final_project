"""Initial migration

Revision ID: 43c0faef15b9
Revises: 
Create Date: 2025-01-07 03:03:46.269184

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '43c0faef15b9'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rockbands')
    op.drop_table('festivals')
    op.drop_table('performances')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('performances',
    sa.Column('performanceid', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('festivalid', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('bandid', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('performancetype', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('number', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('duration', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['bandid'], ['rockbands.bandid'], name='performances_bandid_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['festivalid'], ['festivals.festivalid'], name='performances_festivalid_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('performanceid', name='performances_pkey')
    )
    op.create_table('festivals',
    sa.Column('festivalid', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('location', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('date', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('organizer', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('format', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('festivalid', name='festivals_pkey')
    )
    op.create_table('rockbands',
    sa.Column('bandid', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('yearfounded', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('genre', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('producer', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('members', sa.VARCHAR(length=250), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('bandid', name='rockbands_pkey')
    )
    # ### end Alembic commands ###
