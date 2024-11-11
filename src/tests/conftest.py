from collections.abc import AsyncGenerator

import pytest_asyncio

from fastapi.testclient import TestClient
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.pool import NullPool
from main import main_app
from core.models.base import Base
from core.models.ingredient import Ingredient
from core.models.db_helper import db_helper


DATABASE_URL_TEST = "postgresql+asyncpg://test:test@localhost:5432/test"
engine_test = create_async_engine(DATABASE_URL_TEST, poolclass=NullPool, echo=True)
async_session = async_sessionmaker(bind=engine_test, expire_on_commit=False)


async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session

main_app.dependency_overrides[db_helper.session_getter] = override_get_async_session
client = TestClient(main_app)

ingredients = [
    Ingredient(
        ingredient_name="Мука пшеничная", ingredient_description="высший сорт"
    ),
    Ingredient(ingredient_name="Соль"),
    Ingredient(ingredient_name="Сахар"),
    Ingredient(
        ingredient_name="Яйцо куриное", ingredient_description="0 категории"
    ),
    Ingredient(ingredient_name="Молоко"),
]


@pytest_asyncio.fixture(autouse=True, scope='session')
async def prepare_database():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # async with engine_test.begin() as conn:
    #     await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture(scope='session')
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(
            transport=ASGITransport(app=main_app), base_url='http://test'
    ) as async_test_client:
        yield async_test_client
