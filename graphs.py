import pandas as pd 
import plotly.express as px
import plotly.subplots as sp


def make_bar_charts(pvt_tbl, x_, y_list):
    # y_list : list of pvt_tbl column names
    # returns plotly Figure
    fig = sp.make_subplots(rows=1, cols=len(y_list))
    for i, Y in enumerate(y_list):
        pvt_tbl = pvt_tbl.sort_values(by=Y, ascending=False)
        fig_i= px.bar(pvt_tbl, x=x_, y=Y)
        fig.add_trace(fig_i['data'][0], row=1, col=i+1)
        fig.update_yaxes(title_text=Y, row=1, col=i+1)
    fig.update_layout(height=400, width=1100)
    return fig



    