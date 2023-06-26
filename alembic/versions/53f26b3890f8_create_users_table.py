"""create users table

Revision ID: 53f26b3890f8
Revises: 
Create Date: 2023-06-16 22:14:49.362709

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53f26b3890f8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False, ),
                    sa.Column('first_name', sa.String(), nullable=False),
                    sa.Column('last_name', sa.String(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('token', sa.String()),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('occupation', sa.String(), ),
                    sa.Column('house_address', sa.String(), ),
                    sa.Column('phone_number', sa.String(), ),
                    sa.Column('profile_pics', sa.String(), ),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=True, server_default=sa.text('now()')),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table("users")    
    pass
