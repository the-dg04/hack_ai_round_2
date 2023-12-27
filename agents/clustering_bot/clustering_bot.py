from uagents import Agent,Context,Model
from uagents.setup import fund_agent_if_low

clustering_bot=Agent(name="clustering_bot",seed="clustering_bot",port=8071,endpoint=["http://127.0.0.1:8071/submit"])
fund_agent_if_low(clustering_bot.wallet.address())