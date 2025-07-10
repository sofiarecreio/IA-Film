# 🎬 IA-Film: Recomendador de Gênero de Filme com Base na Personalidade

✨ Uma Inteligência Artificial simples e divertida que sugere o gênero de filme ideal para você com base em 3 traços de personalidade: criatividade, extroversão e racionalidade.

Construído com ❤️ usando:
- `scikit-learn` para o modelo de IA
- `Streamlit` para uma interface web amigável
- `Docker` para rodar em qualquer lugar com um simples comando

---

## 🚀 Demonstração

![demo](https://media.giphy.com/media/l0MYC0LajbaPoEADu/giphy.gif)

> Acesse em: [http://localhost:8501](http://localhost:8501)

---

## 🧠 Como funciona?

Você ajusta 3 controles deslizantes:

🔹 **Criatividade**  
🔹 **Extroversão**  
🔹 **Racionalidade**

E o modelo IA te diz se o seu filme ideal é **🎭 Drama**, **😂 Comédia**, **👽 Ficção**, **💥 Ação** ou **👻 Terror**.

---

## 📁 Estrutura do Projeto

film-recommender/
├── app/
│ ├── model.pkl # Modelo IA treinado
│ ├── labels.pkl # Dicionário de rótulos
│ └── streamlit_app.py # Aplicação com Streamlit
├── data/
│ └── personality_movies.csv # Dataset de treino
├── train_model.py # Script para treinar o modelo
├── requirements.txt # Dependências do projeto
├── Dockerfile # Receita Docker
└── README.md # Este arquivo aqui!
