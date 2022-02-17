from interface import DatabaseInterface
from typing import Type, Dict, Union

class UseCase:

    def __init__(self, repository: Type[DatabaseInterface]) -> None:
        self.__repository = repository #privado

    def do_something(self, data: bool) -> Union[Dict, None]:
        if data is True:
            repositoryResponse = self.__repository.select_one()
            return repositoryResponse
        
        return None