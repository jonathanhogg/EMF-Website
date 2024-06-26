"""Add wise_id

Revision ID: cb664b092ad5
Revises: 619c2e9fe0e7
Create Date: 2022-01-15 22:35:43.056350

"""

# revision identifiers, used by Alembic.
revision = 'cb664b092ad5'
down_revision = '619c2e9fe0e7'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bank_transaction', sa.Column('wise_id', sa.String(), nullable=True))
    op.create_index(op.f('ix_bank_transaction_wise_id'), 'bank_transaction', ['wise_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_bank_transaction_wise_id'), table_name='bank_transaction')
    op.drop_column('bank_transaction', 'wise_id')
    # ### end Alembic commands ###
