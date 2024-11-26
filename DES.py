#Implementation of DES encryption and decrption
def initial_permutation(x):
  # Initial Permutation Table
  ip_table = [
      58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9,  1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7
  ]

  # Apply the initial permutation
  output = ''
  for position in ip_table:
      output += x[position - 1]

  return output

def final_permutation(x):
  # Final Permutation Table
  fp_table = [
      40, 8, 48, 16, 56, 24, 64, 32,
      39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30,
      37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28,
      35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26,
      33, 1, 41, 9, 49, 17, 57, 25
  ]

  # Apply the final permutation
  output = ''
  for position in fp_table:
      output += x[position - 1]
  return output

def expansion_box(input_bits):
  # Expansion Permutation Table
  expansion_table = [
      32, 1, 2, 3, 4, 5, 4, 5,
      6, 7, 8, 9, 8, 9, 10, 11,
      12, 13, 12, 13, 14, 15, 16, 17,
      16, 17, 18, 19, 20, 21, 20, 21,
      22, 23, 24, 25, 24, 25, 26, 27,
      28, 29, 28, 29, 30, 31, 32, 1
  ]

  # Apply the expansion permutation
  output = ''
  for position in expansion_table:
      output += input_bits[position - 1]
  return output

def p_box(x):
  #permutaiton 
  permutation_box = [
      16, 7, 20, 21, 29, 12, 28, 17,
      1, 15, 23, 26, 5, 18, 31, 10,
      2, 8, 24, 14, 32, 27, 3, 9,
      19, 13, 30, 6, 22, 11, 4, 25
  ]
  output = ''
  for position in permutation_box:
      output += x[position - 1]
  return output

def key_xor(input_bits, key):
  # XOR input bits with key
  return ''.join(str(int(bit) ^ int(key_bit)) for bit, key_bit in zip(input_bits, key))

def s_box(input_bits):
  s_boxes = [
    # S-box 1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    # S-box 2
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    # S-box 3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    # S-box 4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    # S-box 5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    # S-box 6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    # S-box 7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    #S-box 8
    [
      [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
      [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
      [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
      [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
  ]
  
  output = ''
  for i in range(8):
      block = input_bits[i * 6:(i + 1) * 6]
      row = int(block[0] + block[5], 2)
      col = int(block[1:5], 2)
      s_value = s_boxes[i][row][col]
      output += format(s_value, '04b')

  return output

def generate_keys(key):
  # Permutation Choice 1 Table
  pc1_table = [
      57, 49, 41, 33, 25, 17, 9,
      1, 58, 50, 42, 34, 26, 18,
      10, 2, 59, 51, 43, 35, 27,
      19, 11, 3, 60, 52, 44, 36
  ]

  # Permutation Choice 2 Table
  pc2_table = [
      14, 17, 11, 24, 1, 5,
      3, 28, 15, 6, 21, 10,
      23, 19, 12, 4, 26, 8,
      16, 7, 27, 20, 13, 2,
      41, 52, 31, 37, 47, 55,
      30, 40, 51, 45, 33, 48,
      44, 49, 39, 56, 34, 53,
      46, 42, 50, 36, 29, 32
  ]

  # Apply Permutation Choice 1 (PC1)
  key_permuted = ''.join(key[pc1] for pc1 in pc1_table)

  # Split key into left and right halves
  left_half = key_permuted[:28]
  right_half = key_permuted[28:]

  # Generate 16 round keys
  round_keys = []
  for i in range(16):
      # Perform circular left shifts
      left_half = left_half[1:] + left_half[0]
      right_half = right_half[1:] + right_half[0]

      # Apply Permutation Choice 2 (PC2)
      round_key = ''.join(left_half[pc2 - 1] for pc2 in pc2_table[:24]) + \
                  ''.join(right_half[pc2 - 1] for pc2 in pc2_table[24:])
      round_keys.append(round_key)

  return round_keys

def des_round(input_bits, round_key):
  # Split input into left and right halves
  left_half = input_bits[:32]
  right_half = input_bits[32:]

  # Expansion (E-box)
  expanded_right = expansion_box(right_half)

  # Key XOR
  xored_right = key_xor(expanded_right, round_key)

  # S-box substitution
  substituted_right = s_box(xored_right)

  # Permutation (P-box)
  permuted_right = p_box(substituted_right)

  # XOR with left half
  new_right = ''.join(str(int(bit1) ^ int(bit2)) for bit1, bit2 in zip(permuted_right, left_half))

  # New left half becomes the old right half
  new_left = right_half

  # Combine left and right halves
  return new_left + new_right

def des_encrypt(plaintext, key):
  # Padding:
  if len(plaintext) % 64 != 0:
      padding_length = 64 - (len(plaintext) % 64)
      plaintext += '0' * padding_length
    
  # Apply initial permutation
  permuted_text = initial_permutation(plaintext)

  # Generate round keys
  round_keys = generate_keys(key)  

  # Apply 16 rounds of DES
  current_bits = permuted_text
  for round_key in round_keys:
      current_bits = des_round(current_bits, round_key)

  # Apply final permutation
  cipher_text = final_permutation(current_bits)
  return cipher_text

def des_decrypt(cipher_text, key):
  # Apply initial permutation
  permuted_text = initial_permutation(cipher_text)

  # Generate round keys
  round_keys = generate_keys(key)

  # Apply 16 rounds of DES in reverse order for decryption
  current_bits = permuted_text
  for round_key in reversed(round_keys):
      current_bits = des_round(current_bits, round_key)

  # Apply final permutation
  plain_text = final_permutation(current_bits)
  plain_text = plain_text.rstrip('0')
  return plain_text