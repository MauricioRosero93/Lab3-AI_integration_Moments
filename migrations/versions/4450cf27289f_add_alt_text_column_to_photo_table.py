"""Add alt_text column to Photo table

Revision ID: 4450cf27289f
Revises: 
Create Date: 2025-03-14 09:04:07.394949

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4450cf27289f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('photo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('alt_text', sa.String(length=500), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('photo', schema=None) as batch_op:
        batch_op.drop_column('alt_text')

    # ### end Alembic commands ###
