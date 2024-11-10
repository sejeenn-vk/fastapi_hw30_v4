# from typing import Annotated
#
# import pytest_asyncio
# from fastapi import Depends
# from httpx import AsyncClient, ASGITransport
# from collections.abc import AsyncGenerator
#
# from sqlalchemy.ext.asyncio import AsyncSession
#
# from core.models import db_helper
# from main import main_app
#
#
# @pytest_asyncio.fixture(loop_scope='session', scope="session")
# async def async_client() -> AsyncGenerator[AsyncClient, None]:
#     async with AsyncClient(
#             transport=ASGITransport(app=main_app), base_url='http://test'
#     ) as async_test_client:
#         yield async_test_client
# #
# #
# # @pytest_asyncio.fixture(scope="session")
# # async def async_db(
# #         session: Annotated[
# #             AsyncSession,
# #             Depends(db_helper.session_getter),
# #         ],
# # ):
# #     yield session
