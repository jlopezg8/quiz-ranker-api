from fastapi import FastAPI
from fastapi.routing import APIRoute

from routers import auth_router, test_router


# https://fastapi.tiangolo.com/advanced/generate-clients/?h=sdk#client-method-names
def custom_generate_unique_id(route: APIRoute):
    return route.name


app = FastAPI(generate_unique_id_function=custom_generate_unique_id)
app.include_router(auth_router)
app.include_router(test_router)
