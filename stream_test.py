import streamlit as st
import subprocess

if st.button('Run A* Algorithm'):
    subprocess.run(['python', 'astar.py'])

url = st.text_input('Enter Path To File:')
#command = ['python','mcqg.py','--url',url]
print(url)
if st.button('Run'):
    import mcqg
    mcqg.main(url)

def open_file(url):
    with open(url, 'r') as file:
        file_contents = file.read()
    return file_contents

if st.button('Open File'):
    url='mcq.txt'
    file_contents=open_file(url)
    st.text(file_contents)

if st.button('Show File Answers'):
    url='mcq_ans.txt'
    file_contents=open_file(url)
    st.text(file_contents)

if st.button('Video Chat 1'):
    subprocess.run(['python','video_chat1.py'])

if st.button('Video Chat 2'):
    subprocess.run(['python','video_chat2.py'])