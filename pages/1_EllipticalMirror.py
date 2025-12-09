import streamlit as st
import numpy as np
import pandas as pd
st.set_page_config(page_title="Elliptical mirror", page_icon="")
st.markdown("# Elliptical mirror")
st.sidebar.header("Elliptical mirror")
st.write(
    """This page is a collection of useful calculation tools for daily life dealing with elliptical mirrors, for example for K-B systems. Enjoy!"""
)
st.write("Typical case: elliptical optics to focus a source point to an image point using paraxial formulas") 
p=st.text_input("insert p value (meters)", value="100")
q=st.text_input("insert q value (meters)", value="10")
theta=st.text_input("insert grazing incidence theta value (milliradians)", value="9")
thetag=float(theta)*1E-3
r=float(p)
rp=float(q)
u=np.cos(thetag)*(1/r-1/rp)
v=1/(r*rp)
a0=0
a1=0
a2=np.sin(thetag)/4*(1/r+1/rp)
a3=a2*u/2
a4=a2*(5*u**2/16+v/4)

x=np.arange(-0.5,0.5,0.001)
y=a2*x**2+a3*x**3+a4*x**4
coeff=np.polyfit(x,y,2)
prof_bestParab=np.polyval(coeff,x)
prof_bestParabRem=y-prof_bestParab
df = pd.DataFrame(y*1E6)
st.line_chart(df,x_label="mm",y_label="microns")
st.caption("Calculated ellipse profile")

df = pd.DataFrame(prof_bestParabRem*1E9)
st.line_chart(df,x_label="mm",y_label="nm")
st.caption("Calculated ellipse profile minus best parabola profile")

st.write("Radius of curvature at middle point (Km): ",round(1/(2*a2)*1E-3,3)) 
st.write("Radius of curvature of best parabola (Km): ",round(1/(2*coeff[0])*1E-3,3)) 
#st.write(r)

#df = pd.DataFrame(ypp)
#st.line_chart(df,x_label="mm",y_label="")
