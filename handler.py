from mangum import Mangum
from fastapi_project.main import app as fastapi_app

handler = Mangum(fastapi_app)
