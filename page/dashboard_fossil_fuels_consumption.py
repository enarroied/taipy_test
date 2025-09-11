from algorithms import load_dataset

import taipy.gui.builder as tgb


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


with tgb.Page() as fossil_fuel_page:
    tgb.text("# Fossil Fuel consumption per capita by country", mode="md")
    tgb.text(
        """Data comes from [Our World in Data](https://ourworldindata.org/grapher/per-capita-fossil-energy-vs-gdp)""",
        mode="md",
    )
    tgb.selector(
        "{country}",
        lov="{lov_region}",
        on_change=on_change_country,
        dropdown=True,
        label="Country/Region",
    )
    tgb.chart(
        "{dataset_fossil_fuels_gdp_cp}",
        type="plot",
        x="Year",
        y="Fossil fuels per capita (kWh)",
        height="200%",
        layout="{layout}",
    )
    tgb.text("## Fossil fuel per capita for {country} :", mode="md")
    tgb.table("{dataset_fossil_fuels_gdp_cp}", height="400px", width="95%")
