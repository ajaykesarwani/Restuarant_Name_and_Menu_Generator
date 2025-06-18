from langchain.chains import SimpleSequentialChain

def generate_restaurant_name_and_items(cuisine):
    # Chain 1: Restaurant Name
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest one fancy name for this. No description"
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name)

    # Chain 2: Menu Items
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="""Suggest some menu items for {restaurant_name}. Return it as a comma-separated string. No Preamble"""
    )

    # Rename input key to match output from first chain
    menu_chain = LLMChain(llm=llm, prompt=prompt_template_items)

    # Simple chain
    overall_chain = SimpleSequentialChain(chains=[name_chain, menu_chain], verbose=True)

    result = overall_chain.run(cuisine)

    # Split result into name + menu manually (hacky but effective for now)
    restaurant_name, menu_items = result.split("\n", 1) if "\n" in result else (result, "")

    return {
        "restaurant_name": restaurant_name.strip(),
        "menu_items": menu_items.strip()
    }
