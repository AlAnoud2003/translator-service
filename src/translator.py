import openai
import time
from openai.error import RateLimitError


# Use your actual API Key and Endpoint
openai.api_key = "2gHiOE3kZe8zUYUjM6wrGfqYFC0AVlxgc1B0MnutTXgqujcLnnKuJQQJ99AJACYeBjFXJ3w3AAABACOGo4UE"  # Your API key
# Dont use the entire url!! https://[name-of-your-resource].openai.azure.com/
openai.api_base = "https://hayas-openai-resources.openai.azure.com"  # Your endpoint base URL
openai.api_type = "azure"
openai.api_version = "2024-08-01-preview"

# Use your deployment name
deployment_name = "gpt-4"


def get_translation(post: str) -> str:
    context = "Translate the given text into English. Respond with only the translated text."

    # Try to call the API with retry logic
    retries = 5  # Number of retries
    delay = 5    # Initial delay time

    for attempt in range(retries):
        try:
            response = openai.ChatCompletion.create(
                engine=deployment_name,  # Make sure deployment_name is defined
                messages=[
                    {"role": "system", "content": context},
                    {"role": "user", "content": f"Translate the following text into English: {post}"}
                ]
            )
            result = response.choices[0].message.content.strip()
            return result

        except RateLimitError as e:
            print(f"Rate limit exceeded. Retrying after {delay} seconds... Error: {e}")
            time.sleep(delay)
            delay *= 2  # Exponential backoff: double the delay on each retry

    return "Rate limit exceeded. Please try again later."  # Return a default message after retries are exhausted


def get_language(post: str) -> str:
    context = "Identify whether the given text is in English or a different language. Respond with either 'English' or the language itself only. If it is an unrecognizable language return 'gibberish'"

    # Try to call the API with retry logic
    retries = 5  # Number of retries
    delay = 5    # Initial delay time

    for attempt in range(retries):
        try:
            response = openai.ChatCompletion.create(
                engine=deployment_name,
                messages=[
                    {"role": "system", "content": context},
                    {"role": "user", "content": f"Is the following text in English or Non-English? Text: {post}"}
                ]
            )
            result = response.choices[0].message.content.strip()
            return result

        except openai.error.RateLimitError as e:
            print(f"Rate limit exceeded. Retrying after {delay} seconds... Error: {e}")
            time.sleep(delay)
            delay *= 2  # Exponential backoff: double the delay on each retry
    return "Rate limit exceeded. Please try again later."  # Return a default message after retries are exhausted

#helper function

def response(post):
    llm_repsonse = get_translation(post)
    return llm_repsonse.string()

def translate_content(post: str) -> tuple[bool, str]:
        try: 
            is_valid = False
            if get_language(post) == "English":
                is_valid = True
                return (is_valid, post)
            else:
                is_valid = False
                llm_response = get_translation(post)
                return (is_valid, llm_response)
        
        except Exception as e:
            # Handle API errors or other exceptions
            print(f"Error querying LLM: {e}")
            return (False, "An error occurred while processing the request.")

        #return (is_valid, llm_response)
