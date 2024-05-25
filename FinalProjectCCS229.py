#Angelica Villar BSCS3A
#Final Project in Intelligent Systems (CCS229)

import streamlit as st
import openai

#OpenAI API and Streamlit libraries
openai.api_key = "cm-mZ56JoBm83JbRA1ifrEPiEneT1dDkdOsBoEybn5RCepYdyKfiZT5j1d9emso9wU3"
st.set_page_config(layout="wide")

#Define the multi-level prompting system
prompts = [
    {"prompt": "Please provide a creative idea for a new product.", 
     "options": ["A new smart home device", "A sustainable fashion line", "A innovative kitchen gadget"]},
    {"prompt": "Please choose one of the following options: ",
     "options": ["A new smart home device", "A sustainable fashion line", "A innovative kitchen gadget"]}
]

#Define the GPT-3 API integration
gpt3_model = "text-davinci-003"

#Define the main function
def main():
    #Guide the user through the prompting process
    for i, prompt in enumerate(prompts):
        st.write(f"**Level {i+1}**")
        st.write(f"{prompt['prompt']}")
        selected_option = st.selectbox("Select an option:", prompt["options"])
        st.write(f"Selected option: {selected_option}")

        #Integrate the GPT-3 API to generate creative text formats
        response = openai.Completion.create(
            model=gpt3_model,
            prompt=selected_option,
            max_length=200,
            temperature=0.5,
            top_p=0.9,
            frequency_penalty=0.5,
            presence_penalty=0.5
        )
        generated_text = response.choices[0].text

        #Display the generated creative text
        st.write(f"**Generated Text:**")
        st.write(generated_text)

        #Refine the generated text based on user input
        refine_text = st.text_area("Refine the generated text:")
        refine_response = openai.Completion.create(
            model=gpt3_model,
            prompt=refine_text,
            max_length=200,
            temperature=0.5,
            top_p=0.9,
            frequency_penalty=0.5,
            presence_penalty=0.5
        )
        refined_text = refine_response.choices[0].text

        #Display the refined text
        st.write(f"**Refined Text:**")
        st.write(refined_text)

if __name__ == "__main__":
    main()