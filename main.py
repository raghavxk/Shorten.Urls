from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from urlApp import routes as url_routes
from redirectApp import routes as redirect_routes

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(url_routes.router)
app.include_router(redirect_routes.router)
