from flask import Flask, jsonify, request
import pandas as pd
import re

app = Flask(__name__)

# Lee el archivo de Excel y crea un DataFrame
clientes_df = pd.read_excel('D:\OtroDc\Tareas\8cuatri\Compiladores\Analisador Lexico\ExpresionesRegulares\contactos.xlsx', engine='openpyxl')
clientes_df = clientes_df.fillna("")  # Reemplaza todos los valores NaN con cadenas vacías
clientes = clientes_df.to_dict('records')

def buscar_clientes(palabra):
    regex_pattern = f"({re.escape(palabra)})"
    pattern = re.compile(regex_pattern, re.IGNORECASE)
    coincidencias = [cliente for cliente in clientes if pattern.search(str(cliente["   Nombre Contacto "])) or pattern.search(str(cliente["Clave cliente"])) or pattern.search(str(cliente["Correo "])) or pattern.search(str(cliente["Teléfono Contacto  "]))]
    return coincidencias

@app.route('/buscar/<string:palabra>', methods=['GET'])
def get_buscar(palabra):
    coincidencias = buscar_clientes(palabra)
    return jsonify(coincidencias)

if __name__ == '__main__':
    app.run(debug=True)
