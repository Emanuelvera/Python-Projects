import plotly.express as px
import pandas as pd


folder = input("Ingrese ruta del archivo csv, sino cargo ninguno ingrese arg.csv =>")


def generate_bubble_map(csv_file):
      # Lee el archivo CSV
    df = pd.read_csv(csv_file)

    # Valores dinamicos
    color_column = df.columns[0]

    value_columns = df.columns[1:]

    # Crear el mapa de burbujas
    fig = px.scatter_mapbox(df,
                            lon=df["lon"],
                            lat=df["lat"],
                            zoom=5,
                            color=df[color_column],
                            size=df[value_columns[0]],  # Se puede cambiar esto según lo que se necesite
                            size_max=70,
                            width=1200,
                            height=900,
                            title="Argentina",
                            )
  

    fig.update_layout(mapbox_style="carto-positron")
    fig.update_layout(margin={"r": 0, "t": 50, "l": 0, "b": 1})
    fig.show()
    

    print("Plot complete")

# Ingresar el path del archivo en este caso arg.csv
generate_bubble_map(folder)


#Esto es una prueba