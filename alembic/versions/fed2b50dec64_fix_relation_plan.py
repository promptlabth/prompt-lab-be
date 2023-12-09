"""fix relation plan

Revision ID: fed2b50dec64
Revises: 1ca44a84be7d
Create Date: 2023-12-09 17:37:31.195197

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel # added


# revision identifiers, used by Alembic.
revision: str = 'fed2b50dec64'
down_revision: Union[str, None] = '1ca44a84be7d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
