#Angelica Villar BSCS3A
#Final Project in Intelligent Systems (CCS229)

import streamlit as st
import openai


#OpenAI API and Streamlit libraries
openai.api_key = "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"
st.set_page_config(layout="wide")

#Define the Streamlit app
def app():
    st.title('Final Project in Intelligent Systems')
    st.write('by Angelica Villar of BSCS3A')

#Define the multi-level prompting system
prompts = [
    {"prompt": "Please provide a creative idea for the coffee shop upgrade.", 
     "options": ["A new vegan coffee", "A limited edition recycled cup", "An innovative kitchen gadget for easy access of orders"]},
    {"prompt": "Please choose one of the following options: ",
     "options": ["A new vegan coffee", "A limited edition recycled cup", "An innovative kitchen gadget for easy access of orders"]}
]

#Define the GPT-3 API integration
gpt3_model = "text-davinci-003"

#Define the main function
def main():
    #Guide the user through the prompting process
    for i, prompt in enumerate(prompts):
        st.write(f"**Idea**")
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
