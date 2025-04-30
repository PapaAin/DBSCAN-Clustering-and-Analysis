# DBSCAN Clustering and Analysis

## Description
This project involves reading a tab-separated dataset (data.tsv) from the src folder into a DataFrame. 
The dataset consists of two features (X1, X2) and a label (y). 
The primary goal is to apply DBSCAN clustering using different values of the eps parameter, ranging from 0.05 to 0.2 in increments of 0.05.

## Key Tasks:

- Load the dataset into a DataFrame.

- Perform clustering using DBSCAN with multiple eps values.

- Collect and analyze the following metrics for each clustering run:
    - Accuracy score (excluding outliers).
    - Number of clusters formed.
    - Number of outlier points detected (DBSCAN assigns label -1 to outliers).

## Special Considerations:

- Modify the find_permutation function to exclude outliers from the accuracy score calculation.

- If the number of detected clusters does not match the number of unique labels in the original dataset, set the accuracy score to **NaN**.

The final results will be compiled into a DataFrame with appropriate column names to facilitate analysis and comparisons across different eps values.
