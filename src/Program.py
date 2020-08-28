import argparse
from injector import Injector, Binder, inject
from typing import Dict
from Preprocessing.RetinaNet.Interfaces.IGenerateTrainingFilesService import IGenerateTrainingFilesService
from Preprocessing.RetinaNet.Interfaces.ISeparateImagesFromAnnotationsService import ISeparateImagesFromAnnotationsService
from Preprocessing.RetinaNet.Services.GenerateTrainingFilesService import GenerateTrainingFilesService
from Preprocessing.RetinaNet.Services.SeparateImagesFromAnnotationsService import SeparteImagesFromAnnotationsService
from Models.IModelFactory import IModelFactory
from Models.IModelService import IModelService
from Models.ModelFactory import ModelFactory
from Models.RetinaNetDet import RetinaNetDet
import json

def BindServices(binder: Binder):
    binder.bind(IModelFactory, to=ModelFactory())


class Program:
    @inject
    def __init__(self, modelFactory: IModelFactory):
                self.modelFactory = modelFactory
                
    
    def Main(self, parser: argparse.ArgumentParser) -> None:
        args = parser.parse_args()
        model = args.model
        config: Dict = self.__Configure()
        Model = self.modelFactory.CreateModel(model, bindServices = self.BindPreprocessingServices)
        Model.Preprocess(config)
        Model.Train()
        #Model.Predict()
        
    def __Configure(self) -> Dict:
        with open("config.json") as config:
            return json.load(config)
    
    def BindPreprocessingServices(self, binder: Binder):
        binder.bind(IGenerateTrainingFilesService, to=GenerateTrainingFilesService())
        binder.bind(ISeparateImagesFromAnnotationsService, to=SeparteImagesFromAnnotationsService())
        binder.bind(IModelFactory, to=ModelFactory())

parser = argparse.ArgumentParser(description = "A program to train a detector with some logos")
parser.add_argument('model',
                    help = "The detector you want to train")
injector: Injector = Injector(BindServices)
program = injector.get(Program)

if __name__ == "__main__":
    program.Main(parser = parser)
                
