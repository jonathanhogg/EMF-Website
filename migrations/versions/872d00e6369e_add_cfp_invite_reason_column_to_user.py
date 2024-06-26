"""add cfp_invite_reason column to user

Revision ID: 872d00e6369e
Revises: c594b354e0d3
Create Date: 2024-02-03 21:57:10.273521

"""

# revision identifiers, used by Alembic.
revision = '872d00e6369e'
down_revision = 'c594b354e0d3'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('cfp_invite_reason', sa.String(), nullable=True))
    op.add_column('user_version', sa.Column('cfp_invite_reason', sa.String(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_version', 'cfp_invite_reason')
    op.drop_column('user', 'cfp_invite_reason')
    # ### end Alembic commands ###
