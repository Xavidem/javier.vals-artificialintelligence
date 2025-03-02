import json
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Cargar los resultados desde results.json
with open("results.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Unir todos los abstracts en un solo texto
abstracts = " ".join([info["abstract"] for info in data.values() if info["abstract"] != "No abstract found"])

# Crear la nube de palabras
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(abstracts)

# Mostrar la nube de palabras
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Keyword Cloud from Abstracts")
plt.show()

