from uagents import Agent,Context,Model
from uagents.setup import fund_agent_if_low
from input_funcs import get_job_description,get_resumes
import streamlit as st 
import sys
import os
sys.path.append("../../")
from utils.utils import get_bot_address

class PdfToTextModel(Model):
    resume_address:str
    job_description:str
    file_name:str

class PercentMatchModel(Model):
    percent_match:float
    file_name:str

IO_bot=Agent(name="IO_bot",seed="IO_bot",port=8070,endpoint=["http://127.0.0.1:8070/submit"])
fund_agent_if_low(IO_bot.wallet.address())

@IO_bot.on_event("startup")
async def get_input(ctx:Context):
    # get file from ui
    resumes=get_resumes()
    job_description=get_job_description()
    if(job_description):
        for r in resumes:
            resume_file=os.path.join(os.getcwd(),"input_resumes",r)
            file_name=r
            job_description=job_description
            await ctx.send(get_bot_address("pdf_parser_bot"),PdfToTextModel(resume_address=resume_file,job_description=job_description,file_name=file_name))

@IO_bot.on_message(model=PercentMatchModel)
async def display_match(ctx: Context, sender: str, msg: PercentMatchModel):
    percent_match=msg.percent_match
    file_name=msg.file_name
    text_color="red"
    if(percent_match>=50):
        text_color="yellow"
    if(percent_match>=80):
        text_color="green"
    ctx.logger.info(f"percent match for {file_name} is {percent_match}%")
    # st.write(f"{file_name}\t:{text_color}[{percent_match}% match]")
    # print name and percent match