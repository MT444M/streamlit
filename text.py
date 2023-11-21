import streamlit as st

# Fonction pour la section d'introduction
def afficher_introduction():
    st.title("Introduction")
    st.write("Bienvenue dans notre application Blue Tech Marine, où nous explorons les défis marins et les solutions technologiques pour les relever.")
    st.write("Découvrez la beauté de la mer et les problèmes auxquels elle est confrontée.")
    st.video("demo.mp4")

# Fonction pour la section de sensibilisation
def afficher_sensibilisation():
    st.title("Sensibilisation")
    st.write("Nous vous proposons ces 4 quiz pour nous aider à comprendre l'impact de l'humain sur la vie maritime.")

# Fonction pour la section des solutions Blue Tech
def afficher_solutions_blue_tech():
    st.title("Solutions Blue Tech")
    st.write("Nous vous proposons 2 solutions Blue Tech pour lutter contre la dégradation dans le milieu maritime.")

# Titre de l'application
st.title("Blue Tech Marine")

# Section d'Introduction
st.subheader("Introduction")
afficher_introduction

# Section Sensibilisation
st.subheader("Sensibilisation")
afficher_sensibilisation
# Section Solution
st.subheader("Solutions Blue Tech")
afficher_solutions_blue_tech

# Menu principal
menu_choice = st.sidebar.radio("Menu Principal", ("Introduction", "Sensibilisation", "Solution"))

# Affichage des parties correspondantes
if menu_choice == "Introduction":
    afficher_introduction()

elif menu_choice == "Sensibilisation":
    afficher_sensibilisation()

elif menu_choice == "Solution":
    afficher_solutions_blue_tech()
