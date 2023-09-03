import os

from sqlalchemy.orm import sessionmaker
from sqlmodel import create_engine
from sqlmodel.ext.asyncio.session import AsyncSession, AsyncEngine

engine = AsyncEngine(create_engine(os.environ.get('DB_URL'), echo=True, future=True))


async def get_session() -> AsyncSession:
    async with sessionmaker(engine, class_=AsyncSession, expire_on_commit=False) as session:
        yield session
