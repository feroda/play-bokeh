# myappwithcallback.py

from random import random

from bokeh.layouts import column
from bokeh.models import Button
from bokeh.palettes import RdYlBu3
from bokeh.plotting import figure, curdoc

from bokeh.models import ColumnDataSource
import random
from bokeh.driving import count


last_x = 0
last_y = 50

source = ColumnDataSource(data=dict(x=[last_x], y=[last_y]))

@count()
def update(t):
    global last_x, last_y
    x, y = last_x + t/100, last_y+random.randrange(-5, 5)
    last_x, last_y = x, y
    source.stream(dict(x=[x], y=[y]))

# create a plot and style its properties
p = figure(x_range=(0, 100), y_range=(0, 100), toolbar_location=None)
p.border_fill_color = 'black'
p.background_fill_color = 'black'
p.outline_line_color = None
p.grid.grid_line_color = None

l = p.circle(x='x', y='y', source=source, size=10)

# put the button and plot in a layout and add to the document
curdoc().add_root(column(p))

curdoc().add_periodic_callback(update, 100)
curdoc().title = "Finta linea"
