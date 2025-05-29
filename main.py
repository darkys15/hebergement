from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/") 
async def Bienvenu():
    try:
        return{"message" :" Bonjourr RCW 1002"}
    except Exception as e :
        raise HTTPException(status_code=500,detail=str(e))

@app.get("/test")
async def Bonjour():
    try:
        return{"message" :"SERVEUR COURS RCW"}
    except Exception as e :
        HTTPException(status_code=500,detail=str(e))


    