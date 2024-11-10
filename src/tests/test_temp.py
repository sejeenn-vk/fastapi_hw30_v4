import os
from dotenv import load_dotenv
import pytest
import pytest_asyncio
import asyncio
from httpx import AsyncClient
# from .conftest import async_client


dot_env = load_dotenv("../.test.env")


# @pytest.mark.asyncio(loop_scope="session")
# async def test_register(async_client: AsyncClient):
#     print("++++++++++++++++++++", dot_env)
#     print("====event_loop====", asyncio.get_event_loop())
#     response = await async_client.get("/")
#     assert response.status_code == 200


@pytest_asyncio.fixture(loop_scope="module")
async def current_loop():
    return asyncio.get_running_loop()


@pytest.mark.asyncio(loop_scope="module")
async def test_runs_in_module_loop(current_loop):
    assert current_loop is asyncio.get_running_loop()
