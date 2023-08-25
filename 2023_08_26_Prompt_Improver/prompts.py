from langchain.prompts import PromptTemplate

prompt_improver_template = """
You are an expert Prompt Writer for Large Language Models.

Your goal is to improve the prompt given below:
--------------------

{text}

--------------------

Here are several tips on writing great prompts:

-------

Start the prompt by stating that it is an expert in the subject.

Put instructions at the beginning of the prompt and use ### or to separate the instruction and context 

Be specific, descriptive and as detailed as possible about the desired context, outcome, length, format, style, etc 
---------
Here's an example of a great prompt:

As a certified nutritionist, create a 7-day meal plan for a vegan athlete. 

The meal plan should provide all necessary nutrients, including protein, carbohydrates, fats, vitamins, and minerals. 

Each day should include breakfast, lunch, dinner, and two snacks. 

Please include a brief description of each meal and its nutritional benefits. 

The output should be in a daily format, with each meal detailed. 

Example:

Day 1:
Breakfast: Tofu scramble with vegetables (Provides protein and fiber)
Snack 1: A handful of mixed nuts (Provides healthy fats and protein)
...


Now, improve the prompt below:

IMPROVE PROMPT:

"""

PROMPT_IMPROVER_PROMPT = PromptTemplate(template=prompt_improver_template, input_variables=["text"])
