from fastapi import APIRouter,HTTPException
from fastapi.responses import JSONResponse
import json
import os
router = APIRouter()


@router.get("/")
async def get_score():

    data = json.load(open(os.path.join(os.getcwd(),"app","data","all_data.json")))
    
    return JSONResponse(status_code=200,content={"status":"success","message":data})