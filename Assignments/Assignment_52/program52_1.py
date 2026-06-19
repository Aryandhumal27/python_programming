import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def main():

    # ----------------------------------------------------------------------
    # Step 1 : Load and Explore the Dataset
    # ----------------------------------------------------------------------

    border = "-" * 70

    print(border)
    print("Step 1 : Load and Explore the Dataset")
    print(border)

    df = pd.read_csv("student_performance_ml(2).csv")

    print(border)
    print("Shape of Dataset")
    print(border)
    print(df.shape)

    print(border)
    print("First 5 Records")
    print(border)
    print(df.head())

    print(border)
    print("Information of Dataset")
    print(border)
    print(df.info())

    print(border)
    print("Null Values")
    print(border)
    print(df.isnull().sum())

    # ----------------------------------------------------------------------
    # Step 2 : Select Required Features
    # ----------------------------------------------------------------------

    print(border)
    print("Step 2 : Select Required Features")
    print(border)

    X = df[["G1", "G2", "G3", "studytime", "failures", "absences"]]

    print(X.head())

    # ----------------------------------------------------------------------
    # Step 3 : Scale the Data
    # ----------------------------------------------------------------------

    print(border)
    print("Step 3 : Scale the Data")
    print(border)

    scalar = StandardScaler()

    X_scaled = scalar.fit_transform(X)

    print("Shape of Scaled Data :", X_scaled.shape)

    # ----------------------------------------------------------------------
    # Step 4 : Train K-Means Clustering Model
    # ----------------------------------------------------------------------

    print(border)
    print("Step 4 : Train K-Means Clustering Model")
    print(border)

    model = KMeans(
        n_clusters=3,
        random_state=42
    )

    df["Cluster"] = model.fit_predict(X_scaled)

    print(df[["G1", "G2", "G3", "Cluster"]].head())

    # ----------------------------------------------------------------------
    # Step 5 : Display Cluster Statistics
    # ----------------------------------------------------------------------

    print(border)
    print("Step 5 : Display Cluster Statistics")
    print(border)

    print("Number of Students in Each Cluster")
    print(df["Cluster"].value_counts())

    print(border)
    print("Mean Values of Each Cluster")
    print(border)

    cluster_mean = df.groupby("Cluster")[["G1", "G2", "G3", "studytime", "failures", "absences"]].mean()

    print(cluster_mean)

    # ----------------------------------------------------------------------
    # Step 6 : Assign Cluster Names
    # ----------------------------------------------------------------------

    print(border)
    print("Step 6 : Assign Cluster Names")
    print(border)

    top_cluster = cluster_mean["G3"].idxmax()
    struggle_cluster = cluster_mean["G3"].idxmin()

    average_cluster = list(set(cluster_mean.index) - {top_cluster, struggle_cluster})[0]

    cluster_names = {
        top_cluster: "Top Performers",
        average_cluster: "Average Students",
        struggle_cluster: "Struggling Students"
    }

    df["Performance"] = df["Cluster"].map(cluster_names)

    print(df[["Cluster", "Performance"]].head())

    print(border)
    print("Cluster Mapping")
    print(border)

    print(cluster_names)

    # ----------------------------------------------------------------------
    # Step 7 : Visualize Clusters
    # ----------------------------------------------------------------------

    print(border)
    print("Step 7 : Visualize Clusters")
    print(border)

    plt.figure(figsize=(8, 6))

    plt.scatter(
        df["G3"],
        df["studytime"],
        c=df["Cluster"]
    )

    plt.xlabel("Final Grade (G3)")
    plt.ylabel("Study Time")
    plt.title("Student Performance Clusters")

    plt.show()

    # ----------------------------------------------------------------------
    # Step 8 : Display Students with Performance Group
    # ----------------------------------------------------------------------

    print(border)
    print("Step 8 : Students Performance Group")
    print(border)

    print(df[["G1", "G2", "G3", "studytime", "failures", "absences", "Performance"]].head(20))


if __name__ == "__main__":
    main()