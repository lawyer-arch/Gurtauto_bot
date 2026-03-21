from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '77ed6755760f'
down_revision = '41c9d4ad99b6'
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Меняем тип telegram_id на BigInteger
    op.alter_column(
        'users',
        'telegram_id',
        type_=sa.BigInteger(),
        postgresql_using='telegram_id::bigint'
    )

def downgrade() -> None:
    # Откат: возвращаем в Integer (осторожно — возможна потеря данных)
    op.alter_column(
        'users',
        'telegram_id',
        type_=sa.Integer(),
        postgresql_using='telegram_id::integer'
    )