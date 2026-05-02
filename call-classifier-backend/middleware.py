from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def add_middleware(app: FastAPI) -> None:
    """
    Register all middleware on the FastAPI app instance.
    Call this function once in main.py before the app starts.
    """

    # CORSMiddleware handles the preflight OPTIONS requests and adds the right
    # response headers so the browser allows the cross-origin call.
    app.add_middleware(
        CORSMiddleware,
        # allow_origins: which frontend URLs are allowed to call this API.
        # "*" means anyone — fine for development, but in production you should
        # list only your real frontend URL, e.g. ["https://yourapp.com"]
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
