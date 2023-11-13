from abc import ABC, abstractmethod
import pandas as pd
import os

class DataModule(ABC):
    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def write_data(self):
        pass

class csvDataSource(DataModule):
    def __init__(self, read_file_path=None, write_file_path=None):
        self.read_file_path = read_file_path
        self.write_file_path = write_file_path

    def get_data(self):
        df = pd.read_csv(self.read_file_path)
        return df
    
    def write_data(self, data):
        if os.path.isfile(self.write_file_path):
            data.to_csv(self.write_file_path, index=False, mode='a', header=False)
        else:
            data.to_csv(self.write_file_path, index=False)


