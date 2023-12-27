from uagents import Agent,Context,Model
from uagents.setup import fund_agent_if_low



from PyPDF2 import PdfReader
import sys
sys.path.append("../../")
from utils.utils import get_bot_address

class PdfToTextModel(Model):
    resume_address:str
    job_description:str
    file_name:str

class TextToFilterModel(Model):
    content:str
    job_description:str
    file_name:str

pdf_parser_bot=Agent(name="pdf_parser_bot",seed="pdf_parser_bot",port=8072,endpoint=["http://127.0.0.1:8072/submit"])
fund_agent_if_low(pdf_parser_bot.wallet.address())



from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def RemoveStopwords(sentence): 
    stop_words = set(stopwords.words('english'))
    
    word_tokens = word_tokenize(sentence)

    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]

    filtered_sentence = []
    
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    
 
    return filtered_sentence



@pdf_parser_bot.on_message(model=PdfToTextModel)
async def pdf_to_text(ctx: Context, sender: str, msg: PdfToTextModel):
    pdf_file=msg.resume_address
    job_desc=msg.job_description
    # convert pdf to text
    reader = PdfReader(pdf_file)
    page = reader.pages[0]
    transcript  = page.extract_text()
    #cleaning the stopwords and newlines
    resume_cleaned=transcript.replace("\n","")
    description_cleaned=job_desc.replace("\n","")
    resume_cleaned = str(RemoveStopwords(resume_cleaned))
    description_cleaned = str(RemoveStopwords(description_cleaned))

    await ctx.send(get_bot_address("filtering_bot"),TextToFilterModel(content=resume_cleaned,job_description=description_cleaned,file_name=msg.file_name))

