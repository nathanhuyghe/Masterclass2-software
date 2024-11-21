import streamlit as st
from chatbot_functies import chatbot_response

def complete_sentence(partial_sentence):
    """
    Generate a sentence completion for the given partial sentence
    
    Args:
        partial_sentence (str): The beginning of a sentence to be completed
    
    Returns:
        str: The completed sentence
    """
    COMPLETION_PROMPT = f"""Complete this sentence creatively and naturally: "{partial_sentence}". 
    Ensure the completion flows well and makes sense in context."""
    return chatbot_response(COMPLETION_PROMPT)

st.set_page_config(page_title="Creative Writing AI", page_icon="✍️")

st.title("🖋️ Creative Writing AI")

# Tabs for different writing modes
tab1, tab2 = st.tabs(["Full Story Generation", "Sentence Completion"])

with tab1:
    st.header("Generate a Full Story")
    form1 = st.form(key="full_story_form")
    with form1:
        AI_concept = st.text_input("Enter a theme you want to write about:", key="story_concept")
        generate_button = form1.form_submit_button("Write Story")
        
        if generate_button:
            with st.spinner('Generating your story...'):
                PROMPT = f"""Write a creative and engaging story about: {AI_concept}"""
                response = chatbot_response(PROMPT)
            st.write(response)

with tab2:
    st.header("Sentence Completion")
    form2 = st.form(key="sentence_completion_form")
    with form2:
        partial_sentence = st.text_input("Start a sentence:", key="partial_sentence")
        complete_button = form2.form_submit_button("Complete Sentence")
        
        if complete_button:
            with st.spinner('Completing your sentence...'):
                completed_sentence = complete_sentence(partial_sentence)
            
            # Display the original start and the completed sentence
            st.markdown(f"**Original Start:** *{partial_sentence}*")
            st.markdown(f"**Completed Sentence:** {completed_sentence}")
            
            # Optional: Add a copy button
            if st.button("Copy Completed Sentence"):
                st.code(completed_sentence)

# Sidebar with writing tips
st.sidebar.header("✍️ Writing Tips")
st.sidebar.markdown("""
- Be specific in your theme or sentence start
- The more context you provide, the better the result
- Experiment with different inputs
- Use the sentence completion for creative writing prompts
""")

# Footer
st.markdown("---")
st.markdown("*Powered by AI Creative Writing Assistant*")