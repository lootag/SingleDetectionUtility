from interface import implements
from typing import *
import types
from Interfaces.IInferenceService import IInferenceService

class InferenceService(implements(IInferenceService)):
    def Predict(self) -> None:
        raise NotImplementedError