from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import sympy as sp

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


t = np.linspace(0, 0.05, 100)
v = np.sqrt(2) * 220 * np.sin(2 * np.pi * 60 * t)
media = np.mean(v)
media
fig = plt.figure(dpi=100)
plt.plot(t, v)
plt.grid()
plt.xlabel('$t$')
plt.ylabel('v')
plt.title('Função 1')
plt.show()

#w = (np.sqrt(2) * 220 * np.sin(2 * np.pi * 60 * t))**2
w = v**2
media2 = np.mean(w)
media2
fig = plt.figure(dpi=100)
plt.plot(t, w)
plt.grid()
plt.xlabel('$t$')
plt.ylabel('w')
plt.title('Função 2')
plt.show()
