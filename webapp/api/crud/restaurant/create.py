from fastapi import Depends, HTTPException
from fastapi.responses import ORJSONResponse
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from webapp.api.crud.restaurant.router import restaurant_router
from webapp.crud.restaurant import restaurant_crud
from webapp.db.postgres import get_session
from webapp.schema.info.restaurant import RestaurantInfo
from webapp.utils.auth.jwt import JwtTokenT, jwt_auth


@restaurant_router.post('/create')
async def create_restaurant(
    body: RestaurantInfo,
    session: AsyncSession = Depends(get_session),
    access_token: JwtTokenT = Depends(jwt_auth.validate_token),
) -> ORJSONResponse:
    try:
        await restaurant_crud.create(session, body)
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)

    return ORJSONResponse(content={'message': 'Restaurant created successfully'}, status_code=status.HTTP_201_CREATED)