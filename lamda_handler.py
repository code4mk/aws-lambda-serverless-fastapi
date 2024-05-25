from mangum import Mangum
from fastapi_project.main import app

handler = Mangum(app)


