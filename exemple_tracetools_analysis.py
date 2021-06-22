import tracetools_analysis; import bokeh
events = load_file('~/.ros/tracing/pingpong')# Lire la trace
handler = Ros2Handler.process(events)# (Pré-)traiter les données
data_util = Ros2DataModelUtil(handler.data)
callback_symbols = data_util.get_callback_symbols()# Extraire les fonctions de callback
duration = bokeh.plotting.figure(...)
for obj, symbol in callback_symbols.items():# Pour chaque callback...
    owner_info = data_util.get_callback_owner_info(obj)
    if not owner_info or '/parameter_events' in owner_info:#   Filtrer les subscriptions internes
        continue
    duration_df = data_util.get_callback_durations(obj)#   Obtenir les données de durée
    duration.line(x='timestamp', y='duration', legend=str(symbol),#   Ajouter au graphique
                  source=bokeh.models.ColumnDataSource(duration_df))
bokeh.io.show(duration)# Afficher le graphique final
