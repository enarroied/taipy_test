from algorithms.load_dataset import load_dataset
from data.data import dataset_fossil_fuels_gdp


def on_change_country(state):
    """Update the dataset based on the selected country.

    Args:
        state (object): The "state" of the variables ran by the program (value changes through selectors)

    Returns:
        None
    """
    print("country is:", state.country)
    _country = state.country
    dataset_fossil_fuels_gdp_cp = load_dataset(_country, dataset_fossil_fuels_gdp)
    state.dataset_fossil_fuels_gdp_cp = dataset_fossil_fuels_gdp_cp


page = """
# Fossil Fuel consumption by per capita by country*

Data comes from <a href="https://ourworldindata.org/grapher/per-capita-fossil-energy-vs-gdp" target="_blank">Our World in Data</a>

<|{country}|selector|lov={lov_region}|on_change=on_change_country|dropdown|label=Country/Region|>
<|{dataset_fossil_fuels_gdp_cp}|chart|type=plot|x=Year|y=Fossil fuels per capita (kWh)|height=200%|layout={layout}|>

## Fossil fuel per capita for <|{country}|>:
<|{dataset_fossil_fuels_gdp_cp}|table|height=400px|width=95%|>
"""
