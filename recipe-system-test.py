import transformers
import torch
import logging

def test_model_availability():
    """
    Test the availability and basic functionality of the Hugging Face model
    """
    try:
        print("Checking Hugging Face Transformers version...")
        print(f"Transformers Version: {transformers.__version__}")
        
        print("\nChecking PyTorch CUDA availability...")
        print(f"CUDA Available: {torch.cuda.is_available()}")
        if torch.cuda.is_available():
            print(f"CUDA Device Name: {torch.cuda.get_device_name(0)}")
        
        print("\nAttempting to load model...")
        generator = transformers.pipeline(
            'text-generation', 
            model='mistralai/Mistral-7B-Instruct-v0.1'
        )
        
        print("\nModel loaded successfully!")
        
        # Quick test generation
        test_prompt = "Suggest a recipe using chicken, rice, and vegetables."
        print("\nTesting model generation...")
        response = generator(test_prompt, max_length=500)
        print("\n--- Generated Recipe Suggestion ---")
        print(response[0]['generated_text'])
        
    except Exception as e:
        print(f"\nError occurred: {e}")
        print("\nTroubleshooting Tips:")
        print("1. Ensure you have latest transformers and torch installed")
        print("2. Check your internet connection")
        print("3. You might need to install additional dependencies")
        print("\nTry these commands:")
        print("pip install --upgrade transformers torch")
        print("pip install accelerate")

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    
    # Run availability test
    test_model_availability()
