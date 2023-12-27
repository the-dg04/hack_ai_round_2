from uagents import Agent

def get_bot_address(bot_seed):
    agent=Agent(seed=bot_seed)
    return agent.address