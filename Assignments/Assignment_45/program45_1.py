# Step 1:
# Get Data

# Step 2:
# Clean, Prepare and Manipulate data

# Step 3:
# Train Data

# Step 4:
# Test Data

# Step 5:
# Calculate Accuracy

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


def main():
    Border = "-"*70
    #-------------------------------------------------------------------------
    # Step 1 : Load the dataset
    #-------------------------------------------------------------------------

    print(Border)
    print("Step 1 : Load the dataset")
    print(Border)

    print("Read csv file")
    df = pd.read_csv('WinePredictor.csv')

    print(df.head())

    #-------------------------------------------------------------------------
    # Step 2 : Clean, Prepare and Manipulate data
    #-------------------------------------------------------------------------

    print(Border)
    print("Step 2 : Clean, Prepare and Manipulate data")
    print(Border)

    # Check Missing value present or not
    print(Border)
    print("Check Missing value present or not : ")
    print(Border)
    print(df.isna().sum())

    # Shape before check Duplicate record
    print(Border)
    print("Shape before check Duplicate record : ")
    print(Border)
    print(df.shape)

    # Check Duplicated records present or not
    print(Border)
    print("Check Duplicated records present or not : ")
    print(Border)
    print(df.drop_duplicates())

    # Shape After check Duplicate record
    print(Border)
    print("Shape After check Duplicate record : ")
    print(Border)
    print(df.shape)

    # Check datatypes of columns
    print(Border)
    print("Check datatype of columns : ")
    print(Border)
    print(df.info())

    #-------------------------------------------------------------------------
    # Step 3 : Train the dataset
    #-------------------------------------------------------------------------

    print(Border)
    print("Step 3 : Train the dataset")
    print(Border)
    
    X = df.drop(columns=["Class"])                  # Independant variables
    Y = df["Class"]                                 # Dependant variable

    model = DecisionTreeClassifier()                # Create the object of model

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model.fit(X_train, Y_train)

    print("Model trained successfully")

    #-------------------------------------------------------------------------
    # Step 4 : Test the dataset
    #-------------------------------------------------------------------------

    print(Border)
    print("Step 4 : Test the dataset")
    print(Border)

    Y_pred = model.predict(X_test)

    print("Model Test Successfully")

    #-------------------------------------------------------------------------
    # Step 5 : Calculate Accuracy
    #-------------------------------------------------------------------------

    print(Border)
    print("Step 5 : Calculate Accuracy")
    print(Border)

    # Calculate Accuracy
    Accuracy = accuracy_score(Y_pred, Y_test)
    print("Accuracy is : ", Accuracy*100)

    # Display Confusion matric
    cm = confusion_matrix(Y_pred, Y_test)
    print("COnfusion matrix are : \n", cm)

    # Display classification report
    cr = classification_report(Y_pred, Y_test)
    print("Classification report : \n", cr)

if __name__ == "__main__":
    main()