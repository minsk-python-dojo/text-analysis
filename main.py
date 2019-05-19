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

def sentences_count(text: str) -> int:
    counter = 0
    while text:
        to_slice_count = 1
        if text[:3] == '...':
            counter += 1
            to_slice_count = 3
        elif text[:2] == '?!':
            counter += 1
            to_slice_count = 2
        elif text[0] in '.!?':
            counter += 1
        text = text[to_slice_count:]
    return counter


def letter_count(text: str):
    pass
