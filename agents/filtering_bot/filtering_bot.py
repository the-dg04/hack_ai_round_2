from uagents import Agent,Context,Model
from uagents.setup import fund_agent_if_low
import sys
sys.path.append("../../")
from utils.utils import get_bot_address

class KeywordsToMatchModel(Model):
    keywords:str
    job_description:str
    file_name:str

class PercentMatchModel(Model):
    percent_match:str
    file_name:str

filtering_bot=Agent(name="filtering_bot",seed="filtering_bot",port=8071,endpoint=["http://127.0.0.1:8071/submit"])
fund_agent_if_low(filtering_bot.wallet.address())

@filtering_bot.on_message(model=KeywordsToMatchModel)
async def match_resume(ctx: Context, sender: str, msg: KeywordsToMatchModel):
    keywords=msg.keywords
    job_desc=msg.job_description

    # calculate percent match

    percent_match=69
    await ctx.send(get_bot_address("IO_bot"),PercentMatchModel(percent_match,msg.file_name))