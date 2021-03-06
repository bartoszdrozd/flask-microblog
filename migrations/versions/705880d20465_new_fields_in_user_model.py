"""new fields in user model

Revision ID: 705880d20465
Revises: b9b75281a4e1
Create Date: 2021-05-31 12:25:57.032717

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '705880d20465'
down_revision = 'b9b75281a4e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
