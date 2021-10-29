import plotly
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots

import numpy as np
import pandas as pd

x = np.arange(0,5,0.1)
def f(x):
    return x**2


def h(x):
    return np.sin(x)


def k(x):
    return np.cos(x)


def m(x):
    return np.tan(x)


fig = go.Figure()

fig = make_subplots(rows=2, cols=2,
                    specs=[[{"colspan": 2}, None], [{}, {}]])

fig.update_yaxes(range=[-0.5,1.5], zeroline=True, zerolinewidth=2, zerolinecolor='LightPink',col=2)
fig.update_xaxes(range=[-0.5,1.5], zeroline=True, zerolinewidth=2, zerolinecolor='#008000',col=2)

fig.add_trace(go.Scatter(x=x, y=h(x), name='h(x)=sin(x)'), 2, 2)
fig.add_trace(go.Scatter(x=x, y=k(x), name='k(x)=cos(x)'), 2, 2)
fig.add_trace(go.Scatter(x=x, y=m(x), name='m(x)=tg(x)'), 1, 1)

fig.add_trace(go.Scatter(x=x,y=f(x), mode='lines+markers', name='f(x)=x<sup>2</sup>'), 2, 1)
fig.add_trace(go.Scatter(x=x,y=x, mode='markers', name='g(x)=x'), 2, 1)
fig.update_layout(legend_orientation='h',
                  title = 'Plot Title',
                  xaxis_title = 'x Axis Title',
                  yaxis_title = 'y Axis Title',
                  legend=dict(x=.5, xanchor='center'),
                  margin=dict(l=0, r=0, t=0, b=0))
fig.update_xaxes(title='Ось X графика 1', col=1, row=1)
fig.update_xaxes(title='Ось X графика 2', col=2, row=1)
fig.update_yaxes(title='Ось Y графика 1', col=1, row=1)
fig.update_yaxes(title='Ось Y графика 2', col=2, row=1)
fig.update_traces(hoverinfo="all", hovertemplate='Аргумент: %{x}<br>Функция: %{y}')
fig.show()