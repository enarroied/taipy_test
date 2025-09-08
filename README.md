[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)

# Taipy Test

## What is this app?

This is a very minimal app using Taipy to test it.

I use this application [to write a Medium article introducing Taipy GUI](https://medium.com/better-programming/discovering-taipy-and-taipy-gui-e1b664765017).

This mini-application only uses Taipy GUI, it does not use Taipy Core.

* ```main.py``` calls dashboard_fossil_fuels_consumption.py
* ```hello_taipy.py``` is just a Hello World app with Taipy

The dashboard app only has a selector for Countries or regions of the world. Data about fossil fuel consumption, per capita, will be shown as a plot and in a table, for the selected country or region.

![mage of the dashoard](pics/GUI_app.png "The GUI app displayed in the browser")

## Data sources

The application uses:

* The dataset about [Per Capita fossil energy consumption vs. GDP from Our World in Data](https://ourworldindata.org/grapher/per-capita-fossil-energy-vs-gdp?).
* A CSV file with country codes and continents [from this GitHub repo](https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes/blob/master/all/all.csv).
