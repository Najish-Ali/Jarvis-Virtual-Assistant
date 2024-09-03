from openai import OpenAI
import os

# Function Definition
def ai_process(command):
    """
        Process a command using OpenAI's GPT-3.5-turbo model.
    
        Args:
        command (str): The user's input command to be processed by the AI.

        Returns:
        str: The AI's response to the command.
    """
    # Retrieve the API key from environment variables
    api_key = os.environ.get('OPENAI_API_KEY')
    
    # Checks if the API key is not present and raises an exception if it's missing
    if not api_key:
        raise ValueError("OpenAI API key not found in environment variables.")
    
    # Sets the API key for authentication with the OpenAI API.
    OpenAI.api_key = api_key

    try:
        # Generate AI response using the Davinci model
        response = OpenAI.Completion.create(
            model="text-davinci-003",  # Specify the Davinci model to use
            prompt=command,  # The user's command as the input prompt
            max_tokens=150,  # Limit the number of tokens in the response
            temperature=0.7,  # Controls the randomness of the output (0.0 is more deterministic, 1.0 is more random)
            top_p=1.0,  # Controls the diversity of the output (1.0 means no cutoff)
            n=1  # Number of responses to generate
        )
        
        # Extract and return the content of the response
        message = response.choices[0].text.strip()  # Access the text from the response and remove extra whitespace
        return message

    except OpenAI.OpenAIError as e:
        # Handle errors specific to the OpenAI API (e.g., rate limits, invalid requests)
        print(f"OpenAI API error: {e}")  # Print the error for debugging
        return "Sorry, I encountered an error while processing your request."  # Return a user-friendly error message

    except Exception as e:
        # Handle any other unexpected errors that may occur
        print(f"An unexpected error occurred: {e}")  # Print the error for debugging
        return "Sorry, something went wrong."  # Return a user-friendly error message
