from taipy import Gui
from page.dashboard_fossil_fuels_consumption import *

if __name__ == "__main__":
    Gui(page).run(
        use_reloader=True,
        title="Test",
        dark_mode=False,
    )  # use_reloader=True if you are in development