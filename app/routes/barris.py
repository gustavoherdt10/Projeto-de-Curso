from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def listar_barris():
    return {"mensagem": "Lista de barris"}