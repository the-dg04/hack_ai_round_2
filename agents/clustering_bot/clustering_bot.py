from uagents import Agent,Context,Model
from uagents.setup import fund_agent_if_low
import sys
sys.path.append("../../")
from utils.utils import get_bot_address

class ResumeMessage(Model):
    resume_address:str
    job_description:str

class PercentMatchModel(Model):
    percent_match:int

clustering_bot=Agent(name="clustering_bot",seed="clustering_bot",port=8071,endpoint=["http://127.0.0.1:8071/submit"])
fund_agent_if_low(clustering_bot.wallet.address())

@clustering_bot.on_message(model=ResumeMessage)
async def match_resume(ctx: Context, sender: str, msg: ResumeMessage):
    parsed_text=msg.resume_address
    job_desc=msg.job_description

    # calculate percent match

    percent_match=69
    await ctx.send(get_bot_address("IO_bot"),PercentMatchModel(percent_match))