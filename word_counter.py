def count_words(text):
    """
    Count the number of words in a given text.
    
    Parameters:
    text (str): The input text to be processed.
    
    Returns:
    int: The number of words in the input text.
    """
    # Strip leading/trailing whitespace and check if the text is empty
    if not text.strip():
        return 0  # Return 0 if the text is empty
    
    # Split the text into words based on whitespace
    words = text.split()
    
    # Return the number of words
    return len(words)

# Main program execution starts here
if __name__ == "__main__":
    # Prompt the user to enter a sentence or paragraph
    user_input = input("Enter a sentence or paragraph: ")
    
    # Call the count_words function with the user input and store the result
    word_count = count_words(user_input)
    
    # Display the word count to the user
    print(f"The number of words in the entered text is: {word_count}")
