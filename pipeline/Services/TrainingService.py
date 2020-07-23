from interface import implements
from Interfaces.ITrainingService import ITrainingService
from typing import *
import types

class TrainingService(implements(ITrainingService)):
    def Train(self) -> None:
        raise NotImplementedError