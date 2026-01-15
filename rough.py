# from config.model_config import load_config

# cfg = load_config()

# print(cfg.model);
# print(cfg.debugging_app);

# -----------------------------------------

# test-> llm_client.py

from utils.llm_client import GeminiClient

client = GeminiClient()

print(client.ask("What is capital of newzland"))