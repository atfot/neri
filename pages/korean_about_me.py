import streamlit as st
from korean_menu import make_sidebar
from streamlit import session_state as sss
from security import check
import socket
import urllib.request
from requests import get

st.set_page_config(
    page_title="당신의 AI 심리상담사, 네리",
    page_icon="🧊",
    layout="wide"
)
try:
    del sss.fix_info, sss.auth_email
except:
    pass
make_sidebar()
check('hi')
st.write("개발자의 말 부분임. 나중에 적을 것임")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
local_ip = s.getsockname()[0]
s.close()
st.write(f"Your local IP address is: {local_ip}")
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
st.write(f"Your computer's IP address is: {ip_address}")

def get_public_ip():
    with urllib.request.urlopen('https://api.ipify.org') as response:
        public_ip = response.read().decode('utf8')
    return public_ip

st.write("Public IP Address:", get_public_ip())

ip = get('https://api.ipify.org').text
st.write('My public IP address is: {}'.format(ip))