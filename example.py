import streamlit as st
import numpy as np
import pandas as pd

st.title('Useful formulas for Xray optics')

st.subheader('Elliptical focusing mirrors')
st.write("Typical case: elliptical optics to focus a source point to an image point using paraxial formulas") 
st.text_input("insert p value (meters)", value="100")
st.text_input("insert q value (meters)", value="10")
st.text_input("insert theta value (milliradians)", value="9")
thetag=float(theta)*1E-3
r=double(p)
rp=double(q)
u=np.cos(thetag)*(1/r-1/rp)
v=1/(r*rp)


