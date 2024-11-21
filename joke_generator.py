import streamlit as st
from chatbot_functies import chatbot_response

# Predefined joke themes
JOKE_THEMES = [
    "Animal Jokes",
    "Work/Office Humor",
    "Science Jokes", 
    "Technology Jokes",
    "Food Jokes",
    "Travel Jokes",
    "Sports Jokes",
    "Music Jokes",
    "Relationship Jokes",
    "School/Student Jokes",
    "Movie/TV Jokes",
    "Coding/Programmer Jokes",
    "Political Humor",
    "Dad Jokes",
    "Nerdy/Geek Humor"
]

st.set_page_config(
    page_title="🤣 Joke Generator", 
    page_icon="😂"
)

st.title("🎭 Joke Generator")

# Sidebar for additional controls
st.sidebar.header("🎩 Joke Preferences")
joke_style = st.sidebar.selectbox(
    "Select Joke Style", 
    [
        "Clean/Family-Friendly", 
        "Slightly Edgy", 
        "Pun-based", 
        "Sarcastic", 
        "Witty"
    ]
)

# Main form
form = st.form(key="joke_settings")
with form:
    # Theme selection
    selected_theme = st.selectbox(
        "Choose Joke Theme", 
        JOKE_THEMES
    )
    
    # Complexity slider
    joke_complexity = st.slider(
        "Joke Complexity", 
        min_value=1, 
        max_value=5, 
        value=3,
        help="1 = Simple, 5 = Complex/Sophisticated"
    )
    
    # Generate button
    generate_button = form.form_submit_button("🎲 Generate Joke")

    # Joke generation
    if generate_button:
        with st.spinner('Brewing a hilarious joke...'):
            # Detailed prompt for more specific joke generation
            PROMPT = f"""
            Generate a {joke_style} joke about {selected_theme}. 
            The joke should be approximately complexity level {joke_complexity} out of 5. 
            Ensure the joke is clever and actually funny and also return it in dutch.
            """
            
            response = chatbot_response(PROMPT)
        
        # Display the joke
        st.header("🤣 Here's Your Joke!")
        st.markdown(f"**Theme:** {selected_theme}")
        st.markdown(f"**Style:** {joke_style}")
        st.write(response)

# Fun facts sidebar
st.sidebar.header("😂 Joke Trivia")
trivia_options = [
    "Laughter reduces stress hormones",
    "The average adult laughs 17 times a day",
    "Humor is a sign of intelligence",
    "Laughing burns approximately 10-40 calories"
]
st.sidebar.markdown(f"🌟 Fun Fact: {trivia_options[hash(st.session_state) % len(trivia_options)]}")

# Footer
st.markdown("---")
st.markdown("*Powered by AI Joke Generator*")