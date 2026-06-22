class Solution:
    """
    Thought process
    Encode
    - To encode a string we need to first calulate the number of characters in each string. 
    - We append each strings character count as a prefix to the original string before
        including it in the encoding. 
    - We do this for all strings to form the final encoded string
    - The prefix will include a delimeter to tell the number place of the character count.
    - Eg. 5#Hello, 10#difficulty. This helps us differentiate if the next word is 10 or 1

    Decode
    - To decode the string; we iterate through the encoded string; 
    - We extract out the prefix for the next word
    - We form that word using the prefix count as the window size for the next word. 
    - We do for the remainder of the string till we form our encoded string back

    strs = ["Hello","World"]4

               0 1 2 3 4 5 6 7 8 9 10 11 12 13
    encoded = "5 # H e l l o 5 # W o  r  l  d"
                                               ^
    decoded = ["Hello", "World"]
    prefix = 0
    pointer = 14
    start = 9
    end = 14
    """

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for word in strs:
            count = len(word)
            encoded += f'{count}#{word}'
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        prefix = 0
        pointer = 0

        while pointer < len(s):
            if s[pointer].isdigit():
                prefix = prefix * 10 + int(s[pointer])
                pointer += 1
                continue 
            
            start = pointer + 1
            end = prefix + pointer + 1
            word = s[start:end]
            decoded.append(word)
            pointer = end
            prefix = 0
        
        return decoded

