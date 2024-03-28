from SelTest import farben
import matplotlib.pyplot as plt
from collections import Counter
import csv 
import os

farben_count = Counter(farben)
# Extrahieren Sie Labels und Counts in separate Listen
labels = list(farben_count.keys())
counts = list(farben_count.values())

# Erstellen Sie den Scatter-Plot
plt.scatter(labels, counts, s=[count*100 for count in counts], alpha=0.5)

# Beschriften Sie die Achsen und zeigen Sie den Plot an
plt.xlabel('Farben')
plt.ylabel('Häufigkeit')
plt.title('Häufigkeit der Farben')
plt.show()

with open(r'C:\Users\boraa\Documents\GitHub\FlipAnalysis\farben.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Farbe', 'Häufigkeit'])
    for farbe, count in farben_count.items():
        writer.writerow([farbe, count])
