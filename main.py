from algorithms import create_fossil_fuel_dataset, load_dataset
from page.dashboard_fossil_fuels_consumption import page

from taipy import Gui


def on_change_country(state):
    """Update the dataset based on the selected country.

    Args:
        state (object): The "state" of the variables ran by the program
    (value changes through selectors)

    Returns:
        None
    """
    with state as s:
        print("country is:", s.country)
        dataset_fossil_fuels_gdp_cp = load_dataset(
            s.country, s.dataset_fossil_fuels_gdp
        )
        s.dataset_fossil_fuels_gdp_cp = dataset_fossil_fuels_gdp_cp


if __name__ == "__main__":

    dataset_fossil_fuels_gdp = create_fossil_fuel_dataset()
    # Variable for the chart
    country = "Spain"
    region = "Europe"
    lov_region = list(dataset_fossil_fuels_gdp.Entity.unique())

    dataset_fossil_fuels_gdp_cp = load_dataset(country, dataset_fossil_fuels_gdp)

    layout = {"yaxis": {"range": [0, 100000]}, "xaxis": {"range": [1965, 2021]}}

    Gui(page).run(use_reloader=True, title="Test", dark_mode=False)
