"""empty message

Revision ID: 43d10d77ec74
Revises: c6565a91be18
Create Date: 2022-10-02 02:26:03.949871

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43d10d77ec74'
down_revision = 'c6565a91be18'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('items', 'price',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=False)
    op.alter_column('users', 'password',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.String(length=255),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'password',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('items', 'price',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=False)
    # ### end Alembic commands ###
