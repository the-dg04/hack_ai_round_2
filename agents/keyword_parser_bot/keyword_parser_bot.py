from uagents import Agent,Context,Model
from uagents.setup import fund_agent_if_low
import sys
sys.path.append("../../")
from utils.utils import get_bot_address

class TextToKeywordsModel(Model):
    content:str
    job_description:str

class KeywordsToMatchModel(Model):
    keywords:str
    job_description:str

keyword_parser_bot=Agent(name="keyword_parser_bot",seed="keyword_parser_bot",port=8073,endpoint=["http://127.0.0.1:8073/submit"])
fund_agent_if_low(keyword_parser_bot.wallet.address())

@keyword_parser_bot.on_message(model=TextToKeywordsModel)
async def pdf_to_text(ctx: Context, sender: str, msg: TextToKeywordsModel):
    content=msg.content

    # convert text to keywords

    keywords="sample keywords"
    await ctx.send(get_bot_address("filtering_bot"),KeywordsToMatchModel(content,msg.job_description))