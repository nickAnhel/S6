import typing as tp
import typing_extensions as te

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from config import settings


async_engine = create_async_engine(
    url=settings.db_url,
    echo=settings.echo,
)

async_session_maker = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


async def execute(query: te.LiteralString, **params: tp.Any):
    async with async_session_maker() as session:
        res = await session.execute(text(query), params)
        await session.commit()
        return res
