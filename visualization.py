
import dash
from dash import dcc, html, Input, Output, dash_table, State
import plotly.express as px

from values import data, fig_gains,fig_reussites_echecs,fig_avg_successes,fig_time,time_to_seconds

# --------------------------------Application Dash ---------------------------------------------------

app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

couleur_principale = 'black'
couleur_secondaire = '#404040'
couleur_texte = '#ffffff'

Tab_Style = {'backgroundColor': couleur_principale, 'color': couleur_texte}
Content_Style = {'height': '100%','backgroundColor':couleur_secondaire,'color': couleur_texte,'margin': '0','padding': '0','text-align': 'left'}
Main_Style = {'height': '100%','backgroundColor':couleur_principale,'width': '90%', 'float': 'left','margin': '0','padding': '0','color': couleur_texte,'text-align': 'center'}

# Définition du layout de l'application
app.layout = html.Div([
    # Barre de navigation à gauche avec des onglets pour sélectionner les graphiques
    html.Div([
        dcc.Tabs(id="tabs", value='tab-start', children=[
            dcc.Tab(label="Introduction", value='tab-start', style=Tab_Style),
            dcc.Tab(label="L'équipe la plus riche", value='tab-1', style=Tab_Style),
            dcc.Tab(label='Taux échecs et réussites', value='tab-2', style=Tab_Style),
            dcc.Tab(label="L'équipe la plus victorieuse", value='tab-3', style=Tab_Style),
            dcc.Tab(label="L'équipe ayant le plus de temps", value='tab-4', style=Tab_Style),
            dcc.Tab(label="Recherche", value='tab-search', style=Tab_Style),
        ], vertical=True, style={'height': '100vh'}),
    ], style={'width': '10%', 'float': 'left', 'backgroundColor':couleur_principale}),

    # Contenu principal qui change en fonction de l'onglet sélectionné
    html.H3('Projet KHOU_LE : Analyse des équipes de Fort Boyard', style= Main_Style),
    html.Div(id='tabs-content', style=Main_Style),
])

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])

def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Quelle équipe à gagner le plus?'),
            dcc.Graph(id='graph-gains', figure=fig_gains),
            dcc.Dropdown(
                id='dropdown-gains',
                options=[
                    {'label': 'Top 5', 'value': 5},
                    {'label': 'Top 10', 'value': 10},
                    {'label': 'Toutes les équipes', 'value': len(data)},
                ],
                value=len(data),
                style={'color': 'black'},),
            html.P("Le gain final d'une équipe dans Fort Boyard est déterminé lors de l'épreuve finale, où les participants recueillent des pièces d'or dans une cage. Cette visualisation met en évidence les équipes qui ont excellé dans cette épreuve, capturant ainsi les plus grandes richesses. Les données révèlent non seulement les montants accumulés mais aussi la performance exceptionnelle de certaines équipes sous pression.", style={'padding': '20px'})
        ], style=Content_Style)
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Comparaison de réussites/échec de chaques équipes'),
            # Contenu pour Graph 2
            dcc.Graph(id='graph-reussites-echecs', figure=fig_reussites_echecs),
            html.P("Cette section offre une comparaison approfondie entre les succès et les revers rencontrés par chaque équipe. En examinant le nombre d'épreuves réussies contre les échecs, nous pouvons identifier les stratégies qui ont conduit à la victoire ou à la défaite. Cette analyse fournit un aperçu précieux des dynamiques d'équipe et de l'importance de la préparation et de l'adaptabilité.", style={'padding': '20px'}),
        ],style=Content_Style )
    elif tab == 'tab-3':
        return html.Div([
            html.H3("Quelle équipe à eu le plus de réussites?"),
            # Contenu pour Graph 3
            dcc.Graph(id='graph-moy-réusite', figure=fig_avg_successes),
            html.P("L'analyse des performances globales révèle que l'équipe ARSEP se distingue par le nombre le plus élevé d'épreuves réussies. Avec des membres expérimentés tels que Vianney, Laura Boulleau, et Maeva Coucke, qui ont participé à plusieurs reprises au jeu, cette équipe illustre l'impact de l'expérience et de la cohésion d'équipe sur le succès.", style={'padding': '20px'}),
        ],style=Content_Style)
    elif tab == 'tab-4':
        return html.Div([
            html.H3("Quelle équipe a eu le plus de temps dans l'épreuve final?"),
            # Contenu pour Graph 2
            dcc.Graph(id='graph-time', figure=fig_time),
            html.Div(id='slider-value-time'),
            dcc.Slider(
                id='slider-time',
                min=0,  
                max=225,  
                step=1,  
                value=0,
                marks={i: str(i) for i in range(0, 226, 10)}
            ),
            html.P("L'épreuve finale de Fort Boyard est un défi contre la montre, où le temps alloué varie en fonction des performances antérieures de l'équipe. Cette section explore comment le temps accordé lors de cette épreuve finale influence le gain final et souligne l'importance de maximiser chaque seconde pour augmenter les chances de victoire.", style={'padding': '20px'}),
        ],style=Content_Style)
    elif tab == 'tab-start':
        return html.Div([
            html.H3("Introduction "),
            html.Img(src='https://fs-prod-cdn.nintendo-europe.com/media/images/10_share_images/games_15/nintendo_switch_4/H2x1_NSwitch_FortBoyard_image1600w.jpg', style={'max-width': '75%', 'height': 'auto'}),
            html.P("Ce projet propose une analyse détaillée des performances des équipes ayant participé à Fort Boyard entre 2019 et 2023. En exploitant des données issues directement du jeu, nous explorerons différents aspects des défis rencontrés par les participants, mettant en lumière les stratégies gagnantes, les taux de réussite et d'échec, ainsi que l'efficacité des équipes dans la gestion du temps lors de l'épreuve finale.", style={'padding': '20px'}),
        ],style=Content_Style )
    elif tab == 'tab-search':
        return html.Div([
            html.H3("Recherche dans l'archive :"),
            dcc.Dropdown(
                id='search-dropdown',
                placeholder='Recherche par équipe...',
                search_value='',
                options=[],
                style={'color': 'black'},
            ),
            html.Div(id='search-output')
        ],style=Content_Style )
    else:
        return html.Div('Sélectionnez une sous-catégorie')






# -------------------------- Section 'Update' ----------------------------------

# Update Graph Gain ----------------------------

@app.callback(
    Output('graph-gains', 'figure'),
    [Input('dropdown-gains', 'value')]
)
def update_gains_graph(selected_value):
    # Filtrer les données basées sur la valeur sélectionnée
    sorted_data = sorted(data, key=lambda x: int(x['Gain'].replace(" ", "")), reverse=True)[:selected_value]
    equipes_filtered = [team['Equipe'] for team in sorted_data]
    gains_filtered = [int(team['Gain'].replace(" ", "")) for team in sorted_data]

    # Créer et retourner le nouveau graphique
    fig = px.bar(x=equipes_filtered, y=gains_filtered, labels={'x': 'Équipes', 'y': 'Gains'},
                 title=f'Top {selected_value} des Gains par Équipe')
    return fig

# Update Graph Time ---------------------------

@app.callback(
    Output('graph-time', 'figure'),
    [Input('slider-time', 'value')]
)
def update_time_graph(selected_value):
    # Convertir selected_value en entier si ce n'est pas déjà le cas
    selected_value = int(selected_value)

    # Filtrer les données basées sur la valeur sélectionnée en secondes
    filtered_data = [team for team in data if time_to_seconds(team['Temps']) <= selected_value]

    # Trier les données filtrées par temps en ordre croissant
    sorted_filtered_data = sorted(filtered_data, key=lambda team: time_to_seconds(team['Temps']))

    # Préparer les données pour le graphique
    equipes_filtered = [team['Equipe'] for team in sorted_filtered_data]
    times_filtered = [time_to_seconds(team['Temps']) for team in sorted_filtered_data]

    # Créer et retourner le nouveau graphique trié
    fig = px.bar(x=equipes_filtered, y=times_filtered, labels={'x': 'Équipes', 'y': 'Temps Total (en secondes)'},
                 title=f'Équipes avec le Temps Total Égal ou Inférieur à {selected_value} secondes')
    return fig

# Update Slider Time --------------------------------

@app.callback(
    Output('slider-value-time', 'children'),
    [Input('slider-time', 'value')]
)
def update_slider_value_output(selected_value):
    return f'Valeur du slider : {selected_value}'

# Update Search bar ---------------------------------

@app.callback(
    Output('search-dropdown', 'options'),
    [Input('search-dropdown', 'search_value')]
)
def update_search_options(search_value):
    if search_value:
        # Filtrer les équipes qui contiennent la chaîne recherchée
        search_results = [team['Equipe'] for team in data if search_value.lower() in team['Equipe'].lower()]
        # Créer des options pour le Dropdown
        return [{'label': team, 'value': team} for team in search_results]
    return []

# Callback pour afficher les informations de l'équipe sélectionnée
@app.callback(
    Output('search-output', 'children'),
    [Input('search-dropdown', 'value')]
)
def display_selected_team_info(selected_team):
    if selected_team:
        # Filtrer les données pour l'équipe sélectionnée
        team_info = next((team for team in data if team['Equipe'] == selected_team), None)
        if team_info:
            # Ici, vous pouvez formater les informations de l'équipe comme vous le souhaitez
            return html.Div([
                html.H3(selected_team),
                # Afficher d'autres informations de team_info ici
            ])
    return 'Veuillez sélectionner une équipe.'


# Lance l'application  ---------------------------------------------------
def create_dashboard():
    return app

