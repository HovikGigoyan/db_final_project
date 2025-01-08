from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = 'unique_id_2'
down_revision: Union[str, None] = 'unique_id_1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('festivals', sa.Column('details', sa.JSON(), nullable=True))


def downgrade() -> None:
    op.drop_column('festivals', 'details')