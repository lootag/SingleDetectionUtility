import sys
sys.path.append("..")
import unittest
import os
from Services.SeparateImagesFromAnnotationsService import SeparteImagesFromAnnotationsService
class SeperateImagesFromAnnotationsServiceTest(unittest.TestCase):
    #Arrange
    def setUp(self):
        super(SeperateImagesFromAnnotationsServiceTest, self).setUp()
        with open('../../LogosVOC/JPGImages/testImage.jpg', 'w'):
            pass
        with open('../../LogosVOC/JPGImages/testImage2.jpg', 'w'):
            pass
        with open('../../LogosVOC/JPGImages/testAnnotation.txt', 'w'):
            pass
        with open('../../LogosVOC/JPGImages/testAnnotation2.txt', 'w'):
            pass
    #Arrange
    def tearDown(self):
        super(SeperateImagesFromAnnotationsServiceTest, self).tearDown()
        os.remove('../../LogosVOC/JPGImages/testImage.jpg')
        os.remove('../../LogosVOC/JPGImages/testImage2.jpg')
        os.remove('../../LogosVOC/Annotations/testAnnotation.txt')
        os.remove('../../LogosVOC/Annotations/testAnnotation2.txt')
    
    def test_Should_Annotations_Folder_Not_Be_Empty(self):        
        #Act
        service = SeparteImagesFromAnnotationsService()
        service.SeparateImagesFromAnnotations(imagesFolder = "../../LogosVOC/JPGImages", annotationsFolder = "../../LogosVOC/Annotations")
        
        #Assert
        self.assertEqual(2, len(os.listdir("../../LogosVOC/Annotations")))

    def test_Should_Images_Folder_Not_Contain_Txt(self):
        #Act
        service = SeparteImagesFromAnnotationsService()
        service.SeparateImagesFromAnnotations(imagesFolder = "../../LogosVOC/JPGImages", annotationsFolder = "../../LogosVOC/Annotations")

        #Assert
        for file in os.listdir("../../LogosVOC/JPGImages"):
            self.assertNotEqual(file[-3:], "txt")
        
    
    






if __name__ == "__main__":
    unittest.main()