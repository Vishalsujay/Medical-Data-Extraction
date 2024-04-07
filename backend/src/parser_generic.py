from abc import ABC, abstractmethod

#Declaring parent class
class MedicalDocParser(ABC):
    def __init__(self,text):
        self.text = text
        
    @abstractmethod
    def parse(self):
        pass