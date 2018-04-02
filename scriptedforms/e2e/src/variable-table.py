from datetime import datetime

import numpy as np
import pandas as pd

from IPython.display import display, Markdown

display(Markdown(
    'Loaded variable-table.py at {}'
    .format(str(datetime.now()))
))

input_types = {
    '1st': 'toggle',
    '3rd': 'number',
    '4th': 'dropdown',
    '5th': 'dropdown',
    '6th': 'readonly'
}

dropdown_items = {
  '4th': ['apple', 'orange', 'pear'],
  '5th': {
    'a': ['sally', 'margaret', 'annita'],
    'b': ['george', 'philip', 'simpson'],
    'c': ['red', 'green', 'blue']
  }
}

table = None


def load_table():
    global table
    table = pd.read_csv('variable-table.csv', index_col=0)
    display(Markdown(
        'Loaded variable-table.csv at {}'
        .format(str(datetime.now()))
    ))
