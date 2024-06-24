import io
import json

# Leer el archivo original con la codificación latin1
with io.open('mysite_data.json', 'r', encoding='latin1') as f:
    data = f.read()

# Guardar el archivo en UTF-8
with io.open('mysite_data_utf8.json', 'w', encoding='utf-8') as f:
    f.write(data)