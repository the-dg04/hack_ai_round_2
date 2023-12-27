from uagents import Agent,Context,Model
from uagents.setup import fund_agent_if_low

IO_bot=Agent(name="IO_bot",seed="IO_bot",port=8070,endpoint=["http://127.0.0.1:8070/submit"])
fund_agent_if_low(IO_bot.wallet.address())