import streamlit as st
import base64
from constant import *
from PIL import Image
from streamlit_pdf_viewer import pdf_viewer


def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")

# photo = Image.open("images/.jpg")
# st.sidebar.image(photo)
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/quentin-bernardin)",unsafe_allow_html=True)
st.sidebar.markdown("[Profil GitHub](https://github.com/Phebos)",unsafe_allow_html=True)


st.markdown(f'<h1 style="text-align:center;background-color:#90ADC6;font-size:60px;border-radius:2%;">'
            f'<span style="color:#444444;">📝 CV</span></h1>', 
            unsafe_allow_html=True)
st.write("")

# with open("images/resume.pdf","rb") as f:
#       base64_pdf = base64.b64encode(f.read()).decode('utf-8')
#       pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="90%" height="860px" type="application/pdf"></iframe>'
#       st.markdown(f'<div style="text-align: center;">{pdf_display}</div>', unsafe_allow_html=True)    

pdf_viewer("images/resume.pdf")
  
