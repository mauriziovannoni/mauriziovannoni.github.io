import streamlit as st
import numpy as np
import pandas as pd

st.title('Useful formulas for Xray optics')

st.subheader('Elliptical focusing mirrors')
st.write("Typical case: elliptical optics to focus a source point to an image point using paraxial formulas") 
st.text_input("insert p value (meters)", value="100")


chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
