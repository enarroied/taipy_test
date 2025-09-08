from algorithms.load_dataset import load_dataset
from data.data import dataset_fossil_fuels_gdp
from page.dashboard_fossil_fuels_consumption import on_change_country, page

from taipy import Gui

if __name__ == "__main__":

    # Variable for the chart
    country = "Spain"
    region = "Europe"
    lov_region = list(dataset_fossil_fuels_gdp.Entity.unique())

    dataset_fossil_fuels_gdp_cp = load_dataset(country, dataset_fossil_fuels_gdp)

    layout = {"yaxis": {"range": [0, 100000]}, "xaxis": {"range": [1965, 2021]}}

    Gui(page).run(use_reloader=True, title="Test", dark_mode=False)
