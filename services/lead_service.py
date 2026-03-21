from database.repository.lead_repo import LeadRepository


class LeadService:

    def __init__(self, repo: LeadRepository):
        self.repo = repo

    async def create_lead(self, data):
        return await self.repo.create(data)