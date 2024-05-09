import streamlit as st
from korean_menu import make_sidebar
from weasyprint import HTML

st.set_page_config(
    page_title="당신의 AI 심리상담사, 네리",
    page_icon="🧊",
    layout="wide"
)
make_sidebar()
def convert_html_to_pdf(html_content, output_pdf_path):
    html=HTML(string=html_content)
    html.write_pdf(output_pdf_path)

if st.button('try'):
    example_html="<html><body><h1>hi</h1></body></html>"
    output_path="C:/chatbot/tuto1.pdf"
    convert_html_to_pdf(example_html,output_path)
    st.success('done')