from uagents import Bureau, Context
from agents.IO_bot.IO_bot import IO_bot
from agents.pdf_parser_bot.pdf_parser_bot import pdf_parser_bot 
from agents.keyword_parser_bot.keyword_parser_bot import keyword_parser_bot
from agents.filtering_bot.filtering_bot import filtering_bot

if __name__ == "__main__":
    bureau = Bureau(endpoint=["http://127.0.0.1:8069/submit"], port=8069) # Create a bereau to manage bot interaction
    
    print(f"Activating {IO_bot.name}")
    bureau.add(IO_bot) 
    print(f"Activating {pdf_parser_bot.name}")
    bureau.add(pdf_parser_bot) 
    print(f"Activating {keyword_parser_bot.name}")
    bureau.add(keyword_parser_bot) 
    print(f"Activating {filtering_bot.name}")
    bureau.add(filtering_bot) 
    bureau.run() # Run the bereau
