from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from starlette.responses import RedirectResponse

from app.routes import links
from database.database import setup_db
from fastapi.openapi.models import Info
from fastapi.openapi.utils import get_openapi

app = FastAPI(
    title="domain-checker"
)


app.include_router(links.router)

setup_db(app)

#Добавляем информацию для Swagger UI
app.openapi = Info(
    title="domain-checker",
    version="1.0.0",
    description="Wеb-сервис для учета посещенных ресурсов",
    terms_of_service="https://t.me/evgenysoloz",
    contact={
        "name": "Евгений Солозобов",
        "url": "https://t.me/evgenysoloz",
    },
)

# Генерация JSON-документа OpenAPI (Swagger)
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="domain-checker",
        version="1.0.0",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

# Добавляем Swagger UI
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="Swagger UI")

@app.get("/openapi.json", include_in_schema=False)
async def custom_openapi_json():
    return app.openapi_schema

# Добавляем редирект с корня на Swagger UI
@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")