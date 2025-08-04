from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import sqlite3
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_NAME = "plats.db"

class Plat(BaseModel):
    nom: str
    prix: float
    disponible: bool

def query_db(query, params=(), fetch=False):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(query, params)
    data = cursor.fetchall() if fetch else None
    conn.commit()
    conn.close()
    return data

@app.on_event("startup")
def startup():
    query_db("""
        CREATE TABLE IF NOT EXISTS plats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            prix REAL NOT NULL,
            disponible BOOLEAN NOT NULL
        )
    """)

@app.get("/plats")
def get_plats():
    plats = query_db("SELECT id, nom, prix, disponible FROM plats", fetch=True)
    return [{"id": p[0], "nom": p[1], "prix": p[2], "disponible": bool(p[3])} for p in plats]

@app.post("/plats")
def create_plat(plat: Plat):
    query_db("INSERT INTO plats (nom, prix, disponible) VALUES (?, ?, ?)", (plat.nom, plat.prix, plat.disponible))
    return {"message": "Plat ajouté avec succès"}

@app.put("/plats/{plat_id}")
def update_plat(plat_id: int, plat: Plat):
    query_db("UPDATE plats SET nom = ?, prix = ?, disponible = ? WHERE id = ?", (plat.nom, plat.prix, plat.disponible, plat_id))
    return {"message": f"Plat {plat_id} modifié"}

@app.delete("/plats/{plat_id}")
def delete_plat(plat_id: int):
    query_db("DELETE FROM plats WHERE id = ?", (plat_id,))
    return {"message": f"Plat {plat_id} supprimé"}

# Servir le frontend React
app.mount("/", StaticFiles(directory="frontend/build", html=True), name="static")

@app.get("/")
def serve_index():
    return FileResponse("frontend/build/index.html")