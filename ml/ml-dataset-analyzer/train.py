from src.dataset_analyzer import DataSetAnalyzer
from sklearn.neighbors import KNeighborsClassifier
import sys

def train(url,target_output):
    
    analyzer = DataSetAnalyzer(url)

    #load data
    analyzer.load_data()
    #prepare the data , input ,output 
    analyzer.prepare_data(target_output)

    features = list(analyzer.X.columns)
    
    #split the data , train the model
    model = KNeighborsClassifier()
    analyzer.train_model(model)

    # accuracy measure
    accuracy = analyzer.evaluate_model()
    print(f"Accuracy:{accuracy}")

    #saving the model into the folder models using pikcle 

    file_path = "models/model.pkl"
    analyzer.save_model(file_path)


if __name__ == "__main__":
    if len(sys.argv)<3:
        print("Usage: python train.py <dataset_path> ,<target_output>") # in the commmand terminal provide dataset path along with function name
        sys.exit(1)

    url = sys.argv[1]
    target_output = sys.argv[2]
    train(url,target_output)
