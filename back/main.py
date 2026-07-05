from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .app.db.connection import engine, Base
from .app.routes import sections, projects, contacts, skills, social_links

# Créer les tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Portfolio API",
    description="API pour gérer un portfolio modifiable",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusion des routes
app.include_router(sections.router)
app.include_router(projects.router)
app.include_router(contacts.router)
app.include_router(skills.router)
app.include_router(social_links.router)

@app.get("/")
def root():
    return {
        "message": "Portfolio API",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc"
    }

@app.get("/api/health")
def health_check():
    return {"status": "healthy"}