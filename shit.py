import streamlit as st 

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("Automated Resume Screening and Matching Agent")


st.caption("""Aim is to Develop an agent that can intelligently
screen and match resumes with job descriptions. The agent should use natural language
processing (NLP) and machine learning techniques to understand the requirements listed in a
job description and evaluate resumes based on these criteria.""")

uploadedJD = st.file_uploader("Upload Job Description", type="pdf")

uploadedResume = st.file_uploader("Upload resume",type="pdf",accept_multiple_files=True)

click = st.button("Process")
print(uploadedJD)

todocomment = '''
try:
    global job_description
    with pdfplumber.open(uploadedJD) as pdf:
        pages = pdf.pages[0]
        job_description = pages.extract_text()
        

except:
    st.write("bro")
    
    
try:
    global resume
    with  pdfplumber.open(uploadedResume) as pdf:
        pages = pdf.pages[0]
        resume = pages.extract_text()
        print(resume)
except:
    st.write("asdfasdf")
'''

#logic
def getResult(JD_txt,resume_txt):
    content = [JD_txt,resume_txt]

    cv = CountVectorizer()

    matrix = cv.fit_transform(content)

    similarity_matrix =  cosine_similarity(matrix)

    match = similarity_matrix[0][1] * 100

    return match


#button 

if click:
    #match = getResult(job_description,resume)
    #match = round(match,2)
    percent_match=100
    file_name="divyansh.pdf"
    text_color="red"
    if(percent_match>=50):
        text_color="blue"
    if(percent_match>=80):
        text_color="green"
    st.write(f"{file_name}\t:{text_color}[{percent_match}% match]")
    percent_match=100
    file_name="divyansh.pdf"
    text_color="red"
    if(percent_match>=50):
        text_color="blue"
    if(percent_match>=80):
        text_color="green"
    st.write(f"{file_name}\t:{text_color}[{percent_match}% match]")
    percent_match=69
    file_name="divyansh.pdf"
    text_color="red"
    if(percent_match>=50):
        text_color="blue"
    if(percent_match>=80):
        text_color="green"
    st.write(f"{file_name}\t:{text_color}[{percent_match}% match]")
    
    
    percent_match=45
    file_name="divyansh.pdf"
    text_color="red"
    if(percent_match>=50):
        text_color="blue"
    if(percent_match>=80):
        text_color="green"
    st.write(f"{file_name}\t:{text_color}[{percent_match}% match]")


