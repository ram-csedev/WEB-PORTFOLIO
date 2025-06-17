import streamlit as st
st.set_page_config(layout="wide")
col1,col2 = st.columns(2)

with col1:
    st.image('image/ram.JPG')
with col2:
    st.title('RAM')
    content="""
    Hi, I'm Ram Nachiappan. I recently completed Class 12 and got admission into the B.Tech Computer Science and Engineering program at VIT Chennai. I'm passionate about technology and coding, and I'm currently working on a menu-driven Python project with a MySQL backend related to the medical field. I like to take a slow and steady approach to learning, making sure I truly understand what I'm studying. I'm also interested in health and natural remedies, and I enjoy learning about ingredients in my own language, Tamil. I'm someone who likes asking questions—whether it's about academics, life, or culture—because I believe curiosity leads to growth. I'm excited to explore new ideas, improve my skills, and make the most of my time in college.
    """
    st.info(content)
content2='''
here there Below are some of the apps that i have created with the help of python.Feel free to contact me teehee
'''
st.write(content2)