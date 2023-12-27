from uagents import Agent,Context,Model
from uagents.setup import fund_agent_if_low

pdf_parser_bot=Agent(name="pdf_parser_bot",seed="pdf_parser_bot",port=8072,endpoint=["http://127.0.0.1:8072/submit"])
fund_agent_if_low(pdf_parser_bot.wallet.address())