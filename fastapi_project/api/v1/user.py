from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi_project.utils.base import the_query
from fastapi_project.services.user_service import UserService
from fastapi_project.schemas.user_schema import UserCreateSchema
from fastapi_project.utils.validation import dto
router = APIRouter()

user_service = UserService()

@router.post("/users/create")
@dto(UserCreateSchema)
async def create_order(request: Request):
    # Retrieve data from the request
    request_data = await the_query(request)
    data = UserCreateSchema(**request_data)
    
    # validated_data = request.state.validated_data
    # output = user_service.s_create_user(request, validated_data)
    
    output = user_service.s_create_user(request, data)
    return JSONResponse(content=output, status_code=status.HTTP_200_OK)

@router.get("/users")
async def get_users(request: Request):
    data = user_service.s_get_users(request)
    return JSONResponse(content=jsonable_encoder(data), status_code=status.HTTP_200_OK)

@router.get("/users/{id}")
async def get_user(request: Request, id: int):
    data = user_service.s_get_user_by_id(user_id=id)
    return JSONResponse(content=jsonable_encoder(data), status_code=status.HTTP_200_OK)
