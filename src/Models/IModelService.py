from interface import Interface
from typing import Dict

class IModelService(Interface):
    def Preprocess(self, config: Dict):
        pass
    
    def Train(self):
        pass
    
    def Predict(self):
        pass