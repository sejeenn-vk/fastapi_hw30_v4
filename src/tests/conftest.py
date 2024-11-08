import os
import pytest
from main import main_app
from httpx import AsyncClient, ASGITransport


os.environ['ENV'] = 'testing'


@pytest.fixture
async def async_client():
    async with AsyncClient(
            transport=ASGITransport(app=main_app),
            base_url="http://localhost:8000"
    ) as async_client:
        yield async_client
