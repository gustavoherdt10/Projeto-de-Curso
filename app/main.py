from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.routes import barris, clientes, movimentacoes, indicadores

app = FastAPI(title="Sistema de Rastreamento de Barris")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="app/templates")

app.include_router(barris.router, prefix="/barris", tags=["Barris"])
app.include_router(clientes.router, prefix="/clientes", tags=["Clientes"])
app.include_router(movimentacoes.router, prefix="/movimentacoes", tags=["Movimentações"])
app.include_router(indicadores.router, prefix="/indicadores", tags=["Indicadores"])

@app.get("/")
def home():
    return {"mensagem": "API de Rastreamento de Barris ativa"}