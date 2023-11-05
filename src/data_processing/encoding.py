import pandas as pd

def variable_encoding(data):
    """
    Description:
    We change the values 'yes, no' to '1,0' respectively.
    We encode the categorical variables.
    We change the values True and False in our data to 1 and 0 respectively.
    We replace 'semi-furnished' with 'semi_furnished'.

    Args:
    data: pandas.DataFrame.

    Returns:
    df: pandas.DataFrame.
    """
    # Create a variable that contains the names of object-type columns
    object_columns = data.select_dtypes(include=['object']).columns

    # Change the values 'yes' and 'no' in our data to 1 and 0 respectively
    for col in object_columns:
        data[col] = data[col].replace({'yes': 1, 'no': 0, 'semi-furnished': 'semi_furnished'})

    # Perform one-hot encoding
    one_hot = data.select_dtypes(include=['object']).columns
    data = pd.get_dummies(data, columns=one_hot)
    
    # Change boolean values to 1 and 0
    boolean_columns = data.select_dtypes(include=['bool']).columns
    data[boolean_columns] = data[boolean_columns].astype(int)
    
    return data
