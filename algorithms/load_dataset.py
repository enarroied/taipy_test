def load_dataset(country, dataset_fossil_fuels_gdp):
    """Load dataset for a specific country.

    Args:
        country (str): The name of the country.
        dataset_fossil_fuels_gdp (pd.DataFrame): Original DataFrame with all
    countries information.

    Returns:
        pandas.DataFrame: A DataFrame containing the fossil fuels GDP data for the specified country.
    """
    dataset_fossil_fuels_gdp_cp = dataset_fossil_fuels_gdp.copy().reset_index()
    return dataset_fossil_fuels_gdp_cp[dataset_fossil_fuels_gdp["Entity"] == country]
