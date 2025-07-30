import random
import time # Import the time module to calculate runtime

def build_markov_chain(text):
    """
    Builds a Markov chain model from a given text.

    Args:
        text (str): The source text to build the model from.

    Returns:
        dict: A dictionary representing the Markov chain.
              Keys are words, and values are lists of words that follow.
    """
    words = text.split()
    chain = {}
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i+1]
        if current_word in chain:
            chain[current_word].append(next_word)
        else:
            chain[current_word] = [next_word]
    return chain

def generate_text(chain, length=100, start_word=None):

    #Generates text using the Markov chain model.
    if not chain:
        return "The chain is empty. Cannot generate text."

    
    # Check if a valid start_word is provided by the user
    if start_word and start_word in chain:
        current_word = start_word
    else:
        # Inform the user if their word was not found or not provided
        if start_word:
            print(f"(Note: '{start_word}' not found in text. Starting with a random word.)")
        # Fallback to a random word if no valid start word is given
        current_word = random.choice(list(chain.keys()))
    
    generated_words = [current_word]
    
    for _ in range(length - 1):
        if current_word in chain and chain[current_word]:
            next_word = random.choice(chain[current_word])
            generated_words.append(next_word)
            current_word = next_word
        else:
            break
            
    return ' '.join(generated_words)


if __name__ == "__main__":
    
    
    
    try:
        filename = input("Enter the name of the text file (e.g., 'sample.txt'): ")
        start_word_input = input("Enter the first word (or press Enter for random): ").strip()
        start_time = time.time()
        with open(filename, 'r', encoding='utf-8') as f:
            text_data = f.read()      
        markov_model = build_markov_chain(text_data)
        
        # Pass the user's chosen start word to the generator function
        new_text = generate_text(markov_model, length=100, start_word=start_word_input)
        
        print("\n--- Generated Text ---")
        print(new_text)
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # --- FEATURE 2: Calculate and display the runtime ---
        end_time = time.time()
        runtime = end_time - start_time
        print(f"\n--- Program finished in {runtime:.4f} seconds. ---")
'''
First test: Data: Shapesperes works first word:Othello

Othello guard, I will you have sumptuously re-edified; Here they look you, And why, my left now, after you. He did speak that I'll begin. MARSHAL. Sound trumpets; let him I' th' neck answer for I dare offer. GRATIANO. Here's the appetite I know not again; I must win the while! THIRD MESSENGER. All princely presence They think thee to come there. CAIUS. By gar, de la robe? ALICE. Les doigts? ALICE. D'elbow. Comment appelez-vous le possession of his period. Where is our queen. MAECENAS. Now powers As those whom I but squeezing you will be sorry it me;'''
