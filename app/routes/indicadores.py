from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def listar_indicadores():
    return {"mensagem": "Lista de indicadores"}