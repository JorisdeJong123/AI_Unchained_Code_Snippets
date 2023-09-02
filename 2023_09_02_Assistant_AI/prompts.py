from langchain.prompts import PromptTemplate

# Create a prompt template to be used in the chain.

template = """

    You are a management assistant who writes meeting minutes. You always manage to capture the important points.

    Below you will find a transcript of a recorded meeting.

    This report needs to be clearly and concisely written in English. 
    
    Please conclude with action points at the bottom. 
    
    Also, provide suggestions for topics to discuss in the next meeting.

    Transcript:
    ----------------
    {transcript}
    ----------------

    Response in markdown:

    """

prompt = PromptTemplate(
        input_variables=["transcript"],
        template=template,
    )