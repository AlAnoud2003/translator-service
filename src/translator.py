import openai

def query_llm(post: str) -> tuple[bool, str]:
    # Query the OpenAI API for a response to the post
    try:
        # Assuming `deployment_name` is set to the engine you've deployed
        response = openai.ChatCompletion.create(
            engine="translator-codehers",  # Use your engine/deployment name
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": post}
            ],
            max_tokens=150  # Adjust the token limit if needed
        )

        # Extract the response text from the model's output
        llm_response = response['choices'][0]['message']['content']

        # Evaluate whether the response is coherent and valid
        is_valid = len(llm_response.strip()) > 0  # Check if the response is non-empty

        # Return a tuple (True/False, response text)
        return (is_valid, llm_response)

    except Exception as e:
        # Handle API errors or other exceptions
        print(f"Error querying LLM: {e}")
        return (False, "An error occurred while processing the request.")


############################################################################################################

def query_llm_robust(post: str) -> tuple[bool, str]:
  try:
      response = query_llm(post)  # Assuming query_llm returns a tuple

      if isinstance(response, tuple) and len(response) == 2:
          validity, response_text = response

          if isinstance(validity, bool) and isinstance(response_text, str):
                return response  # Return the valid response as is
          else:
                print("Unexpected format: response elements are not of the expected type.")
                return (False, "Error: Invalid response format")

      else:
           print("Unexpected format: response is not a tuple or has incorrect length.")
           return (False, "Error: Invalid response format")

  except Exception as e:
      print(f"Error querying the model: {e}")
      return (False, "Error: Unable to retrieve response from model")
  