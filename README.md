# hack_ai_round_2
Installation
1. Run the following command to install the required packages
`pip install -r requirements.txt`
2. Write the job description into job_description.txt according to which the filtering is to be done.
3. Save all the PDFs of the resumes into the agents/IO_bot/input resumes folder
4. Now you can Run main.py
5. That's it! Now you will receive the complete ranking of the resumes filtered according to the job description. 


We approached the problem statement by generating scores for each resume corresponding to the job description, where a higher score corresponds to a more suitable candidate. 

First we begin by extracting text from the resume and preprocessing the text for further analysis using nltk.
Text embeddings are generated using pretrained paraphrase-MiniLM-L6-v2. 

To check similarity, we compare the embeddings using cosine similarity and then create a ranking based the cosine similarity scores.


In our approach to the problem statement we use the flow of the following uAgents 

IObot: This uAgent handles all of the input_operations and output_operations.
IObot is the first agent that is initialised on startup, and communicates with the Streamlit interface. It receives the Job Description pdf file and resume files to be filtered from the interface. Thus, the IObot messages these to the pdf_parser_bot

pdf_parser_bot: Upon recieving the PDFs of job description and resumes, this agent helps to parse them and extract the textual information from each of the files.

filtering_bot: This is the where the actual resume screening happens. As We have explained, BERT approach is chosen to generate embeddings for each resume and the job description.
The embeddings of each of the resume is compared to the job description using NLP techniques. 
On the basis of this, the filtering bot sends the message containing the percent_match to the IObot and the score of each is outputted.
thus this completes the whole uAgents chain
