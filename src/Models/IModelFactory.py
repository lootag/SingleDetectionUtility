from interface import Interface
from Models.IModelService import IModelService
import types

class IModelFactory(Interface):
    def CreateModel(self, model: str) -> IModelService:
        pass
