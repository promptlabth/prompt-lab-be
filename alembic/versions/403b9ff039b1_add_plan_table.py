"""Add plan table

Revision ID: 403b9ff039b1
Revises: fed2b50dec64
Create Date: 2023-12-09 17:58:36.616083

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel # added
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '403b9ff039b1'
down_revision: Union[str, None] = 'fed2b50dec64'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('payments')
    op.alter_column('coins', 'id',
               existing_type=sa.BIGINT(),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('coins', 'total',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('coins', 'user_id',
               existing_type=sa.BIGINT(),
               type_=sa.Integer(),
               existing_nullable=True)
    op.alter_column('features', 'name',
               existing_type=sa.TEXT(),
               type_=sqlmodel.sql.sqltypes.AutoString(),
               nullable=False)
    op.alter_column('features', 'date_of_create',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               type_=sa.Date(),
               nullable=False)
    op.alter_column('features', 'url',
               existing_type=sa.TEXT(),
               type_=sqlmodel.sql.sqltypes.AutoString(),
               nullable=False)
    op.drop_index('idx_features_deleted_at', table_name='features')
    op.drop_column('features', 'deleted_at')
    op.drop_column('features', 'created_at')
    op.drop_column('features', 'updated_at')
    op.add_column('users', sa.Column('plan_id', sa.Integer(), nullable=True))
    op.alter_column('users', 'firebase_id',
               existing_type=sa.TEXT(),
               type_=sqlmodel.sql.sqltypes.AutoString(),
               existing_nullable=True)
    op.alter_column('users', 'name',
               existing_type=sa.TEXT(),
               type_=sqlmodel.sql.sqltypes.AutoString(),
               existing_nullable=True)
    op.alter_column('users', 'email',
               existing_type=sa.TEXT(),
               type_=sqlmodel.sql.sqltypes.AutoString(),
               existing_nullable=True)
    op.alter_column('users', 'profilepic',
               existing_type=sa.TEXT(),
               type_=sqlmodel.sql.sqltypes.AutoString(),
               existing_nullable=True)
    op.alter_column('users', 'platform',
               existing_type=sa.TEXT(),
               type_=sqlmodel.sql.sqltypes.AutoString(),
               existing_nullable=True)
    op.alter_column('users', 'access_token',
               existing_type=sa.TEXT(),
               type_=sqlmodel.sql.sqltypes.AutoString(),
               existing_nullable=True)
    op.drop_index('idx_user_firebase_id', table_name='users')
    op.drop_index('idx_user_stripe_id', table_name='users')
    op.drop_index('idx_users_deleted_at', table_name='users')
    op.drop_constraint('idx_users_stripe_id', 'users', type_='unique')
    op.create_foreign_key(None, 'users', 'plans', ['plan_id'], ['id'])
    op.drop_column('users', 'profile_pic')
    op.drop_column('users', 'updated_at')
    op.drop_column('users', 'stripe_id')
    op.drop_column('users', 'deleted_at')
    op.drop_column('users', 'created_at')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('deleted_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('stripe_id', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('profile_pic', sa.TEXT(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.create_unique_constraint('idx_users_stripe_id', 'users', ['stripe_id'])
    op.create_index('idx_users_deleted_at', 'users', ['deleted_at'], unique=False)
    op.create_index('idx_user_stripe_id', 'users', ['stripe_id'], unique=False)
    op.create_index('idx_user_firebase_id', 'users', ['firebase_id'], unique=False)
    op.alter_column('users', 'access_token',
               existing_type=sqlmodel.sql.sqltypes.AutoString(),
               type_=sa.TEXT(),
               existing_nullable=True)
    op.alter_column('users', 'platform',
               existing_type=sqlmodel.sql.sqltypes.AutoString(),
               type_=sa.TEXT(),
               existing_nullable=True)
    op.alter_column('users', 'profilepic',
               existing_type=sqlmodel.sql.sqltypes.AutoString(),
               type_=sa.TEXT(),
               existing_nullable=True)
    op.alter_column('users', 'email',
               existing_type=sqlmodel.sql.sqltypes.AutoString(),
               type_=sa.TEXT(),
               existing_nullable=True)
    op.alter_column('users', 'name',
               existing_type=sqlmodel.sql.sqltypes.AutoString(),
               type_=sa.TEXT(),
               existing_nullable=True)
    op.alter_column('users', 'firebase_id',
               existing_type=sqlmodel.sql.sqltypes.AutoString(),
               type_=sa.TEXT(),
               existing_nullable=True)
    op.drop_column('users', 'plan_id')
    op.add_column('features', sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True))
    op.add_column('features', sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True))
    op.add_column('features', sa.Column('deleted_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True))
    op.create_index('idx_features_deleted_at', 'features', ['deleted_at'], unique=False)
    op.alter_column('features', 'url',
               existing_type=sqlmodel.sql.sqltypes.AutoString(),
               type_=sa.TEXT(),
               nullable=True)
    op.alter_column('features', 'date_of_create',
               existing_type=sa.Date(),
               type_=postgresql.TIMESTAMP(timezone=True),
               nullable=True)
    op.alter_column('features', 'name',
               existing_type=sqlmodel.sql.sqltypes.AutoString(),
               type_=sa.TEXT(),
               nullable=True)
    op.alter_column('coins', 'user_id',
               existing_type=sa.Integer(),
               type_=sa.BIGINT(),
               existing_nullable=True)
    op.alter_column('coins', 'total',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('coins', 'id',
               existing_type=sa.Integer(),
               type_=sa.BIGINT(),
               existing_nullable=False,
               autoincrement=True)
    op.create_table('payments',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('coin', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('transaction_stripe_id', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('datetime', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('payment_method_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('feature_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['feature_id'], ['features.id'], name='fk_features_payment'),
    sa.ForeignKeyConstraint(['payment_method_id'], ['payment_methods.id'], name='fk_payment_methods_payments'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_users_payment'),
    sa.PrimaryKeyConstraint('id', name='payments_pkey')
    )
    # ### end Alembic commands ###
