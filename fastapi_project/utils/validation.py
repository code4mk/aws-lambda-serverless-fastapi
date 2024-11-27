from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi import FastAPI
from pydantic import BaseModel, ValidationError
from functools import wraps
from fastapi_project.utils.base import the_query

# Add the ValidationException class
class ValidationException(Exception):
    def __init__(self, errors: dict):
        self.errors = errors

# Add the setup_validation_exception_handler function
def setup_validation_exception_handler(app: FastAPI):
    @app.exception_handler(ValidationException)
    async def validation_exception_handler(request: Request, exc: ValidationException):
        return JSONResponse(
            status_code=422,
            content=exc.errors
        )

# Add the dto decorator
def dto(schema: BaseModel):
    def decorator(func):
        @wraps(func)
        async def wrapper(request: Request, *args, **kwargs):
            try:
                request_data = await the_query(request)
                validated_data = schema(**request_data)
                return await func(validated_data, *args, **kwargs)
            except ValidationError as e:
                errors = {}
                for error in e.errors():
                    field = error['loc'][0]
                    message = field + " " + error['msg']
                    if field not in errors:
                        errors[field] = []
                    errors[field].append(message)
                    
                raise ValidationException({
                    'success': False,
                    'errors': errors
                })
            except ValueError:
                raise HTTPException(status_code=400, detail="Invalid JSON")
            
        return wrapper
    return decorator

# Update the __all__ list
__all__ = ['dto', 'ValidationException', 'setup_validation_exception_handler']
