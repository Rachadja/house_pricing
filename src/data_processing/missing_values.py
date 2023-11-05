def handle_missing_values(data):
    # Séparer les variables quantitatives des variables qualitatives
    quantitative_columns = data.select_dtypes(include=['int', 'float']).columns
    qualitative_columns = data.select_dtypes(include=['object']).columns

    # Calculer la moyenne de chaque variable quantitative
    medians = data[quantitative_columns].median()

    modes = data[qualitative_columns].mode().iloc[0]

    # Remplacer les valeurs manquantes dans les variables quantitatives par leur moyenne respective
    data[quantitative_columns] = data[quantitative_columns].fillna(medians)

    # Remplacer les valeurs manquantes dans les variables qualitatives par le mode respectif
    data[qualitative_columns] = data[qualitative_columns].fillna(modes)
    return data