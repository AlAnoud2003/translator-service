from src.translator import translate_content


def test_chinese():
    is_english, translated_content = translate_content("这是一条中文消息")
    assert is_english == False
    assert translated_content == "This is a Chinese message"

#please implement a unit test that verifies that your program can return correct value if LLM provides an expected result
def test_llm_normal_response():
    # Test case 1
    is_english, translated_content = translate_content("Este es un mensaje en español")
    assert is_english == False
    assert translated_content == "This is a Spanish message"  # Assuming this is the expected translation

    # Test case 2
    is_english, translated_content = translate_content("Ceci est un message en français")
    assert is_english == False
    assert translated_content == "This is a French message"  # Assuming this is the expected translation

# please implement a unit test that verifies that your program can handle a gibberish response.
def test_llm_gibberish_response():
    # Test case 1
    is_english, translated_content = translate_content("gibberish input")
    assert is_english == False
    assert translated_content == "Failed to parse LLM response."  # Assuming this is the expected error message

    # Test case 2
    is_english, translated_content = translate_content("another gibberish input")
    assert is_english == False
    assert translated_content == "Failed to parse LLM response."  # Assuming this is the expected error message

# Example usage
if __name__ == "__main__":
    test_chinese()
    test_llm_normal_response()
    test_llm_gibberish_response()
    print("All tests passed.")