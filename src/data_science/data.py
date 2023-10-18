import pandas as pd
import numpy as np

def split_data(df: pd.DataFrame, test_ratio: float = 0.2, seed: int = 0) -> tuple:
    """
    Split the dataset into train and test sets by randomly shuffling the order of the data, while fixing the random seed.

    Args:
        df (pandas.DataFrame): The data to be split into train and test sets.
        test_ratio (float): The percentage of the test set. Must be between 0 and 1.
        seed (int): The shuffling parameter.

    Returns:
        tuple: A tuple containing X_train, y_train, X_test, and y_test DataFrames.
    """
    # Let n be the number of rows of the DataFrame df
    n = df.shape[0]

    # We fix the seed to the value seed, which is 0 by default
    np.random.seed(seed)

    # The number of elements of the test and train sets.
    n_test = int(n * test_ratio)

    if n - n_test <= 0:
        return "Please choose a valid ratio for the test set"

    # We choose at random the indices of the test set.
    test_indices = np.random.choice(np.arange(0, n), n_test, replace=False)

    # To get the indices of the train set, we create an array with values from 0 to n-1, then we remove the values of test_indices array.
    indices = np.arange(n)
    train_indices = indices[~np.isin(indices, test_indices)]

    # Here we create two dataframes used for training and testing
    df_train = df.iloc[train_indices]
    df_test = df.iloc[test_indices]

    # Here we separate the train and test sets into two subsets containing the explanatory variables and the variable to predict
    X_train, X_test = df_train.drop('price', axis=1), df_test.drop('price', axis=1)
    y_train, y_test = df_train['price'].to_frame(), df_test['price'].to_frame()

    return X_train, y_train, X_test, y_test
