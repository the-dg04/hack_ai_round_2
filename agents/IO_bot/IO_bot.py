from uagents import Agent,Context,Model
from uagents.setup import fund_agent_if_low
import sys
sys.path.append("../../")
from utils.utils import get_bot_address

class ResumeMessage(Model):
    resume_address:str
    job_description:str

IO_bot=Agent(name="IO_bot",seed="IO_bot",port=8070,endpoint=["http://127.0.0.1:8070/submit"])
fund_agent_if_low(IO_bot.wallet.address())

@IO_bot.on_event("startup")
async def get_input(ctx:Context):
    # get file from ui
    resume_file="Cape-Town-Resume-Template-Retro-Creative.pdf"
    job_description="job description"
    await ctx.send(get_bot_address("pdf_parser_bot"),ResumeMessage(resume_file,job_description))
