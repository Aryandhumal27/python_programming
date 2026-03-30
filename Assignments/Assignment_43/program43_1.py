# Design machine learning application which follows below steps as

# Step 1:
# Get Data
# Load data from MarvellousInfosystems_PlayPredictor.csv file into python application.

# Step 2:
# Clean, Prepare and Manipulate data
# As we want to use the above data into machine learning application we have prepare
# that in the format which is accepted by the algorithms.
# As our dataset contains two features as Wether and Temperature. We have to replace
# each string field into numeric constants by using LabelEncoder from processing module
# of sklearn.

# Step 3:
# Train Data
# Now we want to train our data for that we have to select the Machine learning algorithm.
# For that we select K Nearest Neighbour algorithm.
# use fit method for training purpose. For training use whole dataset.

# Step 4:
# Test Data
# After successful training now we can test our trained data by passing some value of
# wether and temperature.
# As we are using KNN algorithm use value of K as 3.
# After providing the values check the result and display on screen.
# Result may be Yes or No.

# Step 5:
# Calculate Accuracy
# Write one function as CheckAccuracy() which calculate the accuracy of our algorithm.
# For calculating the accuracy divide the dataset into two equal parts as Training data and
# Testing data.
# Calculate Accuracy by changing value of K.

import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def CheckAccuracy(df):

    X = df[["Whether", "Temperature"]]
    Y = df["Play"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=42)

    for k in range(1, 15):
        model = KNeighborsClassifier(n_neighbors=k)

        model.fit(X_train, Y_train)

        Y_pred = model.predict(X_test)

        Accuracy = accuracy_score(Y_pred, Y_test)

        print(f"Accuracy of model with k = {k} : {Accuracy*100}")


def main():
    #-------------------------------------------------------------------------------------
    # Step 1 : Load the Dataset
    #-------------------------------------------------------------------------------------

    df = pd.read_csv("PlayPredictor.csv")

    print("Dataset with all records : ")
    print(df)

    #---------------------------------------------------------------------------------------
    # Step 2 : Drop Unnecessary columns
    #---------------------------------------------------------------------------------------

    df.drop(df.filter(regex='Unnamed').columns, axis=1, inplace=True)

    le = LabelEncoder()

    # Encode columns using label Encoding
    for col in df.columns:
        df[col] = le.fit_transform(df[col])

    print("\nFirst 5 records after Encoding : \n")
    print(df.head())

    #----------------------------------------------------------------------------------------
    # Step 3 : Train the dataset
    #----------------------------------------------------------------------------------------

    X = df[["Whether", "Temperature"]]
    Y = df["Play"]

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X, Y)

    #-----------------------------------------------------------------------------------------
    # Step 4 : Test the dataset
    #-----------------------------------------------------------------------------------------

    Training_data = {
        "Whether" : [0, 1, 2, 2, 1],
        "Temperature" : [1, 2, 1, 2, 0]
    }

    Testing_data = {
        "Play" : [1, 1, 0, 0, 1]
    }

    Training_data = pd.DataFrame(data=Training_data)
    Testing_data = pd.DataFrame(data=Training_data)

    Result = model.predict(Training_data)

    print("Prediction for testing data")
    for i in Result:
        if(i == 0):
            print("No")
        else:
            print("Yes")

    #--------------------------------------------------------------------------------
    # Step 5 : Calculate Accuracy using different value of k
    #--------------------------------------------------------------------------------

    CheckAccuracy(df=df)

if __name__ == "__main__":
    main()
