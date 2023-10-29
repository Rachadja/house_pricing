import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def etude_univarie(data):
    """
    Description:
    This function displays the distribution of each variable.
    
    Parameters:
    data: A DataFrame
    
    Returns:
    Graphical figures
    """
    colonne_quanti = data.select_dtypes("float").columns
    colonne_quali = data.select_dtypes("object").columns
    
    fig, axes = plt.subplots(nrows=3, ncols=len(colonne_quanti), figsize=(15, 6))

    # Parcourez chaque colonne quantitative et affichez son histogramme
    for i, col in enumerate(colonne_quanti):
        sns.histplot(data[col].to_numpy(), kde=True, ax=axes[0, i], color="blue", bins=30)
        axes[0, i].set_xlabel(col)
        axes[0, i].set_ylabel('Fréquence')
    
    # Parcourez chaque colonne qualitative et affichez un diagramme en secteurs (pie chart)
    for i, col in enumerate(colonne_quali):
        counts = data[col].value_counts()
        if i < len(colonne_quali) and i < 6:
            row = 1
        else:
            row = 2
            i -= 6  # Réduisez l'indice pour accéder correctement aux colonnes qualitatives dans la deuxième ligne
        axes[row, i].pie(counts, labels=counts.index, autopct='%1.1f%%')
        axes[row, i].set_xlabel(col)
        axes[row, i].set_ylabel('')
    for i in range(1,6):
        axes[2,i].axis('off')    

    # Ajustez la mise en page pour éviter les chevauchements d'étiquettes
    plt.tight_layout()
    # Affichez la figure
    fig.suptitle("Figure Title")
    plt.show() 




def etude_multivarie(df):
    """
    Description:
    This function displays the correlation matrix between quantitative variables and the data distribution between two variables.
    
    Parameters:
    data: pandas.DataFrame.
    
    Returns:
    None.
    """
    # ...
    quantitative_col = df.select_dtypes("float").columns

    # ...
    fig, axes = plt.subplots(nrows=4, ncols=3, figsize=(12, 12))
    axes_flat = axes.flatten()

    # Iterate through each quantitative column and display its relationship with the price 
    for i, col in enumerate(quantitative_col):
        if col != 'price':
            if col == 'area':
                sns.regplot(x=col, y='price', data=df, line_kws={"color": 'red'}, ax=axes_flat[i-1])
                axes_flat[i-1].set_xlabel(col)
                axes_flat[i-1].set_ylabel('Price')
            else:    
                sns.histplot(x=col, y='price', data=df, line_kws={"color": 'red'}, ax=axes_flat[i-1], cmap='coolwarm',cbar=True)
                axes_flat[i-1].set_xlabel(col)
                axes_flat[i-1].set_ylabel('Price')
            
    # ...
    sns.heatmap(df.select_dtypes(include=['float64', 'int64']).corr(), annot=True, cmap='coolwarm', ax = axes_flat[5], cbar=False)

    # ...
    colonne_quali = df.select_dtypes('object').columns
    for i, col in enumerate(colonne_quali):
        sns.histplot(x=col, y='price', data=df, line_kws={"color": 'red'}, ax=axes_flat[5+i], cmap='coolwarm',cbar=True)
        axes_flat[5+i].set_xlabel(col)
        axes_flat[5+i].set_ylabel('Price')     
    
    
    plt.tight_layout()
    # Display the figure
    plt.show()