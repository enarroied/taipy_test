import pandas as pd


def create_fossil_fuel_dataset(
    fossil_fuels_path: str = "data/per-capita-fossil-energy-vs-gdp.csv",
    country_codes_path: str = "data/country_codes.csv",
) -> pd.DataFrame:
    """
    Load, merge, filter, and transform the fossil fuels per capita vs GDP dataset.

    Args:
        fossil_fuels_path (str): Path to the fossil fuels vs GDP CSV file.
        country_codes_path (str): Path to the country codes CSV file.

    Returns:
        pd.DataFrame: Cleaned and transformed dataset.
    """
    dataset_fossil_fuels_gdp = pd.read_csv(fossil_fuels_path)
    country_codes = pd.read_csv(country_codes_path)

    dataset_fossil_fuels_gdp = dataset_fossil_fuels_gdp.merge(
        country_codes[["alpha-3", "region"]],
        how="left",
        left_on="Code",
        right_on="alpha-3",
    )

    dataset_fossil_fuels_gdp = dataset_fossil_fuels_gdp[
        ~dataset_fossil_fuels_gdp["Fossil fuels per capita (kWh)"].isna()
    ].reset_index(drop=True)

    # Convert from kWh to Wh
    dataset_fossil_fuels_gdp["Fossil fuels per capita (kWh)"] *= 1000

    return dataset_fossil_fuels_gdp
