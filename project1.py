from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go

app = Dash(__name__)
about_dataset="Humans have greatly associated themselves with Songs & Music. It can improve mood, decrease pain and anxiety, and facilitate opportunities for emotional expression. Research suggests that music can benefit our physical and mental health in numerous ways. Lately, multiple studies have been carried out to understand songs & it's popularity based on certain factors. Such song samples are broken down & their parameters are recorded to tabulate. Predicting the Song Popularity is the main aim."
songs_df = pd.read_csv('song_data.csv')


fig1 = px.bar(songs_df,x='song_popularity',y='acousticness',color='song_popularity')
fig2 = px.scatter(songs_df, x='acousticness',y='song_popularity',
                 size="song_popularity", color="song_popularity", hover_name="song_popularity",
                 log_x=True, size_max=30)

fig3 = px.scatter(songs_df, x='loudness',y='energy', size="song_popularity",
                 color="song_popularity", hover_name="song_popularity",
                 log_x=True, size_max=30)

fig4 = px.scatter(songs_df, x='loudness',y='acousticness', size="song_popularity",
                 color="song_popularity", hover_name="song_popularity",
                 log_x=True, size_max=30)

fig6 = px.histogram(songs_df, x='audio_mode', color='audio_mode')
fig7 = px.histogram(songs_df, x='key', color='audio_mode')



app.layout = html.Div(children=[
    # All elements from the top of the page



    html.Div(children=[
        html.H1(children='Song Dataset'),
        html.H4(children='About...'),
        html.H4(children=about_dataset),

        html.H4(children='Song popularity Vs Acoustics'),
        dcc.Graph(
            id='graph1',
            figure=fig1
        )

    ]),
    # New Div for all elements in the new 'row' of the page
    html.Div(children=[


        dcc.Graph(
            id='graph2',
            figure=fig2
        )

    ]),
    html.Div(children=[

        html.H4(children='Loudness Vs Energy'),
        dcc.Graph(
            id='graph3',
            figure=fig3
        )

    ]),
    html.Div(children=[

        html.H4(children='Loudness Vs Acoustics'),
        dcc.Graph(
            id='graph4',
            figure=fig4
        )

    ]),
    # html.Div(children=[
    #
    #     dcc.Graph(
    #         id='graph5',
    #         figure=fig5
    #     )
    #
    # ]),

    html.Div(children=[

        html.H4(children='Audio_mode'),

        dcc.Graph(
            id='graph6',
            figure=fig6
        )

    ]),

    html.Div(children=[



        dcc.Graph(
            id='graph7',
            figure=fig7
        )

    ])


])



if __name__ == '__main__':
    app.run_server(debug=True)
