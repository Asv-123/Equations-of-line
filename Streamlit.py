import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


st.title('Slope and Intercept vizualizer')

m = st.number_input('Enter the slope value: ',value=1)
c = st.number_input('Enter the Y intercept value: ',value=2)

st.write(f"The equation of the line is: y = {m}x + {c}")

x = np.linspace(-10,10,100)

y = m*x + c

colors = ['Green','Red','Blue']
fig,ax  =plt.subplots()

clr = ''

if m > 0:
    clr = colors[0]
    text = 'Positive Slope line'
elif m < 0:
    clr = colors[1]
    text = 'Negative Slope line'
else:
    clr = colors[2]
    text = 'Parallel Slope line'

ax.plot( x,y ,label = f"y = {m}x + {c}",color = clr)
ax.axhline(0,color = 'black',linewidth = 2)
ax.axvline(0,color = 'black',linewidth = 2)
ax.set_xlabel('X-axis')
ax.set_ylabel('y-axis')
ax.set_title(text)
ax.grid()

if st.button('Visualize'):
    st.pyplot(fig)
