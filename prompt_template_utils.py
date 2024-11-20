"""
This file implements prompt template for llama based models. 
Modify the prompt template based on the model you select. 
This has significant impact on the output of the LLM.
"""

from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

# this is specific to Llama-2.

system_prompt = """You are a helpful assistant, you will use the provided context to answer user questions.
Read the given context before answering questions and think step by step.

Analyze the content of the provided emails to classify it into one of three categories based on the emotional content and the nature of the inquiry. The email content will be supplied from the source_documents. Use the criteria provided to guide your classification:

1. **Processing**: For emails that express a 'neutral' tone or any other emotions not specified in the other categories. This includes general updates, information requests, or any email not fitting into 'Closed' or 'Contact Centre' categories.

2. **Closed**: For emails expressing 'gratitude', typically thank you messages or emails showing appreciation.

3. **Contact Centre**: For emails driven by 'curiosity', characterized by questions or inquiries seeking more information or clarification.

Criteria for analysis:
- Identify key phrases, questions, or expressions of gratitude within the source document.
- Consider the overall tone of the email: neutral, inquisitive, or appreciative.
- Pay attention to explicit questions that indicate 'curiosity'.
- Look for expressions of thanks or appreciation to identify 'gratitude'.

The content of the email will be automatically provided from the source documents associated with this task. Based on the analysis, classify the email into 'Processing', 'Closed', or 'Contact Centre'. Provide a brief justification for your classification, referencing specific aspects of the email that align with the criteria outlined above."
"""


def get_prompt_template(system_prompt=system_prompt, promptTemplate_type=None, history=False):
    if promptTemplate_type == "llama":
        B_INST, E_INST = "[INST]", "[/INST]"
        B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"
        SYSTEM_PROMPT = B_SYS + system_prompt + E_SYS
        if history:
            instruction = """
            Context: {history} \n {context}
            User: {question}"""

            prompt_template = B_INST + SYSTEM_PROMPT + instruction + E_INST
            prompt = PromptTemplate(input_variables=["history", "context", "question"], template=prompt_template)
        else:
            instruction = """
            Context: {context}
            User: {question}"""

            prompt_template = B_INST + SYSTEM_PROMPT + instruction + E_INST
            prompt = PromptTemplate(input_variables=["context", "question"], template=prompt_template)
    elif promptTemplate_type == "mistral":
        B_INST, E_INST = "<s>[INST] ", " [/INST]"
        if history:
            prompt_template = (
                B_INST
                + system_prompt
                + """
    
            Context: {history} \n {context}
            User: {question}"""
                + E_INST
            )
            prompt = PromptTemplate(input_variables=["history", "context", "question"], template=prompt_template)
        else:
            prompt_template = (
                B_INST
                + system_prompt
                + """
            
            Context: {context}
            User: {question}"""
                + E_INST
            )
            prompt = PromptTemplate(input_variables=["context", "question"], template=prompt_template)
    else:
        # change this based on the model you have selected.
        if history:
            prompt_template = (
                system_prompt
                + """
    
            Context: {history} \n {context}
            User: {question}
            Answer:"""
            )
            prompt = PromptTemplate(input_variables=["history", "context", "question"], template=prompt_template)
        else:
            prompt_template = (
                system_prompt
                + """
            
            Context: {context}
            User: {question}
            Answer:"""
            )
            prompt = PromptTemplate(input_variables=["context", "question"], template=prompt_template)

    memory = ConversationBufferMemory(input_key="question", memory_key="history")

    return (
        prompt,
        memory,
    )
