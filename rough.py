# from config.model_config import load_config

# cfg = load_config()

# print(cfg.model);
# print(cfg.debugging_app);

# -----------------------------------------

# test-> llm_client.py

# from utils.llm_client import GeminiClient

# client = GeminiClient()

# print(client.ask("What is capital of newzland"))

# ---------------------------------------------

# import json
# from utils.llm_client import GeminiClient
# from pathlib import Path

# prompt_path=Path("utils/prompts/debugging_prompt.json")
# data = json.loads(prompt_path.read_text())

# system_instruction=data["system_instruction"]
# template=data["user_prompt_template"]

# user_input="print(Hello Wrold)"

# prompt = system_instruction + '\n\n' + template.replace("{{USER_INPUT}}",user_input)

# client=GeminiClient()

# print(client.ask(prompt))


# -----------------------------------------

from utils.debugging_helper import build_debugging_prompt
from utils.llm_client import GeminiClient

client=GeminiClient()

user_code='''class Main{

public void main(String[] args){

}

}'''

prompt=build_debugging_prompt(user_code)

result=client.ask(prompt)

print(result)
