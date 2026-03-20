
#-----This class load the dataset and perform basic analysis-----
import pandas as pd
import matplotlib.pyplot as plt

class DataSetAnalyzer:
    def __init__(self,filepath):
        self.filepath = filepath
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.filepath)
        print("Data loaded successfuly")

    def basic_info(self):
        print("Shape:", self.df.shape)
        print("\nColumns:", self.df.columns)
        print("\nInfo:")
        self.df.info()

    def statistics(self):
        print("\n Statistical Summary:")
        print(self.df.describe())

    def missing_values(self):
        print("\nTotal Missig values per Coloumn")
        print(self.df.isnull().sum())

    def visualization(self):
        self.df.hist(figsize = (10,8))
        plt.show() 

    def run_all(self):
        self.load_data()
        self.basic_info()
        self.statistics()
        self.visualization()

