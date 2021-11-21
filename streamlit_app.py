from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import plotly.express as px
from render_plots import *

st.set_page_config(layout="wide")
"""
# Lead to Sustainable Future with Sievo
"""

left_col, right_col = st.columns(2)

left_col.header("CO2 emissions per kg")
left_col.write(plot2())

right_col.header("CO2 emissions per kg")
right_col.write(plot4())


left_col.header("CO2 emissions per kg")
left_col.write(plot1())

right_col.header("CO2 emissions per kg")
right_col.write(plot4())