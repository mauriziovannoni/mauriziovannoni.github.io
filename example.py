import streamlit as st
import numpy as np
import pandas as pd

st.title('Useful formulas for Xray optics')

st.subheader('Number of pickups by hour')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
