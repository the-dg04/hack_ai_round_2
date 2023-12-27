from uagents import Agent,Context,Model
from uagents.setup import fund_agent_if_low


import sys
sys.path.append("../../")
from utils.utils import get_bot_address

class TextToFilterModel(Model):
    content:str
    job_description:str
    file_name:str

class PercentMatchModel(Model):
    percent_match:float
    file_name:str

filtering_bot=Agent(name="filtering_bot",seed="filtering_bot",port=8071,endpoint=["http://127.0.0.1:8071/submit"])
fund_agent_if_low(filtering_bot.wallet.address())


from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


def text_similarity_bert(text1, text2):
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    embeddings = model.encode([text1, text2])
    similarity_score = cosine_similarity([embeddings[0]], [embeddings[1]])
    return similarity_score[0, 0]


@filtering_bot.on_message(model=TextToFilterModel)
async def match_resume(ctx: Context, sender: str, msg: TextToFilterModel):
    
    job_desc=msg.job_description
    content=msg.content

    # calculate percent match
    similarity = text_similarity_bert(content, job_desc)

    ctx.logger.info(f"recieved {content}")
    percent_match=similarity
    await ctx.send(get_bot_address("IO_bot"),PercentMatchModel(percent_match=percent_match,file_name=msg.file_name))