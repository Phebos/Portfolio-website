import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
from constant import *

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")

page1 = Image.open("images/page_1.png")
page2 = Image.open("images/page_2.png")
homepage = Image.open("images/homepage.png")
recopage = Image.open("images/recopage.png")
result = Image.open("images/result.png")


# photo = Image.open("images/.jpg")
# st.sidebar.image(photo)
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/quentin-bernardin)",unsafe_allow_html=True)
st.sidebar.markdown("[Profil GitHub](https://github.com/Phebos)",unsafe_allow_html=True)


st.markdown(f'<h1 style="text-align:center;background-color: #90ADC6;font-size:60px;border-radius:2%;">'
            f'<span style="color:#444444;">Portfolio</span></h1>', 
            unsafe_allow_html=True)
st.write("")
# -----------------  WCS P1  -----------------  #
with st.container():
    st.markdown("""""")
    st.subheader("Requêtes SQL et Dashboard Power BI")
    with st.expander('Voir le projet'):
        col1,col2 = st.columns([0.5, 0.5])
        with col1:
            st.image(page1)
            st.image(page2)
        with col2:
            st.markdown('<div style="text-align: justify;">Dans le cadre de notre premier projet au sein de la Wild Code School, une entreprise fictive nous a missioné pour réaliser un tableau de bord à partir des données déjà disponibles dans leur base de donnéee en réalisant des requêtes SQL.<br><br> J\'étais en charge de la partie Ventes au sein de mon groupe, j\'ai donc réalisé des KPI basés sur les ventes au mois et à l\'année en comparaison avec les précédents résultats, ces graphiques étant filtrables par catégorie de produit vendus pour avoir un peu plus de détail et d\'insight sur les ventes.</div>', unsafe_allow_html=True)
    st.markdown(""" <a href={}> <em>🔗 repo Github </a>""".format('https://github.com/Phebos/SQL-querry-and-dashboard'), unsafe_allow_html=True)

    
# ----------------- WCS P2 ----------------- #
with st.container():
    st.markdown("""""")
    st.subheader('Dashboard Tableau, système de recommandation de film et site via le framework Django')
    with st.expander('Voir le projet'):
        col1,col2 = st.columns([0.5, 0.5])
        with col1:
            st.image(homepage)
            st.image(recopage)
            st.image(result)
        with col2:
            st.markdown('<div style="text-align: justify;">Dans le cadre de notre deuxième projet au sein de la Wild Code School, un cinema fictif en perte de vitesse situé dans la Creuse nous a missioné pour créer un système de recommendation de film ainsi qu\'un tableau de bord basé sur notre sélection de film choisis au préalable.<br><br> Nous devions donc dans un premier temps faire un choix sur la sélection de film. Nous avons choisis de mettre en avant le cinéma asiatique au cours de ce projet. Les données ont été récupérées à partir des bases de données imdb et tmdb et enrichies par webscrapping. Elles ont par la suite étés traités en Python à l\'aide de la librairie Panda pour ensuite être exploitable sur Tableau ainsi que le site web réalisé avec le framework Django. Le système de recommendation se base sur un algorithme K-Nearest Neighbors effectué sur les données textuelles préalablement traitées (telles que les genres, mots clés et synopsis) à l\'aide de Natural Language Processing.</div>', unsafe_allow_html=True)

    st.markdown(""" <a href={}> <em>🔗 repo Github </a>""".format('https://github.com/Phebos/movie-recommendation'), unsafe_allow_html=True)

# -----------------  WCS P3  -----------------  #

# --------------  Pipeline ELT  --------------  #
