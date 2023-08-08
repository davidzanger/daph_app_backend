import json
from typing import Any, Dict, List
from langapp.gpt_generator import imagine_text

import uvicorn
from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

from enum import Enum, auto


class AutoName(Enum):

    # Overrides the auto() function to automatically set the value of the enum
    # variable to the string name.
    @staticmethod
    def _generate_next_value_(name: str, start, count, last_values):
        return name.lower()


class Difficulty(str, AutoName):
    EASY = auto()
    MEDIUM = auto()
    HARD = auto()


class GenerateTextRequest(BaseModel):
    words: list[str] = ['']
    textLength: int = 500
    difficulty: Difficulty = Difficulty.EASY
    generateText: str = ''


# NOTE: You can use this for debugging.
# @app.post("/generate_text/")
# async def create_item(item: Request):
#     json_raw = await item.json()
#     print(json_raw)
#     return {"generatedText": f'{item}'}


@app.post("/generate_text/")
async def create_item(item: GenerateTextRequest):

    if item.difficulty is Difficulty.EASY:
        difficulty_grammar = 0
        difficulty_vocabulary = 0
    elif item.difficulty is Difficulty.MEDIUM:
        difficulty_grammar = 2
        difficulty_vocabulary = 2
    else:
        difficulty_grammar = 5
        difficulty_vocabulary = 5

    item.generateText = imagine_text(difficulty_grammar=difficulty_grammar, difficulty_vocabulary=difficulty_vocabulary, n_words=item.textLength, topic='', considered_words=' '.join(item.words), language='english')


    return {"generatedText": f'{item}'}


@app.get("/")
async def root():

    return {"words": ['This text actually comes from a python backend!',]}


if __name__ == '__main__':
    uvicorn.run('main:app')
    # json_raw = '{"words": [], "textLength": "0", "difficulty": "medium", "generatedText": ""}'
    # print(json_raw)
    # user_dict = json.loads(json_raw)
    # user = GenerateTextRequest(**user_dict)
    # print(user)