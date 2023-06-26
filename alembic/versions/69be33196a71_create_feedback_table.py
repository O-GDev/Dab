"""create feedback table

Revision ID: 69be33196a71
Revises: 53f26b3890f8
Create Date: 2023-06-16 22:15:49.671907

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69be33196a71'
down_revision = '53f26b3890f8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('feedback',
                    sa.Column('id', sa.Integer(), nullable=False, ),
                    sa.Column('message1', sa.String(), nullable=False),
                    sa.Column('message2', sa.String(), nullable=False),
                    sa.Column('message3', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=True, server_default=sa.text('now()')),
                    )
    pass


def downgrade() -> None:
    op.drop_table('feedback')
    pass
