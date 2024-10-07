#from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from dotenv import load_dotenv
import os

load_dotenv()

# Assuming you've set the correct Groq API key in your .env file
from langchain_groq import ChatGroq

llm = ChatGroq(temperature=0.9, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-70b-versatile")

def generate_restaurant_name_and_items(cuisine):
    # Chain 1: Restaurant Name
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest one fancy name for this. No description"
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # Chain 2: Menu Items
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="""Suggest some menu items for {restaurant_name}. Return it as a comma-separated string. No Preamble"""
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    # SequentialChain: Pass restaurant name from first chain to the next
    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', "menu_items"]
    )

    # Execute the chain and return the result
    response = chain({'cuisine': cuisine})

    # Debugging: Print the intermediate outputs
    print(f"Generated restaurant name: {response['restaurant_name']}")
    print(f"Generated menu items: {response['menu_items']}")

    return response

if __name__ == "__main__":
    # Testing with Italian cuisine
    result = generate_restaurant_name_and_items("Italian")
    print(result)
