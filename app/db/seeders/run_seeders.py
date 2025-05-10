from .admin_seeders import seed_admin  
from .plan_seeders import seed_plans
from .persona_seeders import seed_personas
from .legal_pulse.conclusion_seeders import seed_conclusions
import asyncio


async def run_seeders():
    await seed_admin()
    await seed_plans()
    await seed_personas()
    # await seed_conclusions()

if __name__ == "__main__":
    asyncio.run(run_seeders())