import zipfile
import xml.etree.ElementTree as ET

# Ruta del archivo GeoGebra
ggb_file = 'puntos.ggb'
# Renombrar a zip
zip_file = 'archivo.zip'

# Cambiar nombre del archivo
with open(ggb_file, 'rb') as f_in, open(zip_file, 'wb') as f_out:
    f_out.write(f_in.read())

# Extraer el archivo XML
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extract('geogebra.xml')

# Leer el archivo XML
tree = ET.parse('geogebra.xml')
root = tree.getroot()

# Buscar y extraer coordenadas de puntos
points = []
for element in root.findall(".//element[@type='point']"):
    label = element.get('label')
    coords = element.find('coords')
    x = coords.get('x')
    y = coords.get('y')
    z = coords.get('z')
    points.append((label, x, y, z))

# Guardar los puntos en un archivo de texto
with open('puntos.txt', 'w') as f:
    for point in points:
        f.write(f"{point[0]}: ({point[1]}, {point[2]}, {point[3]})\n")

print("Puntos extraídos y guardados en puntos.txt")