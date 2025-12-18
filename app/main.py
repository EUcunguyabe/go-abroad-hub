from __future__ import annotations

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.controllers import router
from app.exceptions import BadRequestError, NotFoundError

app = FastAPI(title="Go Abroad Hub", version="1.0.0")
app.include_router(router)


@app.exception_handler(NotFoundError)
def not_found_handler(_: Request, exc: NotFoundError):
    return JSONResponse(status_code=404, content={"error": str(exc)})


@app.exception_handler(BadRequestError)
def bad_request_handler(_: Request, exc: BadRequestError):
    return JSONResponse(status_code=400, content={"error": str(exc)})
