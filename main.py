from os import getenv
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
import uvicorn

import config, routes


origins = [
    "https://tambangla.com",
    "http://localhost",
    "http://localhost:3000",
]

def application_details() -> FastAPI:
    application = FastAPI(
        title=config.API_NAME,
        description=config.API_DESCRIPTION,
        version=config.API_VERSION,
    )
    application.include_router(routes.router, prefix=config.API_ROUTE_PREFIX)
    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return application



app = application_details()


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

if __name__ == "__main__":
    port = int(getenv("PORT", 8000))
    uvicorn.run("app.api:app", host="0.0.0.0", port=port, reload=True)