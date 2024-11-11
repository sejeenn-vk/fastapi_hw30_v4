import pytest
from httpx import AsyncClient
from .conftest import ac


@pytest.mark.asyncio
async def test_register(ac: AsyncClient):
    response = await ac.get("/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_register(ac: AsyncClient):
    response = await ac.post("/ingredients", json={
        "ingredient_name": "name for test",
        "ingredient_description": "description for test"
    })
    assert response.json()['ingredient_name'] == 'name for test'
    assert response.json()['ingredient_description'] == 'description for test'
