from SelTest import farben
import matplotlib.pyplot as plt
from collections import Counter

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