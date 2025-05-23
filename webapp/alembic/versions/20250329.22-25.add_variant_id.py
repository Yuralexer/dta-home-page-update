"""add_variant_id

Revision ID: fe6046af9ed9
Revises: 97b339c4e159
Create Date: 2025-03-29 22:25:39.951652

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe6046af9ed9'
down_revision = '97b339c4e159'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('students') as bop:
        bop.add_column(sa.Column('variant', sa.Integer, nullable=True))
        bop.create_foreign_key('fk_students_variant', 'variants', ['variant'], ['id'])


def downgrade():
    with op.batch_alter_table("students") as bop:
        bop.drop_constraint("fk_students_variant", type_="foreignkey")
        bop.drop_column("variant")
