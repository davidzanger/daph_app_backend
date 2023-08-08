import openai

openai.api_key = ""


def imagine_text(
    difficulty_grammar: int,
    difficulty_vocabulary: int,
    n_words: int,
    topic: str,
    considered_words: str,
    language: str,
) -> str:
    if topic != "" or topic == "None":
        topic_text = f'with the topic of "{topic}"'
    else:
        topic_text = ""

    message = (
        f"I want you to act as a leggendary story teller. Write a captivating and interesting story about {topic_text} in {language} language. The difficulty of the grammar on scale from 0 to 5 must be {difficulty_grammar} and the difficulty of"
        f" the vocabulary on scale from 0 to 5 must be {difficulty_vocabulary}. Write {n_words} words (plus or minus 10 percent). You must include the following words: "
        f'"{considered_words}". Do not write any explanations.'
    )
    # f'Additionally generate instructions for the Dall-E Model from OpenAI to generate pictures to accompany the text for better understanding. ' \
    # f'Do generate exactly 2 pictures in comic book style. Separate the text from the image generating instructions for Dall-E by <TEXTSEPARATOR> and separate every image generating instruction' \
    # f'by <INSTRUCTIONSEPARATOR>. Just write the pure text and the pure instructions, dont write anything else in your answer.'
    print(message)
    messages = [{"role": "user", "content": message}]
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    chatgpt_reply = chat.choices[0].message.content
    print(chatgpt_reply)
    return chatgpt_reply