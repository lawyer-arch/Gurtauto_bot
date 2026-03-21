from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models.user import User


class UserRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_or_create(self, telegram_id, username, full_name):

        result = await self.session.execute(
            select(User).where(User.telegram_id == telegram_id)
        )
        user = result.scalar_one_or_none()

        if user:
            return user

        user = User(
            telegram_id=telegram_id,
            username=username,
            full_name=full_name
        )

        self.session.add(user)
        await self.session.commit()

        return user