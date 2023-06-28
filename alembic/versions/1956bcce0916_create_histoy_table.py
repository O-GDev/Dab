"""create-histoy-table

Revision ID: 1956bcce0916
Revises: 69be33196a71
Create Date: 2023-06-28 19:12:01.189591

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1956bcce0916'
down_revision = '69be33196a71'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('history',
                    sa.Column('id', sa.Integer(), nullable=False, ),
                    sa.Column('preg', sa.String(), nullable=False),
                    sa.Column('glu', sa.String(), nullable=False),
                    sa.Column('bp', sa.String(), nullable=False),
                    sa.Column('age', sa.String(), nullable=False),
                    sa.Column('skin', sa.String(), nullable=False),
                    sa.Column('insulin', sa.String(), nullable=False),
                    sa.Column('bmi', sa.String(), nullable=False),
                    sa.Column('dpf', sa.String(), nullable=False),
                    sa.Column('result', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=True, server_default=sa.text('now()')),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    pass


def downgrade() -> None:
    op.drop_table('history')
    pass
