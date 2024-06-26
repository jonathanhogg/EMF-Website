"""Create capacity on Venue

Revision ID: c594b354e0d3
Revises: 8dd432ba3ede
Create Date: 2024-01-30 02:46:27.381445

"""

# revision identifiers, used by Alembic.
revision = 'c594b354e0d3'
down_revision = '8dd432ba3ede'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venue', sa.Column('capacity', sa.Integer(), nullable=True))
    
    conn = op.get_bind()
    meta = sa.MetaData(bind=conn)
    meta.reflect(only=('venue',))
    venue_tbl = sa.Table('venue', meta)

    for venue_name, capacity in [
        ('Stage A', 1000),
        ('Stage B', 600),
        ('Stage C', 450),
        ('Workshop 1', 30),
        ('Workshop 2', 30),
        ('Workshop 3', 30),
        ('Workshop 4', 30),
        ('Workshop 5', 30),
        ('Youth Workshop', 30),
    ]:
        op.execute(sa.update(venue_tbl).where(venue_tbl.c.name == venue_name).values(capacity=capacity))


    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venue', 'capacity')
    # ### end Alembic commands ###
