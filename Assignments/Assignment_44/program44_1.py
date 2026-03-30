# We have to design Machine Learning application which uses Classification technique.

# Design machine learning application which follows below steps as

# Step 1:
# Get Data
# Load data from MarvellousAdvertising.csv file into python application.

# Step 2:
# Clean, Prepare and Manipulate data
# As we want to use the above data into machine learning application we have prepare
# that in the format which is accepted by the algorithms.

# Step 3:
# Train Data
# Now we want to train our data for that we have to select the Machine learning algorithm.
# For that we select Linear Regression algorithm from scikit learn library.
# For training purpose divide the dataset into half part.
# Use train method to train our dataset.

# Step 4:
# Test the data
# Test data by passing the remaining half part of the data set.

# Step 5:
# Display predicted values of Linear regression algorithms as well as expected values
# which are provided by the data set.

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score

def main():
    
    # Step 1:
    # Get Data
    # Load data from MarvellousAdvertising.csv file into python application.

    #--------------------------------------------------------------------------------------
    # Step 1 : Load the dataset
    #--------------------------------------------------------------------------------------

    df = pd.read_csv("Advertising.csv")
    print(df.head())

    # Step 2:
    # Clean, Prepare and Manipulate data
    # As we want to use the above data into machine learning application we have prepare
    # that in the format which is accepted by the algorithms.

    #---------------------------------------------------------------------------------------
    # Step 2 : Clean the dataset, Remove Unnamed index column
    #---------------------------------------------------------------------------------------

    df.drop(df.filter(regex='Unnamed').columns, axis=1, inplace=True)

    print(df.head())

    # Step 3:
    # Train Data
    # Now we want to train our data for that we have to select the Machine learning algorithm.
    # For that we select Linear Regression algorithm from scikit learn library.
    # For training purpose divide the dataset into half part.
    # Use train method to train our dataset.

    #---------------------------------------------------------------------------------------
    # Step 3 : Train the model
    #---------------------------------------------------------------------------------------

    X = df.drop(columns=["sales"])
    Y = df["sales"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=42)

    model = LinearRegression()

    model.fit(X_train, Y_train)  

    # Step 4:
    # Test the data
    # Test data by passing the remaining half part of the data set.

    #---------------------------------------------------------------------------------------
    # Step 4 : Test the model
    #---------------------------------------------------------------------------------------

    Y_pred = model.predict(X_test)

    #---------------------------------------------------------------------------------------------
    # Step 5: Display predicted values of Linear regression algorithms as well as expected values
    # --------------------------------------------------------------------------------------------

    PredictedOutcome = pd.DataFrame(
        {
        "Actual Values" : Y_test.values,
        "Predicted Values" : Y_pred
    })

    print(PredictedOutcome.head())

if __name__ == "__main__":
    main()