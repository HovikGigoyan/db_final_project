from alembic import op
import sqlalchemy as sa

revision = 'unique_id_1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('festivals', sa.Column('description', sa.String(length=255), nullable=True))
    op.add_column('rockbands', sa.Column('awards', sa.String(length=255), nullable=True))


def downgrade() -> None:
    op.drop_column('festivals', 'description')
    op.drop_column('rockbands', 'awards')