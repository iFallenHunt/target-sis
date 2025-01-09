import json
import xml.etree.ElementTree as ET

# Load data from JSON file
with open("fat/dados.json", "r") as json_file:
    json_data = json.load(json_file)

# Load data from XML file
xml_data = []
tree = ET.parse("fat/dados (2).xml")
root = tree.getroot()
for row in root.findall("row"):
    dia = int(row.find("dia").text)
    valor = float(row.find("valor").text)
    xml_data.append({"dia": dia, "valor": valor})

# Combine data from both sources
combined_data = json_data + xml_data

# Filter out days with zero revenue
filtered_data = [
    entry["valor"]
    for entry in combined_data
    if entry["valor"] > 0
]

# Calculate metrics
if filtered_data:
    menor_faturamento = min(filtered_data)
    maior_faturamento = max(filtered_data)
    media_mensal = sum(filtered_data) / len(filtered_data)
    dias_acima_media = [
        entry["dia"]
        for entry in combined_data
        if entry["valor"] > media_mensal
    ]
else:
    menor_faturamento = maior_faturamento = media_mensal = 0
    dias_acima_media = []

# Output results
print(f"Menor faturamento diário: {menor_faturamento}")
print(f"Maior faturamento diário: {maior_faturamento}")
print(f"Dias com faturamento acima da média mensal: {dias_acima_media}")
