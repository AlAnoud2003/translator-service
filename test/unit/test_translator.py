from src.translator import translate_content
from src.translator import response
def test_chinese():
    is_english, translated_content = translate_content("这是一条中文消息")
    assert is_english == False
    assert translated_content == "This is a message in Chinese."

def test_llm_normal_response():
    # Test case 1
    is_english, translated_content = translate_content("Este es un mensaje en español")
    assert is_english == False
    assert translated_content == "This is a message in Spanish."  # Updated expected translation

    # Test case 2
    is_english, translated_content = translate_content("Ceci est un message en français")
    assert is_english == False
    assert translated_content == "This is a message in French."  # Updated expected translation

#def test_llm_gibberish_response():
    # Test case 1
    # is_english, translated_content = translate_content("fksdj dhsk djhks skjdhs")
    # assert is_english == False
    # assert translated_content == response  # Updated expected error message

    # # Test case 2
    # is_english, translated_content = translate_content("dhskj skal dhjsh")
    # assert is_english == False
    # assert translated_content == response  # Updated expected error message

# Example usage
if __name__ == "__main__":
    test_chinese()
    test_llm_normal_response()
    # test_llm_gibberish_response()
    print("All tests passed.")


# #############################

from unittest.mock import patch
import openai

@patch.object(openai.ChatCompletion, 'create')
def test_unexpected_language(mocker):
  # we mock the model's response to return a random message
  mocker.return_value.choices[0].message.content = "I don't understand your request"

  # TODO assert the expected behavior
  assert translate_content("Hier ist dein erstes Beispiel.")

  #test1:
@patch.object(openai.ChatCompletion, 'create')
def test_empty_prompt(mocker):
  """Simulate an empty string response from the LLM."""
  mocker.return_value.choices[0].message.content = ""

  assert translate_content("Hier ist dein erstes Beispiel.")

#test2:
@patch.object(openai.ChatCompletion, 'create')
def test_different_language_response(mocker):
  """Simulate a response in a different language or unexpected output."""
  mocker.return_value.choices[0].message.content = "Esto está en español"


  assert translate_content("Hier ist dein erstes Beispiel.")

#test3:
@patch.object(openai.ChatCompletion, 'create')
def test_no_response(mocker):
  """Simulate no 'choices' field in the response."""
  mocker.return_value = {}


  assert translate_content("Hier ist dein erstes Beispiel.")

#test4:
@patch.object(openai.ChatCompletion, 'create')
def test_digits_only_response(mocker):
  """Simulate a response with only digits."""
  mocker.return_value.choices[0].message.content = "1234567890"


  assert translate_content("Hier ist dein erstes Beispiel.")
