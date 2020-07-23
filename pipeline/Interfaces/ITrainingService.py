from interface import Interface
from typing import *
import types

class ITrainingService(Interface):
    def Train(self) -> None:
        pass