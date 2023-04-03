from taipy import Gui

page = """
# Hello World 🌍 with *Taipy*

This is my first Taipy test app.

And it is running fine!
"""

Gui(page).run(use_reloader=True)  # use_reloader=True if you are in development
