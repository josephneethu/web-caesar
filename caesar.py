def alphabet_position(letter):
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in letter :
        if char.islower():
            position = alphabet_lower.index(char)
        else:
            position = alphabet_upper.index(char)
    return position


def rotate_character(char, rot):
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_char = ""
    if char.isalpha() == False:
        new_char = new_char + char
    elif char.islower():
        rotated_index = int(alphabet_lower.index(char)) + int(rot)
        new_char = new_char + alphabet_lower[rotated_index%26]
    else :
        rotated_index = int(alphabet_upper.index(char)) +int(rot)
        new_char = new_char +alphabet_upper[rotated_index%26]

    return new_char

def encrypt(text, rot):
    encrypted_text = ""
    for char in text :
        rot_char = rotate_character(char,rot)
        encrypted_text = encrypted_text + rot_char
    return encrypted_text
