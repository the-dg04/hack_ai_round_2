from uagents import Bureau, Context
from agents.IO_bot.IO_bot import IO_bot
from agents.pdf_parser_bot.pdf_parser_bot import pdf_parser_bot 
from agents.clustering_bot.clustering_bot import clustering_bot

if __name__ == "__main__":
    bureau = Bureau(endpoint=["http://127.0.0.1:8069/submit"], port=22095) # Create a bereau to manage bot interaction
    
    print(f"Activating {IO_bot.name}")
    bureau.add(IO_bot) 
    print(f"Activating {pdf_parser_bot.name}")
    bureau.add(pdf_parser_bot) 
    print(f"Activating {clustering_bot.name}")
    bureau.add(clustering_bot) 
    bureau.run() # Run the bereau



