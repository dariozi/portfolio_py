import streamlit as st
import pandas


st.set_page_config(layout="wide")
st.title("Dario Zignale")
col1,empty, col2 = st.columns([1.5,0.5, 3.5])

st.divider()
st.write("Below you can find some of the apps i have built in Python. Feel free to contact me!")
st.divider()

with col1:
    st.image("images/photo2.jpeg", use_column_width="auto" )

with col2:

    content = """
With a robust background in international education and a strong technical skill set in statistical programming, 
data visualization, SQL, and data cleaning, I aspire to excel as a junior data analyst. 
    As a former Student Experience Manager and School Manager, I've cultivated expertise in student engagement, 
    communication, and decision-making within the education sector. This experience has honed my problem-solving 
    skills and heightened my awareness of diverse student needs, making me well-prepared to leverage data for 
    informed strategies. My multilingual proficiency in Italian, English, and Portuguese, coupled with a diverse 
    set of interests spanning programming, and cultural exploration, embodies a well-rounded, globally oriented perspective. 

My ambition is to seamlessly merge my data analysis acumen with my passion for enhancing international education, 
    driving innovation, and optimizing student experiences on a global scale.

    """
    st.subheader(content)


col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width=400)
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width=400)
        st.write(f"[Source Code]({row['url']})")
        st.write(f"[Try the app]({row['deployed_link']}")
