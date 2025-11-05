from fastapi import APIRouter

order_router = APIRouter(prefix="/order", tags="order")

@order_router.get("/")
async def order():
    """
    Essa é a rota padrão de order do nosso sistema. Todas as rotas dos order precisam de autenticação
    """
    return {"mensagem": "Você acessou a rota de order"}