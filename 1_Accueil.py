import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline
from constant import *
import base64
# from PIL import Image
# st.set_page_config(page_title='Portfolio Quentin BERNARDIN' ,layout="wide",page_icon='')

# -----------------  loading assets  ----------------- #
# photo = Image.open("images/.jpg")
# st.sidebar.image(photo)
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/quentin-bernardin)",unsafe_allow_html=True)
st.sidebar.markdown("[Profil GitHub](https://github.com/Phebos)",unsafe_allow_html=True)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")

# loading assets
python_lottie = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json")
java_lottie = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_zh6xtlj9.json")
my_sql_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_w11f2rwn.json")
git_lottie = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_03cuemhb.json")
github_lottie = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_6HFXXE.json")
docker_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_35uv2spq.json")
dashboard_lottie = load_lottieurl("https://lottie.host/14c4fe8e-b42a-47a8-97d0-b105ea0e3a92/vl3raV3lVg.json")
ai_lottie = load_lottieurl("https://lottie.host/f298238b-ae7e-4261-9638-9758a53a6f18/4O0vupqg55.json")

# ----------------- info ----------------- #
st.markdown(f'<h1 style="text-align:center;background-color: #90ADC6;font-size:60px;border-radius:2%;">'
            f'<span style="color:#444444;">Bonjour ! Je suis {info['Full_Name']}👋</span><br>'
            f'<span style="color:#444444;font-size:17px;">{info["Intro"]}</span></h1><br>', 
            unsafe_allow_html=True)
st.write("")
st.markdown(f'<div style="text-align: justify;">{info['About']}</div>', unsafe_allow_html=True)


with open("images/Programme_Data_IA_Engineer.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    
st.markdown(f'<a href="data:application/octet-stream;base64,{base64_pdf}" download="Programme_Data_IA_Engineer.pdf">Télécharger le programme de l\'alternance</a>', unsafe_allow_html=True)    
        

# ----------------- skillset ----------------- #
with st.container():
    st.subheader('⚒️ Compétences')
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st_lottie(python_lottie, height=100,width=100, key="python", speed=2.5)
    with col2:
        st_lottie(java_lottie, height=100,width=100, key="java", speed=4)
    with col3:
        st_lottie(my_sql_lottie,height=100,width=100, key="mysql", speed=2.5)
    with col4:
        st_lottie(git_lottie,height=100,width=100, key="git", speed=2.5)
    with col1:
        st_lottie(github_lottie,height=80,width=80, key="github", speed=2.5)
    with col2:
        st_lottie(docker_lottie,height=120,width=120, key="docker", speed=2.5)
    with col3:
        st_lottie(dashboard_lottie,height=160,width=160, key="dashboard", speed=2.5)
    with col4:
        st_lottie(ai_lottie,height=100,width=100, key="ai", speed=1)
    
    
# ----------------- timeline ----------------- #
with st.container():
    st.markdown("""""")
    st.subheader('📌 Carrière')

    # load data
    with open('career.json', "r") as f:
        data = f.read()

    # render timeline
    timeline(data, height=400)


# -----------------  contact  ----------------- #
    with st.container():
        st.subheader("📨 Me Contacter")
        contact_form = f"""
        <form action="https://formsubmit.co/efa64dc617759b22296de0784f30c16e" method="POST">
            <input type="hidden" name="_captcha value="false">
            <input type="text" name="name" placeholder="Nom" required>
            <input type="email" name="email" placeholder="Email" required>
            <textarea name="message" placeholder="Message" required></textarea>
            <button type="submit">Envoyer</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
