from fastapi import APIRouter,HTTPException
from fastapi.responses import JSONResponse
import json
import os
router = APIRouter()


@router.get("/")
async def get_score(pan_id:str = ""):

    data = json.load(open(os.path.join(os.getcwd(),"app","data","data.json")))
    if pan_id == "":
        return JSONResponse(status_code=400,content={"status":"bad_request","message":"PAN NUMBER WAS NOT RECIEVED"})
    elif pan_id not in data["cibil"].keys():
        return JSONResponse(status_code=404,content={"status":"not_found","message":"PAN NUMBER NOT REGISTERED"})
    return JSONResponse(status_code=200,content={"status":"success","message":data["cibil"][pan_id]})