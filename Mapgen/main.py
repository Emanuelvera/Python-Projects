
from fastapi import FastAPI, Depends, Body, HTTPException, Path, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from jwt_manager import create_token, validate_token
from fastapi.security import HTTPBearer
from config.database import Session, engine, Base
from models.movie import Movie as MovieModel



app = FastAPI()
app.title = "Generador de Graficos"
app.version = "0.0.1"



@app.get("/", tags=["home"])
def message():
    return HTMLResponse("<h1>Generador de Graficos</h1>")
