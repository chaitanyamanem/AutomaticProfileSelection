from abc import ABC, abstractmethod
import pypdf

class FileReader(ABC):
    @abstractmethod
    def getText(self, file_path):
        pass
    
class PdfReader(FileReader):
    def getText(self, file_path):
        reader = pypdf.PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
            
        return text
        
class DocReader(FileReader):
    def getText(self, file_path):
        pass