import streamlit as st
from matplotlib import image
import os

st.title("Dashboard - Titanic Data")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "titanic.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "titanic.csv")

img = image.imread(IMAGE_PATH)
st.image(img)
class1 = st.selectbox("Select the who:", df['who'].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['who'] == class1], x="fare")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['who'] == class1], y="fare")
col2.plotly_chart(fig_2, use_container_width=True)
