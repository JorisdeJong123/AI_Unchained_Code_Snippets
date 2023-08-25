from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from prompts import PROMPT_IMPROVER_PROMPT

initial_prompt = "Generate a workout schedule"

# Initialize LLM
openai_api_key = "YOUR_OPENAI_API_KEY"
llm = ChatOpenAI(openai_api_key=openai_api_key, model="gpt-3.5-turbo-16k", temperature=0.4)

# Initialize LLMChain
prompt_improver_chain = LLMChain(llm=llm, prompt=PROMPT_IMPROVER_PROMPT)

# Run LLMChain
improved_prompt = prompt_improver_chain.run(initial_prompt)
print(improved_prompt)