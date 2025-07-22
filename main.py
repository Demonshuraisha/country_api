from fastapi import FastAPI
from routes.country import router as country_router
from routes.extra import router as extra_router

app = FastAPI()

# Inclusion des routes
app.include_router(country_router)
app.include_router(extra_router)




