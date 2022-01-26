from tarefa1.models.usuario import Usuario

from fastapi import APIRouter

router = APIRouter()

@router.post('/')
async def add_usuario(usuario: Usuario):
    await usuario.save()
    return usuario

@router.get('/')
async def lista_usuario():
    return await Usuario.objects.all()
