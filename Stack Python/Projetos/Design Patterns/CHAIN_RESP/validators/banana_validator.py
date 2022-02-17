from .interface import ValidatorInterface

class BananaValidator(ValidatorInterface):

    def validate(self, comida: str) -> bool:
        if comida == 'banana': return True
        return False
    
    def action(self) -> None:
        print('Macaco come banana')
    
     