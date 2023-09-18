{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "\n",
    "def load_data(filename: str) -> pd.DataFrame:\n",
    "    \"\"\"_summary_\n",
    "\n",
    "    Args:\n",
    "        filename (str): _description_\n",
    "\n",
    "    Returns:\n",
    "        pd.DataFrame: _description_\n",
    "    \"\"\"\n",
    "    df = pd.read_csv(filename)\n",
    "    return df\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "env",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.12"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
