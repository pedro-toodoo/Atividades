from fastapi import APIRouter

from controllers import usuario_controller as usuarios
#from controllers import produto_controller as produtos

router = APIRouter()

router.include_router(usuarios.router, prefix='/usuarios')





