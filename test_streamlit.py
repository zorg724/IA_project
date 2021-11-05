# Pour lancer streamlit:
# $ streamlit run app.py
# ATTENTION, on n'utilise pas Python pour lancer !

import datetime

#Third party
import streamlit as st
import numpy
import pandas



print("RAPPEL DE LA PAGE...")

st.title("Form for the Users")
st.write("Here, you can answer to some questions in this form.")

st.write("HTML c'est de la merde!")

user_id = st.text_input("Entrez votre ID:", value="Votre ID", max_chars=7)

info = st.text_area("Entrer un texte multiline:", "Put information here",
                    help='Vous pouvez tout raconter!')

age = st.number_input("Age", min_value=18, max_value=100, step=1)

smoke_checkbox = st.checkbox("Est-ce que vous fumez?")
genre_film_radio = st.radio("Quel type de film aimez vous?",
                 options=['horror', 'adventure', 'romantic'])

# on demande la sasie de la date
date_input = st.date_input("Quand etes vous né?", datetime.date(2019,7,6))

#Puis on l'affiche en dessous:
st.write ("La date de votre anniversaire:", date_input)


weight_slider = st.slider("Saisser votre poid:", min_value=40., max_value=150., step=0.5)


physical_form = st.selectbox("Select level of your physical condition",
                             options=["Bad", "Normal", "Good"])

colors = st.multiselect('What are your favorite colors',
                        options=['Green', 'Yellow', 'Red', 'Blue', 'Pink'])

image = st.file_uploader("Upload your photo", type=['jpg', 'png'])


# SUBMIT INPUT:
submit = st.button("Submit")

if submit:
    st.write("You submitted the form")

# On peut ajouter une slide bar (bar de coté), avec dedans les controles qu'on veut:
click_sidebar = st.sidebar.button('PRESSE side bar button!')
vitesse_multiselect  = st.sidebar.multiselect('Choisisser la vitesse:',
                                options=['lent', 'rapide', 'lumiere'])

if click_sidebar:
    st.sidebar.write(f"Vous avez cliqué sur le bouton de la bar de coté et choisit la vitesse: {vitesse_multiselect}")


# ajout de colonnes:
col1, col2 = st.columns(2)
nb_clic_cat = 0 # le récupérer d'une persistance car la page est répellé à chaque action
 
with col1:
    print("Entrer dans la colonne 1...")
    print(f"nb_clic_cat: {nb_clic_cat}")

    st.image("https://static.streamlit.io/examples/cat.jpg", width=300)
    clic_cat = st.button("Like cats")

    if clic_cat:

        nb_clic_cat += 1
        # Penser à sauver le nb_clic_cat ailleur car 
        # à chaque clic_cat, toute la page est rapelée

        print(f"nb_clic_cat: {nb_clic_cat}")
        st.write(f" '+' {nb_clic_cat}")

with col2:
    print("Entrer dans la colonne 2...")

    st.image("https://static.streamlit.io/examples/dog.jpg", width=355)
    clic_dog = st.button("Like dogs")
    nb_clic_dog = 0 # à récupere de la persistance
    if clic_dog:
        
            nb_clic_dog += 1
            # Penser à sauver le nb_clic_cat ailleur car 
            # à chaque clic_cat, toute la page est rapelée

            print(f"clic_dog: {nb_clic_dog}")
            st.write(f" '+' {nb_clic_dog}")

###TP Linux
FONCTIONS ={"2*x+n": lambda x,n: 2*x + n,
             "x**n": lambda x,n: x**n,
             "n*cos(x)": lambda x,n: n*numpy.cos(x)
            }

fct_select = st.selectbox ("choix fonction:", ["2*x+n", "x**n","n*cos(x)"])
fct = FONCTIONS[fct_select]

n = st.slider("Valeur de n:", min_value =0, max_value=10)

# 3 colonnes:
Donnees = {
    "x": range(-5,6,1),
    "y": (fct(x,n) for x in range(-5,6,1)),
    "z": 0
}

print(f"Donnees:\n{Donnees}")

data = pandas.DataFrame(Donnees)
# CELA AFFICHE AUTOMATIQUE La table "excell" de panda !
st.write (data)

# un Chart associé: on va calculer des points intermeidaires

RESOLUTION = 0.1
Donnees_chart = {
    "x": numpy.arange(-5,6,0.1),
    "y": (fct(x,n) for x in numpy.arange(-5,6, RESOLUTION)),
}
print(f"Donnees_chart:\n{Donnees_chart}")
data_chart = pandas.DataFrame(Donnees_chart)
# Donnees_chart:
# {'x': array([-5.00000000e+00, -4.90000000e+00, -4.80000000e+00, -4.70000000e+00,
#        -4.60000000e+00, -4.50000000e+00, -4.40000000e+00, -4.30000000e+00,
#        -4.20000000e+00, -4.10000000e+00, -4.00000000e+00, -3.90000000e+00,...
#          5.20000000e+00,  5.30000000e+00,
#         5.40000000e+00,  5.50000000e+00,  5.60000000e+00,  5.70000000e+00,
#         5.80000000e+00,  5.90000000e+00]), 'y': <generator object <genexpr> at 0x000001B7DCADEF90>}
 
start = -5
labels = []
 # calcul des labels

# Nb de points:110
nb_total_de_points = len(numpy.arange(-5,6, RESOLUTION))

print(f"Nb de points:{nb_total_de_points}")

for i in range(nb_total_de_points):
    labels.append( (i, start) )
    start += RESOLUTION

print(f"labels:\n{labels}")
# [(0, -5), (1, -4.9), (2, -4.800000000000001), (3, -4.700000000000001), (4, -4.600000000000001), (5, -4.500000000000002), (6, -4.400000000000002), (7, -4.3000000000000025), (8, -4.200000000000003), (9, -4.100000000000003), (10, -4.0000000000000036), (11, -3.9000000000000035), (12, -3.8000000000000034), (13, -3.7000000000000033), (14, -3.600000000000003), (15, -3.500000000000003), (16, -3.400000000000003), (17, -3.300000000000003), (18, -3.200000000000003), (19, -3.1000000000000028), (20, -3.0000000000000027), (21, -2.9000000000000026), (22, -2.8000000000000025), (23, -2.7000000


#table des labels:
 
table_des_labels = dict( (x,y) for x,y in labels)

print(f"table_des_labels:\n{table_des_labels}")
# {0: -5, 1: -4.9, 2: -4.800000000000001, 3: -4.700000000000001, 4: -4.600000000000001, 5: -4.500000000000002, 6: -4.400000000000002, 7: -4.3000000000000025, 8: -4.200000000000003, 9: -4.100000000000003, 10: -4.0000000000000036, 11: -3.9000000000000035, 12: -3.8000000000000034, 13: -3.7000000000000033, 14: -3.600000000000003, 15: -3.500000000000003, 16: -3.400000000000003, 17: -3.300000000000003, 18: -3.200000000000003, 19: -3.1000000000000028, 20: -3.0000000000000027, 21: -2.9000000000000026, 22: -2.8000000000000025, 23: -2.70000000000000..

data_chart = data_chart.rename(index =  table_des_labels)
#Dessin de courbes
st.line_chart(data_chart)



