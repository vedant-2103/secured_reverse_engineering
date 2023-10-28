import random
dict1 = {}
def make_dict(dic):
    local_98 = [7, 9, 0xd, 5, 0x13, 0x12, 4, 0x12, 8, 0xf, 10, 9, 0xf, 2, 0x12, 0xf, 0x12, 0xc, 0x10, 0x10, 0x10, 0xb, 0xd, 4, 9, 9, 4, 0xd, 9, 0x13, 7, 3]
    for i in range(len(dic)):
        if dic[i] not in dict1:
            dict1[dic[i]] = []
        for j in range(len(local_98)):
            if ((ord(dic[i]) ^ local_98[j]) % local_98[j] == 0):
                dict1[dic[i]].append(j)
make_dict("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(dict1)

word_length = 32

def generate_combination(word_length, dict1):
    combination = [''] * word_length
    for letter, indices in dict1.items():
        # print(indices)
        if not indices:
            continue
        index = random.choice(indices)
        combination[index] = letter

    # Fill empty positions with random letters from the dictionary
    for i in range(word_length):
        if not combination[i]:
            available_letters = [letter for letter, indices in dict1.items() if i in indices]
            if available_letters:
                letter = random.choice(available_letters)
                combination[i] = letter
            else:
                # Handle the case when there are no available letters for the index
                # You can add your own logic here, like choosing a random letter or skipping this position
                pass

    return ''.join(combination)

# Generate 5 combinations
print("Use any of the below keys to unlock and get the flag:")
for _ in range(5):
    result = generate_combination(word_length, dict1)
    print(result)





# "ACDDADPFUDHUDRHPAZLXLICXDULZZZSU"

# [7, 5, 6, 5, 3, 0xf, 0x10, 0xb, 0xf, 2, 0x12, 0x11, 0xf, 3, 6, 0x10, 7, 10, 0x13, 0xc, 0x13, 0xb, 0xd, 9, 0x11, 0xf, 0x13, 0x12, 0x12, 5, 7, 0xf]
#  0: A,J,S
#  5: D,U
#  7: I,F,S
#  21: I,F,S
#  22: C,L,V
#  23: A,X,S,X
#  24: D,U
#  25: D,U
#  26: 

# print(len("PPAPPZZFHXPLPULFSZSSSLSHRZZSRAFL"))



# {'A': [2, 16, 18, 19, 20, 27, 29], 
#  'B': [], 'C': [0, 12, 17, 31], 
#  'D': [0, 3, 9, 12, 13, 17, 24, 28], 'E': [],
#  'F': [7, 15, 22, 30], 'G': [], 'H': [3, 5, 6, 8, 23, 24, 28], 
#  'I': [7, 15, 22, 30], 'J': [2, 19], 'K': [], 
#  'L': [1, 3, 4, 11, 14, 21, 25, 26, 31], 'M': [], 'N': [0, 12, 17, 24, 28], 'O': [], 
#  'P': [0, 1, 3, 4, 10, 11, 12, 17, 21, 23, 25, 26], 'Q': [], 
#  'R': [24, 28], 'S': [2, 7, 15, 16, 18, 19, 20, 22, 27, 29, 30], 'T': [3], 
#  'U': [0, 12, 13, 17], 'V': [31], 'W': [], 'X': [3, 9, 16, 18, 20, 23, 27, 29], 
#  'Y': [], 'Z': [0, 1, 4, 5, 6, 8, 11, 12, 17, 21, 25, 26]}


# def encode(input_str):
#     local_98 = [7, 5, 6, 5, 3, 0xf, 0x10, 0xb, 0xf, 2, 0x12, 0x11, 0xf, 3, 6, 0x10, 7, 10, 0x13, 0xc, 0x13, 0xb, 0xd, 9, 0x11, 0xf, 0x13, 0x12, 0x12, 5, 7, 0xf]
#     result = []

#     for i in range(len(input_str)):
#         print(f"For i = {i}: Character = {input_str[i]}, local_98 = {local_98[i]},ord(char) = {ord(input_str[i])}, xor is = {(ord(input_str[i]) ^ local_98[i])},mod condition is = {(ord(input_str[i]) ^ local_98[i]) % local_98[i] != 0} , and mod value is =  {(ord(input_str[i]) ^ local_98[i]) % local_98[i]}")
#         # if(ord(input_str[i]) & 0x100 != 0):
#         #     print(f"ord is= {ord(input_str[i])}, and operation is: {ord(input_str[i]) & 0x100}")
#         #     print("yes")
#         if ((ord(input_str[i]) ^ local_98[i]) % local_98[i] != 0) or not input_str[i].isalpha():
#             continue
#         result.append(chr((ord(input_str[i]) ^ local_98[i]) // local_98[i]))

#     return result

# input_str = "ACDDADPFUDHUDRHPAZLXLICXDULZZZSU"
# decoded_result = encode(input_str)

# if decoded_result:
#     print("Input String:", input_str)
# else:
#     print("No valid input string found.")