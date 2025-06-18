from langchain_core.prompts import PromptTemplate
from langchain_core.chains import SequentialChain
from langchain.chains import LLMChain 
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    temperature=0.9,
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-70b-versatile"
)

def generate_restaurant_name_and_items(cuisine):
    # Prompt for restaurant name
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest one fancy name for this. No description."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # Prompt for menu items
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest some menu items for {restaurant_name}. Return it as a comma-separated string. No Preamble."
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    # Sequential chain
    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=["cuisine"],
        output_variables=["restaurant_name", "menu_items"],
        verbose=True
    )

    return chain({"cuisine": cuisine})
