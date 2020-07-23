from interface import Interface
import types
from typing import *

class IInferenceService(Interface):
    def Predict(self) -> None:
        pass