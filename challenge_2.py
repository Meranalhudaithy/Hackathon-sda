# ANOTHER SSTORY YOU WONT GET BORED ON MY WATCHHHH
#sureeee i didnt need too code but you know i like to flex my skills


# In the museum archive, you find a note that was "double-locked."

# First lock: a Caesar shift (no key given hmmmm how will we decypher???). 
# Second lock: Base64 wrapping.

# Your job as the conservator: peel off the Base64 wrap then try every
# Caesar unshift until the sentence reads like normal English.
# We’ll rank candidates with a tiny English-ness check Not fancy just effective.

import base64

def caesar_unshift(text, shift):
 
    out = []
    for ch in text:
        if 'A' <= ch <= 'Z':
            out.append(chr((ord(ch) - ord('A') - shift) % 26 + ord('A')))
        elif 'a' <= ch <= 'z':
            out.append(chr((ord(ch) - ord('a') - shift) % 26 + ord('a')))
        else:
            out.append(ch)
    return "".join(out)

def break_cipher(encoded):
 
 
    after_base64 = base64.b64decode(encoded).decode("utf-8")

    
    common = [" the ", " and ", " to ", " you ", " is ", " this ", " message ", " cipher "]
    best_score, best_shift, best_plain = -1, None, None

    for s in range(26):
        candidate = caesar_unshift(after_base64, s)
        score = sum(word in candidate.lower() for word in common)
        if score > best_score:
            best_score, best_shift, best_plain = score, s, candidate

    return best_shift, after_base64, best_plain

if __name__ == "__main__":
    
    encoded_str = "Qm5tZnF6c3RrenNobm1yISBYbnQgZ3p1ZCBicXpiamRjIHNnZCBiaG9nZHEu"

    print(" Removing Base64")
    best_shift, after_b64, plaintext = break_cipher(encoded_str)

    print("After Base64:")
    print(after_b64)
    print(" Caesar unshift:", best_shift)
    print(" original message:")
    print(plaintext)

    print("im a hackerrrrrrr")

    
