import os
def get_resumes():
    files=os.listdir(os.path.join(os.getcwd(),"input_resumes"))
    resumes=[]
    for f in files:
        if(f!='job_description.txt'):
            resumes.append(f)
    return resumes

def get_job_description():
    try:
        with open(os.path.join(os.getcwd(),"input_resumes",'job_description.txt'),"r") as f:
          return f.read()
    except:
        return False