from fastapi import FastAPI
from app.routers import equifax,experian,cibil,crif_highmark,np
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Bureaus API for Credit Score")

# Define allowed origins
origins = [
    "http://localhost:8081",  # Your frontend URL
    "http://127.0.0.1:8081",  # In case you use IP address
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

app.include_router(experian.router, tags=["Experian"],prefix="/experian")
app.include_router(equifax.router, tags=["Equifax"],prefix="/equifax")
app.include_router(cibil.router, tags=["Cibil"],prefix="/cibil")
app.include_router(crif_highmark.router, tags=["Crif_highmark"],prefix="/crif_highmark")
app.include_router(np.router, tags=["NP"],prefix="/np")


@app.get("/")
async def root():
    return {"message": "Hello dashboard"}
