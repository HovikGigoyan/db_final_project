from alembic import op
import sqlalchemy as sa

revision = 'unique_id_3'
down_revision = 'unique_id_2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_index('idx_festivals_name', 'festivals', ['name'])
    op.create_index('idx_rockbands_genre', 'rockbands', ['genre'])


def downgrade() -> None:
    op.drop_index('idx_festivals_name', table_name='festivals')
    op.drop_index('idx_rockbands_genre', table_name='rockbands')