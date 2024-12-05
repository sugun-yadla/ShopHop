#pip install streamlit requests
#download ollama  https://ollama.com/
# install mistral using "ollama pull mistral"
# use "streamlit run recipe_recommender.py" to run the code

import streamlit as st
import requests

def get_recipe_recommendations(ingredients):
    """
    Args:
        ingredients (list)
    
    Returns:
        str: Generated recipe recommendations
    """

    prompt = f"""Please suggest some creative and delicious recipes using the following ingredients: {', '.join(ingredients)}. 
    For each recipe, provide:
    - Recipe name
    - Brief description
    - Key ingredients
    - Simple cooking instructions
    
    Aim for diverse and interesting recipe ideas that make the most of these ingredients."""

    # Ollama API endpoint for generating text
    url = "http://localhost:11434/api/generate"
    
    payload = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }

    try:
        # Send request to Ollama
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an exception for bad responses
        
        # Extract and return the generated text
        return response.json()['response']
    
    except requests.RequestException as e:
        return f"Error generating recipes: {str(e)}"

def main():
    # Set page configuration
    st.set_page_config(page_title="Recipe Recommender", page_icon="🍳")
    
    # Page title and description
    st.title("🍽️ Ingredient-Based Recipe Recommender")
    st.write("Enter the ingredients you have, and get creative recipe suggestions!")

    # Ingredient input
    ingredients_input = st.text_input(
        "Enter ingredients (comma-separated)", 
        placeholder="e.g. chicken, tomatoes, pasta, basil"
    )

    # Recommend button
    if st.button("Get Recipe Recommendations"):
        # Validate input
        if not ingredients_input:
            st.warning("Please enter some ingredients!")
            return

        ingredients = [ing.strip() for ing in ingredients_input.split(',')]

        # Generate and display recommendations
        with st.spinner('Generating delicious recipes...'):
            recommendations = get_recipe_recommendations(ingredients)
    
    
            st.subheader("🥘 Recipe Recommendations")
            st.write(recommendations)

if __name__ == "__main__":
    main()
