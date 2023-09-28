import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo2.jpeg", width=600)

with col2:
    st.title("Dario Zignale")
    content = """
    I am a junior data analyst with a strong passion for data-driven decision-making. 
    My love for languages and cultures is reflected in my fluency in Italian, English, and Portuguese. 
    Having lived in Malta and the UK, I enjoy exploring new places and embracing diverse cultures. 
    Football, programming, and cooking are my leisure pursuits, while maintaining a healthy lifestyle 
    through fitness activities is crucial to me. I have a deep curiosity for learning, whether it's through books, 
    volunteering, or attending cultural events. 
    My interests reflect a balanced blend of analytical skills and a well-rounded personality.
    """
    st.info(content)

st.write("Below you can find some of the apps i have built in Python. Feel free to contact me!")