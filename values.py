import json
import plotly.express as px
import plotly.graph_objs as go

with open('data.json', 'r') as file:
    data = json.load(file)
    
    

# Initialisation des variables pour les graphiques
equipes = [team['Equipe'] for team in data]
gains = [int(team['Gain'].replace(" ", "")) for team in data]

# Création du graphique des gains
equipes_gains_sorted, gains_sorted = zip(*sorted(zip(equipes, gains), key=lambda x: x[1]))
fig_gains = px.bar(x=equipes_gains_sorted, y=gains_sorted, labels={'x': 'Équipes', 'y': 'Gains'}, title='Histogramme des Gains par Équipe')

# Calcul des réussites et échecs (ajustement nécessaire ici)
reussites = []
echecs = []
for team in data:
    if 'Reussites' in team:  # Vérifie si la clé 'Reussites' existe
        toutes_reussites = team['Reussites'].count("Reussite")
        tous_echecs = team['Reussites'].count("Echec")
    else:
        toutes_reussites = 0
        tous_echecs = 0
    reussites.append(toutes_reussites)
    echecs.append(tous_echecs)

# Création Histogramme
fig_reussites_echecs = go.Figure(data=[
    go.Bar(name='Réussites', x=equipes, y=reussites),
    go.Bar(name='Échecs', x=equipes, y=echecs)
])
fig_reussites_echecs.update_layout(barmode='group', title='Réussites et Échecs par Équipe')

# Graph Moy Réussite ---------------------------------------------------
data_triage = data.copy()

# Triez la nouvelle variable par ordre croissant de réussite moyenne
data_triage.sort(key=lambda team: team['Reussites'].count("Reussite") / len(team['Reussites']) if team['Reussites'] else 0)


# Création Histogramme
# Supposons que chaque élément dans 'Reussites' est une chaîne de caractères ("Reussite" ou "Echec")
fig_avg_successes = px.bar(
    x=[team['Equipe'] for team in data_triage],
    y=[team['Reussites'].count("Reussite") / len(team['Reussites']) if team['Reussites'] else 0 for team in data_triage],
    labels={'x': 'Équipe', 'y': 'Nombre Moyen de Réussites'},
    title='Nombre Moyen de Réussites par Équipe'
)


# Graph Temps ---------------------------------------------------
# Fonction minute en seconde
def time_to_seconds(time_value):
    if isinstance(time_value, str):
        # Si c'est une chaîne, la diviser et convertir en secondes
        parts = time_value.split(':')
        return int(parts[0]) * 60 + int(parts[1])
    elif isinstance(time_value, list) and len(time_value) == 2:
        # Si c'est une liste avec deux éléments, les convertir en entiers et calculer les secondes
        return int(time_value[0]) * 60 + int(time_value[1])
    else:
        # Gérer autrement les cas non prévus
        return 0

# Application de la nouvelle fonction pour chaque élément de données
times = [time_to_seconds(team['Temps']) for team in data]

# Tri des données par temps en ordre décroissant
equipe_time_sorted, times_sorted = zip(*sorted(zip(equipes, times), key=lambda x: x[1]))

# Création Histogramme
fig_time = px.bar(x=equipe_time_sorted, y=times_sorted, labels={'x': 'Équipes', 'y': 'Temps Total (seconde)'},
                  title="Temps Total (en seconde) par Équipe dans l'épreuve final")



