import streamlit as st
from langchain.llms import Cohere
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain

import os
os.environ["COHERE_API_KEY"] = "M8ELpOX9YoF6xeDgg3bx7DIeUcbMO9yUD1IwH5gM"

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a cuisine:", ("Indian", "American", "Italian", "Mexican", "Arabic"))

def generate_rest_name_items(cuisine):
  llm = Cohere(temperature=0.7)
  prompt_template_name = PromptTemplate(
    input_variables = ['cuisine'],
    template = 'I want to open a restaurant for {cuisine} food. Suggest a fancy name for this.'
  )
  name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key='restau_name')

  prompt_template_items = PromptTemplate(
    input_variables = ['restau_name'],
    template = 'Suggest some menu items for {restau_name}. Return it as comma separated values.'
  )
  food_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key='menu_items')

  # chain = SimpleSequentialChain(chains = [name_chain, food_chain])

  # chain = SequentialChain(
  #   chains = ['restau_name', 'menu_items'],
  #   input_variables = ['cuisine'],
  #   output_variables=['restaurant_name', 'menu_items']
  # )
  # response = chain({'cuisine':cuisine})

  from langchain.chains import SequentialChain

  chain = SequentialChain(
    chains = [name_chain, food_chain],
    input_variables = ['cuisine'],
    output_variables=['restau_name', 'menu_items']
  )

  response = chain({'cuisine':cuisine})
  
  return response

if __name__ == "__main__":
  response = generate_rest_name_items("Italian")
  st.header(response["restau_name"])
  menu_items = response['menu_items'].split(',')
  st.write("--Menu Items--")
  
  for item in menu_items:
    st.write('-', item)
