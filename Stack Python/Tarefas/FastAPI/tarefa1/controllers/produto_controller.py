from models.produto import Produto

from fastapi import APIRouter

router = APIRouter()

@router.post('/')
async def add_produto(produto: Produto):
    await produto.save()
    return produto

@router.get('/')
async def lista_produto():
    return await Produto.objects.all()
