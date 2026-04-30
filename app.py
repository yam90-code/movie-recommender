import streamlit as st
import pickle

df = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

def recommend(movie):
    index = df[df["title"] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),
                      reverse=True, key=lambda x: x[1])
    movies = []
    for i in distances[1:6]:
        movies.append(df.iloc[i[0]].title)
    return movies

st.title("🎬 Movie Recommender")

selected_movie = st.selectbox("Select a movie", df["title"].values)

if st.button("Recommend"):
    results = recommend(selected_movie)
    for movie in results:
        st.write(movie)