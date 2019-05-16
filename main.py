def length_of_str(text: str) -> int:
    counter = 0
    for char in text:
        counter += 1
    return counter
      
      #  text = 'Hello,  World!'

def word_count(text: str) -> int:
    if text == "": 
        return 0

    counter = 0
    is_letter = False

    for char in text:
        if char != " ":
            is_letter = True
        elif is_letter:
            counter += 1
            is_letter = False
    
    if is_letter:
        counter += 1
    return counter

def sentences_count(text: str):
    pass

def letter_count(text: str):
    pass