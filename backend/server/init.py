from fastapi import FastAPI
from database.settings import database, check_connection
import yaml
from fastapi.middleware.cors import CORSMiddleware


async def create_app() -> FastAPI:
    app = FastAPI(docs_url="/")

    origins = [
        "http://localhost:5002",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    try:
        await check_connection()

        if "datathon" not in await database.list_collection_names():
            print("Collection 'datathon' does not exist. Creating...")
            print("Collection 'datathon' created.")
        else:
            print("Collection 'datathon' already exists.")

    except Exception as e:
        print(f"Error initializing MongoDB: {e}")

    register_views(app=app)

    def custom_openapi():
        if app.openapi_schema:
            return app.openapi_schema
        
        # with open("server/api.yaml", encoding="utf-8") as f:
        #     openapi_schema = yaml.safe_load(f)
        #     app.openapi_schema = openapi_schema
        #     return app.openapi_schema
        

    app.openapi = custom_openapi


    return app


def register_views(app: FastAPI):
    from app.controllers.blockchain_controller import api_router
    app.include_router(api_router)