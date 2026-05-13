from app.routes.history import router as history_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import Base, engine
from app.routes import user, calculation   # ✅ math removed

app = FastAPI()

# ✅ CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Create tables
Base.metadata.create_all(bind=engine)

# ✅ Routers
app.include_router(user.router)
app.include_router(calculation.router)
app.include_router(history_router)

# ✅ Root
@app.get("/")
def root():
    return {"message": "THIS IS MY APP"}