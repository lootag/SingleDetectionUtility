import sys 
sys.path.append("../..")
import unittest
import os
from Preprocessing.RetinaNet.Services.GenerateTrainingFilesService import GenerateTrainingFilesService

class GenerateTrainingFilesServiceTest(unittest.TestCase):
    #Arrange
    def setUp(self):
        super(GenerateTrainingFilesServiceTest, self).setUp()
        with open('../../../LogosVOC/JPGImages/testImage.jpg', 'w'):
            pass
        with open('../../../LogosVOC/JPGImages/testImage2.jpg', 'w'):
            pass
        with open('../../../LogosVOC/Annotations/testAnnotation.txt', 'w'):
            pass
        with open('../../../LogosVOC/Annotations/testAnnotation2.txt', 'w'):
            pass
    
    #Arrange
    def tearDown(self):
        super(GenerateTrainingFilesServiceTest, self).tearDown()
        os.remove('../../../LogosVOC/JPGImages/testImage.jpg')
        os.remove('../../../LogosVOC/JPGImages/testImage2.jpg')
        os.remove('../../../LogosVOC/Annotations/testAnnotation.txt')
        os.remove('../../../LogosVOC/Annotations/testAnnotation2.txt')
    
    def test_Should_Files_Be_Generated_Correctly(self):
        #Act
        service = GenerateTrainingFilesService()
        service.GenerateTrainingFiles("../../../LogosVOC/JPGImages", "../../../LogosVOC/ImageSets/Main", 0.4)

        #Assert
        self.assertEqual(3, len(os.listdir("../../../LogosVOC/ImageSets/Main")))
        self.assertTrue("trainval.txt" in os.listdir("../../../LogosVOC/ImageSets/Main"))
        self.assertTrue("train.txt" in os.listdir("../../../LogosVOC/ImageSets/Main"))
        self.assertTrue("val.txt" in os.listdir("../../../LogosVOC/ImageSets/Main"))

        with open("../../../LogosVOC/ImageSets/Main/trainval.txt", 'r') as trainval:
            allFiles = trainval.readlines()
            self.assertTrue("testImage\n" in allFiles)
            self.assertTrue("testImage2\n" in allFiles)
            for file in allFiles:
                    self.assertTrue(file[-3:] != "jpg")
            with open("../../../LogosVOC/ImageSets/Main/train.txt", 'r') as train:
                trainFiles = train.readlines()
                self.assertTrue(len(trainFiles) < len(allFiles))
                for file in trainFiles:
                    self.assertTrue(file[-3:] != "jpg")
            
            with open("../../../LogosVOC/ImageSets/Main/train.txt", 'r') as val:
                valFiles = val.readlines()
                self.assertTrue(len(valFiles) < len(allFiles))
                for file in valFiles:
                    self.assertTrue(file[-3:] != "jpg")
                

    

if __name__ == "__main__":
    unittest.main()
    