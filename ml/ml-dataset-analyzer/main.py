from src.dataset_analyzer import DataSetAnalyzer

def main():
    
    analyzer = DataSetAnalyzer(None)

    #loading the trained  model
    DEFAULT_MODEL_PATH = "models/model.pkl"
    analyzer.load_model(DEFAULT_MODEL_PATH)

    #CLI

    dict_quit = {"exit", "quit", "q"}
    while True:
        
        user_input = input("enter values for :should be same as input features length: ")
        
        if user_input.lower()  in dict_quit:
            break
        
        try:
            values = user_input.split(",")
            user_input_df = [float(x) for x in values]


            prediction = analyzer.predict(user_input_df)
            print(f"predicted flower is {prediction}")
        except Exception as e:
            print("Invalid input:",e)    





if __name__ == "__main__":
    main()
