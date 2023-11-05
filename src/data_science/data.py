import pandas as pd
import numpy as np

def split_data(df: pd.DataFrame, test_ratio: float = 0.2, seed: int = 0, stratify_col: str = None) -> tuple[pd.DataFrame]:
    """Split the dataset into train and test sets by manually stratifying the data based on a specified column.

    Args:
        df (pd.DataFrame): The input DataFrame.
        test_ratio (float): The percentage of the test set. This float number must be between 0 and 1.
        seed (int): The shuffling parameter.
        stratify_col (str): The column in the DataFrame to stratify based on.

    Returns:
        tuple[pd.DataFrame]: X_train, y_train, X_test, y_test
    """
    # Let n be the number of observations we have
    n = df.shape[0]

    # We fix the seed to the value seed, which is 0 by default
    np.random.seed(seed)

    # The number of elements of the test and train sets.
    n_test = int(n * test_ratio)

    if n - n_test <= 0:
        return "Please choose a valid ratio for the test set"

    if stratify_col is not None:
        # Manually perform stratification based on the specified column
        unique_values = df[stratify_col].unique()

        test_indices = []
        for value in unique_values:
            value_indices = np.where(df[stratify_col] == value)[0]
            np.random.shuffle(value_indices)
            split_point = int(len(value_indices) * test_ratio)
            test_indices.extend(value_indices[:split_point])

        # To get the indices of the train set, we create an array with values from 0 to n-1, then we remove the values of test_indices array.
        indices = np.arange(n)
        train_indices = indices[~np.isin(indices, test_indices)]

        # Here we create two dataframes used for training and testing
        df_train = df.iloc[train_indices]
        df_test = df.iloc[test_indices]

    else:
        # No stratification, so we choose at random the indices of the test set.
        test_indices = np.random.choice(np.arange(0, n), n_test, replace=False)

        # To get the indices of the train set, we create an array with values from 0 to n-1, then we remove the values of test_indices array.
        indices = np.arange(n)
        train_indices = indices[~np.isin(indices, test_indices)]

        # Here we create two dataframes used for training and testing
        df_train = df.iloc[train_indices]
        df_test = df.iloc[test_indices]

    # From the created dataframes, ....
    X_train, X_test = df_train.drop('price', axis=1), df_test.drop('price', axis=1)
    y_train, y_test = df_train['price'].to_frame(), df_test['price'].to_frame()

    return X_train, y_train, X_test, y_test
