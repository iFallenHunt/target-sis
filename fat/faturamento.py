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
    day = int(row.find("day").text)
    value = float(row.find("value").text)
    xml_data.append({"day": day, "value": value})

# Combine data from both sources
combined_data = json_data + xml_data

# Filter out days with zero revenue
filtered_data = [
    entry["value"]
    for entry in combined_data
    if entry["value"] > 0
]

# Calculate metrics
if filtered_data:
    lowest_revenue = min(filtered_data)
    highest_revenue = max(filtered_data)
    monthly_average = sum(filtered_data) / len(filtered_data)
    days_above_average = [
        entry["day"]
        for entry in combined_data
        if entry["value"] > monthly_average
    ]
else:
    lowest_revenue = highest_revenue = monthly_average = 0
    days_above_average = []

# Output results
print(f"Lowest daily revenue: {lowest_revenue}")
print(f"Highest daily revenue: {highest_revenue}")
print(f"Days with revenue above the monthly average: {days_above_average}")