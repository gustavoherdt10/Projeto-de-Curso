from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def listar_movimentacoes():
    return {"mensagem": "Lista de movimentações"}