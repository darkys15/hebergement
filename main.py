from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/") 
async def Bienvenu():
    try:
        return{"message" :" Bienvenu au cours de RCW groupe 1002"}
    except Exception as e :
        raise HTTPException(status_code=500,detail=str(e))

@app.get("/test")
async def Bonjour():
    try:
        return{"message" :"TEST DU SERVEUR COURS RCW REUSSI"}
    except Exception as e :
        HTTPException(status_code=500,detail=str(e))


    
