from uagents import Agent,Context,Model
from uagents.setup import fund_agent_if_low
import sys
sys.path.append("../../")
from utils.utils import get_bot_address

class PdfToTextModel(Model):
    resume_address:str
    job_description:str
    file_name:str

dummy=Agent(name="sdfdf")
fund_agent_if_low(dummy.wallet.address())
@dummy.on_event("startup")
async def send_message(ctx:Context):
    await ctx.send(get_bot_address("pdf_parser_bot"),PdfToTextModel(resume_address="resume_file",job_description="job_description",file_name="file_name"))


if __name__=="__main__":
    dummy.run()