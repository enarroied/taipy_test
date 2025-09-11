from algorithms import create_fossil_fuel_dataset, load_dataset
from page.dashboard_fossil_fuels_consumption import fossil_fuel_page

from taipy import Gui

if __name__ == "__main__":

    dataset_fossil_fuels_gdp = create_fossil_fuel_dataset()
    # Variable for the chart
    country = "Spain"
    region = "Europe"
    lov_region = list(dataset_fossil_fuels_gdp.Entity.unique())

    dataset_fossil_fuels_gdp_cp = load_dataset(country, dataset_fossil_fuels_gdp)

    layout = {"yaxis": {"range": [0, 100000]}, "xaxis": {"range": [1965, 2021]}}

    Gui(fossil_fuel_page).run(
        use_reloader=True, title="Fossil Fuel Page", dark_mode=False
    )
