import pandas as pd


def load_data(filename: str) -> pd.DataFrame:
    """_summary_

    Args:
        filename (str): _description_

    Returns:
        pd.DataFrame: _description_
    """
    df = pd.read_csv(filename)
    return df
