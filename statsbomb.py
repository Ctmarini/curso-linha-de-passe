# import pandas as pd
from statsbombpy import sb

# Configurar o pandas para exibir todas as linhas e colunas
# pd.set_option('display.max_rows', None)  # Exibir todas as linhas
# pd.set_option('display.max_columns', None)  # Exibir todas as colunas
# pd.set_option('display.width', None)  # Ajusta a largura para evitar quebras
# pd.set_option('display.max_colwidth', None)  # Ajusta a largura das colunas

# competições -> partidas -> eventos

comp = sb.competitions()
matches = sb.matches(43, 106)
# print(matches[['match_id', 'match_date','home_team','away_team']].head())
events = sb.events(3857258)
# print(events[['type', 'player', 'pass_recipient', 'location', 'pass_end_location']].head())


passes = events[['type', 'player', 'pass_recipient', 'location', 'pass_end_location']]
passes = passes[passes['type']=='Pass']

print(passes.head())