
#-----This class load the dataset and perform basic analysis-----
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle 
import os
class DataSetAnalyzer:
    def __init__(self,filepath):
        self.filepath = filepath
        self.df = None
        self.X = None
        self.y = None
        self.model = None

    def load_data(self):
        self.df = pd.read_csv(self.filepath)
        print("Data loaded successfuly")
        return self.df

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

    def prepare_data(self, target_col):
        """
        Prepares the dataset for modeling by splitting it into features (X) and target (y).

        Parameters:
        target_col (str): The name of the target column in the dataset.
        """
        if self.df is None:
            print("Data is not loaded")
            return
        elif target_col not in self.df.columns :
            print(f"{target_col} not found in the dataset")
            return
        else:
            self.X = self.df.drop(target_col, axis = 1)
            self.y = self.df[target_col]
            print("\nData prepared successfully")

    def train_model(self,model):
        if self.X is None or self.y is None:
            print("\nData is not prepared")
            return
        else:
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X,self.y, test_size= 0.2, random_state=42)

        self.model = model
        self.model.fit(self.X_train,self.y_train)
        print("Model is trained successfully")

    def evaluate_model(self):
        if self.model is None:
            print("model is not trained")
            return
        else:
             predictions = self.model.predict(self.X_test)
             accuracy = accuracy_score(self.y_test,predictions)
        
        return accuracy     

    def predict(self, input_data):
        try:
            prediction = self.model.predict([input_data]) 
            return prediction[0] 
        except Exception as e:
                print("prediction error:",e)
                return str(e)
                          

           

    def save_model(self, file_path):

        if self.model is None:
            print("Model is not trained")
            return
        else:
            folder = os.path.dirname(file_path)
            if folder:
                os.makedirs(folder, exist_ok = True)
 
            
            with open(file_path,"wb") as f:
                pickle.dump(self.model, f)
                 


    def load_model(self, file_path):
        if not os.path.exists(file_path):
            print("File not found")
            return
        if os.path.isdir(file_path):
            print("Invalid path: It is a directory")
            return
        with open(file_path,"rb") as f:
            self.model = pickle.load(f) 
        print("Model loaded successfully")               


    def run_all(self):
        self.load_data()
        self.basic_info()
        self.statistics()
        self.visualization()


