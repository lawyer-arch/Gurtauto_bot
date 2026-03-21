from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert
from typing import Dict, Any

from database.models.lead import Lead


class LeadRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: Dict[str, Any]) -> Lead:
        stmt = insert(Lead).values(**data).returning(Lead)
        result = await self.session.execute(stmt)
        await self.session.commit()

        return result.scalar_one()