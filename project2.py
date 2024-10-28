# Word Counter Program

def count_words(text):
    """
    Count the number of words in a given text.
    
    Parameters:
    text (str): The input text from which to count words.
    
    Returns:
    int: The count of words in the input text.
    """
    # Split the text into words based on whitespace and filter out any empty strings
    words = text.split()
    return len(words)

def main():
    """
    Main function to execute the Word Counter program.
    """
    # Prompt user for input
    user_input = input("Please enter a sentence or paragraph: ").strip()
    
    # Error handling for empty input
    if not user_input:
        print("Error: You entered an empty string. Please provide a valid sentence or paragraph.")
        return
    
    # Count the number of words using the count_words function
    word_count = count_words(user_input)
    
    # Display the word count
    print(f"The number of words in your input is: {word_count}")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
    