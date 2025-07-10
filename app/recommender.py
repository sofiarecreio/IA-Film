# app/recommender.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Carrega o dataset
df = pd.read_csv('data/personality_movies.csv')

# Transforma a saída (string) em número
df['genero_favorito'] = df['genero_favorito'].astype('category')
df['genero_favorito_cat'] = df['genero_favorito'].cat.codes
label_map = dict(enumerate(df['genero_favorito'].cat.categories))

# Separa features e rótulos
X = df[['criatividade', 'extroversao', 'racionalidade']]
y = df['genero_favorito_cat']

# Treina o modelo
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Salva o modelo e o dicionário
joblib.dump(model, 'app/model.pkl')
joblib.dump(label_map, 'app/labels.pkl')
