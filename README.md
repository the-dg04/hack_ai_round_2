# hack_ai_round_2
Installation
1. Run the following command to install the required packages
`pip install -r requirements.txt`
2. Write the job description into agents/IO_bot/job_description.txt according to which the filtering is to be done.
3. Save all the PDFs of the resumes into the agents/IO_bot/input_resumes folder
4. Run main.py
5. That's it! Now you will receive the compolete



For our approach to the problem statement we use the flow of the following uAgents 

IObot: This uAgent handles all of the input_operations and output_operations.
IObot is the first agent that is initialised on startup, and communicates with the Streamlit interface. It receives the Job Description pdf file and resume files to be filtered from the interface. Thus, the IObot messages these to the pdf_parser_bot

pdf_parser_bot: Upon recieving the PDFs of job description and resumes, this agent helps to parse them and extract the textual information from each of the files.

filtering_bot: This is the where the actual resume screening happens. As We have explained, BERT approach is chosen to generate embeddings for each resume and the job description.
The embeddings of each of the resume is compared to the job description using NLP techniques. 
On the basis of this, the filtering bot sends the message containing the percent_match to the IObot and the score of each is outputted.
thus this completes the whole uAgents chain
