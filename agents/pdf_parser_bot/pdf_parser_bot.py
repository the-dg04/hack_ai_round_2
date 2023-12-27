from uagents import Agent,Context,Model
from uagents.setup import fund_agent_if_low
import sys
sys.path.append("../../")
from utils.utils import get_bot_address

class PdfToTextModel(Model):
    resume_address:str
    job_description:str
    file_name:str

class TextToKeywordsModel(Model):
    content:str
    job_description:str
    file_name:str

pdf_parser_bot=Agent(name="pdf_parser_bot",seed="pdf_parser_bot",port=8072,endpoint=["http://127.0.0.1:8072/submit"])
fund_agent_if_low(pdf_parser_bot.wallet.address())

@pdf_parser_bot.on_message(model=PdfToTextModel)
async def pdf_to_text(ctx: Context, sender: str, msg: PdfToTextModel):
    pdf_file=msg.resume_address

    # convert pdf to text here
    ctx.logger.info(f"recieved {msg.resume_address}")
    resume_text="sample text"
    await ctx.send(get_bot_address("keyword_parser_bot"),TextToKeywordsModel(content=resume_text,job_description=msg.job_description,file_name=msg.file_name))