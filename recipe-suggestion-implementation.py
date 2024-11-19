import openai  
import json
from typing import List, Dict

class RecipeSuggestionSystem:
    def __init__(self, api_key: str):
        """
        Initialize the recipe suggestion system with AI configuration
        
        Args:
            api_key (str): API key for AI service (OpenAI, Claude, etc.)
        """
        self.ai_client = openai.OpenAI(api_key=api_key)
        
        # Predefined prompt template for recipe suggestions
        self.prompt_template = """
        You are a helpful culinary assistant. Given a list of ingredients, 
        suggest 3-5 recipes that can be prepared using most or all of these ingredients. 
        For each recipe, provide:
        - Recipe name
        - Required ingredients (highlighting what the user already has)
        - Missing ingredients
        - Brief cooking instructions
        - Estimated preparation and cooking time
        
        Ingredients in cart: {ingredients}
        
        Response format should be a JSON with the following structure:
        {{
            "recipes": [
                {{
                    "name": "Recipe Name",
                    "ingredients_available": ["item1", "item2"],
                    "ingredients_missing": ["item3", "item4"],
                    "instructions": "Brief cooking steps...",
                    "prep_time": "X minutes",
                    "cook_time": "Y minutes"
                }}
            ]
        }}
        """
    
    def get_recipe_suggestions(self, cart_ingredients: List[str]) -> Dict:
        """
        Generate recipe suggestions based on cart ingredients
        
        Args:
            cart_ingredients (List[str]): List of ingredients currently in cart
        
        Returns:
            Dict: Parsed recipe suggestions with details
        """
        try:
            ingredients_str = ", ".join(cart_ingredients)
            
            full_prompt = self.prompt_template.format(ingredients=ingredients_str)
            
            # Call AI service
            response = self.ai_client.chat.completions.create(
                model="gpt-3.5-turbo-1106",  
                response_format={"type": "json_object"},
                messages=[
                    {"role": "system", "content": "You are a helpful recipe suggestion assistant."},
                    {"role": "user", "content": full_prompt}
                ]
            )
            
            # Parse the JSON response
            recipes_json = json.loads(response.choices[0].message.content)
            
            return recipes_json
        
        except Exception as e:
            print(f"Error generating recipe suggestions: {e}")
            return {
                "recipes": [],
                "error": str(e)
            }
    
    def validate_recipe_suggestions(self, suggestions: Dict, cart_ingredients: List[str]) -> Dict:
        """
        Additional validation of recipe suggestions
        
        Args:
            suggestions (Dict): AI-generated recipe suggestions
            cart_ingredients (List[str]): Current cart ingredients
        
        Returns:
            Dict: Validated and potentially modified recipe suggestions
        """
        validated_suggestions = {"recipes": []}
        
        for recipe in suggestions.get("recipes", []):
            # Check ingredient availability
            available_ingredients = [
                ing for ing in recipe.get("ingredients_available", []) 
                if ing.lower() in [cart_item.lower() for cart_item in cart_ingredients]
            ]
            
            # Only include recipes with at least some ingredients available
            if available_ingredients:
                recipe["match_percentage"] = len(available_ingredients) / len(recipe.get("ingredients_available", []))
                validated_suggestions["recipes"].append(recipe)
        
        # Sort recipes by match percentage
        validated_suggestions["recipes"] = sorted(
            validated_suggestions["recipes"], 
            key=lambda x: x.get("match_percentage", 0), 
            reverse=True
        )
        
        return validated_suggestions

# Example usage
def main():
    # Initialize the system
    recipe_system = RecipeSuggestionSystem(api_key="your_openai_api_key")
    
    # Simulate a cart of ingredients
    cart_ingredients = ["chicken", "rice", "onions", "garlic", "bell peppers"]
    
    # Get recipe suggestions
    suggestions = recipe_system.get_recipe_suggestions(cart_ingredients)
    
    # Validate and refine suggestions
    validated_suggestions = recipe_system.validate_recipe_suggestions(suggestions, cart_ingredients)
    
    # Display or further process suggestions
    print(json.dumps(validated_suggestions, indent=2))

if __name__ == "__main__":
    main()
