from alembic import op
import sqlalchemy as sa

revision = 'unique_id_4'
down_revision = 'unique_id_3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('festivals', 'details', type_=sa.dialects.postgresql.JSONB)
    op.execute("CREATE INDEX idx_details_gin ON festivals USING gin (details jsonb_path_ops)")


def downgrade() -> None:
    op.execute("DROP INDEX IF EXISTS idx_details_gin")
    op.alter_column('festivals', 'details', type_=sa.JSON)