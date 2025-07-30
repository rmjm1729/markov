import random

def build_markov_chain(text):
    """
    Builds a Markov chain model from a given text.

    Args:
        text (str): The source text to build the model from.

    Returns:
        dict: A dictionary representing the Markov chain.
              Keys are words, and values are lists of words that follow.
    """
    # Split the text into a list of words
    words = text.split()
    
    # The dictionary to hold the Markov chain model
    chain = {}
    
    # Iterate through the list of words to build the chain
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i+1]
        
        # If the current word is already in our chain, append the next word to its list
        if current_word in chain:
            chain[current_word].append(next_word)
        # Otherwise, create a new entry for the current word
        else:
            chain[current_word] = [next_word]
            
    return chain

def generate_text(chain, length=50):
    """
    Generates text using the Markov chain model.

    Args:
        chain (dict): The Markov chain model.
        length (int): The number of words to generate.

    Returns:
        str: The generated text.
    """
    if not chain:
        return "The chain is empty. Cannot generate text."

    # Choose a random starting word from the keys of the chain
    current_word = random.choice(list(chain.keys()))
    generated_words = [current_word]
    
    # Generate words one by one
    for _ in range(length - 1):
        # Check if the current word has any followers
        if current_word in chain and chain[current_word]:
            # Choose a random word from the list of followers
            next_word = random.choice(chain[current_word])
            generated_words.append(next_word)
            current_word = next_word
        else:
            # If a word has no followers, break the loop
            break
            
    return ' '.join(generated_words)

# --- Main part of the script ---
if __name__ == "__main__":
    try:
        # Get the filename from the user
        filename = input("Enter the name of the text file (e.g., 'sample.txt'): ")
        
        # Read the content of the file
        with open(filename, 'r', encoding='utf-8') as f:
            text_data = f.read()
            
        # Build the Markov chain from the text data
        markov_model = build_markov_chain(text_data)
        
        # Generate new text using the model
        new_text = generate_text(markov_model, length=100)
        
        print("\n--- Generated Text ---")
        print(new_text)
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")