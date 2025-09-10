page = """
# Fossil Fuel consumption per capita by country*

Data comes from 
<a href="https://ourworldindata.org/grapher/per-capita-fossil-energy-vs-gdp" 
target="_blank">Our World in Data</a>

<|{country}|selector|lov={lov_region}|on_change=on_change_country|dropdown|label=Country/Region|>
<|{dataset_fossil_fuels_gdp_cp}|chart|type=plot|x=Year|y=Fossil fuels per capita (kWh)|height=200%|layout={layout}|>

## Fossil fuel per capita for <|{country}|>:
<|{dataset_fossil_fuels_gdp_cp}|table|height=400px|width=95%|>
"""
