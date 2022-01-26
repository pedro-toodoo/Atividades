from models.papel import Papel

from fastapi import APIRouter

router = APIRouter()

@router.post('/')
async def add_papeis(papel: Papel):
    await papel.save()
    return papel

@router.get('/')
async def lista_papeis():
    return await Papel.objects.all()
