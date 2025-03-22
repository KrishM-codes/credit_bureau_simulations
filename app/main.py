from fastapi import FastAPI
from app.routers import equifax,experian,cibil,crif_highmark
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Weride Dashboard")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

app.include_router(experian.router, tags=["Experian"],prefix="/experian")
app.include_router(equifax.router, tags=["Equifax"],prefix="/equifax")
app.include_router(cibil.router, tags=["Cibil"],prefix="/cibil")
app.include_router(crif_highmark.router, tags=["Crif_highmark"],prefix="/crif_highmark")


@app.get("/")
async def root():
    return {"message": "Hello dashboard"}
