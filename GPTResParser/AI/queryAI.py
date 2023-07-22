from freeGPT import gpt3, gpt4
import sys
import os


project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_dir)


async def askGPT3(query):
    if type(query) is str:
        resp = await gpt3.Completion.create(prompt=query)
        return resp
    return None


async def askGPT4(query):
    if type(query) is str:
        resp = await gpt4.Completion.create(prompt=query)
        return resp
    return None


