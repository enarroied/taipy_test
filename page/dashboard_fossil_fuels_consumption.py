import pandas as pd
import taipy as tp

from data.data import dataset_fossil_fuels_gdp

country = "Spain"
region = "Europe"
lov_region = list(dataset_fossil_fuels_gdp.Entity.unique())


def load_dataset(_country):
    dataset_fossil_fuels_gdp_cp = dataset_fossil_fuels_gdp.reset_index()

    dataset_fossil_fuels_gdp_cp = dataset_fossil_fuels_gdp_cp[
        dataset_fossil_fuels_gdp["Entity"] == _country
    ]
    return dataset_fossil_fuels_gdp_cp


dataset_fossil_fuels_gdp_cp = load_dataset(country)


def on_change_country(state):
    print("country is:", state.country)
    _country = state.country
    dataset_fossil_fuels_gdp_cp = load_dataset(_country)
    state.dataset_fossil_fuels_gdp_cp = dataset_fossil_fuels_gdp_cp


layout = {"yaxis": {"range": [0, 100000]}, "xaxis": {"range": [1965, 2021]}}

page = """
# Fossil Fuel consumption by per capita by country*

Data comes from <a href="https://ourworldindata.org/grapher/per-capita-fossil-energy-vs-gdp" target="_blank">Our World in Data</a>

<|{country}|selector|lov={lov_region}|on_change=on_change_country|dropdown|label=Country/Region|>



<|{dataset_fossil_fuels_gdp_cp}|chart|type=plot|x=Year|y=Fossil fuels per capita (kWh)|height=200%|layout={layout}|>

## Fossil fuel per capita for <|{country}|>:
<|{dataset_fossil_fuels_gdp_cp}|table|height=400px|width=95%|>


"""
