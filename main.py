from fastapi import FastAPI

from routers import auth_router, test_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(test_router)
