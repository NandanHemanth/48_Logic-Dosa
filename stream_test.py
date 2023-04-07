import streamlit as st
import subprocess

# Set up the app layout
st.set_page_config(page_title="EDUMIZE", page_icon=":books:")
st.title("EDUMIZE")
st.header("By Logic Dosa\n")

def open_file(url):
    with open(url, "r") as file:
        file_contents = file.read()
    return file_contents

def open_file1(text):
    with open(text, 'r') as file:
        file_contents = file.read()
    return file_contents

st.markdown("Welcome to EDUMIZE, an educational app that provides various tools for learning.")

menu = ["Visual Learning", "Text Summarizer", "MCQ Generator", "Study Room"]
choice = st.sidebar.selectbox("Select a tool:", menu)

if choice == "Visual Learning":
    st.subheader("Visual Learning")
    if st.button("Run A* Algorithm"):
        subprocess.run(["python", "astar.py"])
elif choice == "Text Summarizer":
    st.subheader("Text Summarizer")
    text = st.text_area("Enter Text:", height=10)
    if st.button("Run Text Summarizer"):
        import summary
        summary.main1(text)
    if st.button("Print File"):
        text="summarized.txt"
        file_contents = open_file1(text)
        st.text(file_contents)
elif choice == "MCQ Generator":
    st.subheader("MCQ Generator")
    url = st.text_input("Enter Path To File:")
    if st.button("Run"):
        import mcqg
        mcqg.main(url)
    if st.button("Open File"):
        url = "mcq.txt"
        file_contents = open_file(url)
        st.text(file_contents)
    if st.button("Show File Answers"):
        url = "mcq_ans.txt"
        file_contents = open_file(url)
        st.text(file_contents)
elif choice == "Study Room":
    st.subheader("Study Room")
    container = st.container()
    with container:
        if st.button("Video Chat 1"):
            subprocess.run(["python", "video_chat1.py"])
        if st.button("Video Chat 2"):
            subprocess.run(["python", "video_chat2.py"])
