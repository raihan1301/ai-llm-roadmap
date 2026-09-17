"""
Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:
String encode(List<String> strs) {
    // ... your code
    return encoded_string;
}

Machine 2 (receiver) has the function:
List<String> decode(String encoded_string) {
    // ... your code
    return decoded_strs;
}

So Machine 1 does:
String encoded_string = encode(strs);

and Machine 2 does:
List<String> decoded_strs = decode(encoded_string);

decoded_strs in Machine 2 should be the same as the input strs in Machine 1.
Implement the encode and decode methods.

Example 1:
Input: strs = ["Hello","World"]
Output: ["Hello","World"]

Explanation for example 1:
Solution solution = new Solution();
String encoded_string = solution.encode(strs);

// Machine 1 ---encoded_string---> Machine 2
List<String> decoded_strs = solution.decode(encoded_string);

Example 2:
Input: strs = [""]
Output: [""]

Constraints:
0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains any possible characters out of 256 valid ASCII characters.
"""

class Solution:

    def encode(self, strs: list[str]) -> str:
        encode_string = ""

        for word in strs:
            encode_string = encode_string + str(len(word)) +"#" + word
            """
            we will store length of word and than # and than word
            example : ["Hello", "World"] ----> 5#Hello5#World
            example : ["", ""]  -----> 0#0#
            """
        return encode_string


    def decode(self, s: str) -> list[str]:

        result = []
        i = 0

        while i < len(s) : 
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])  # this will give how much is the length of the single world example hello

            word_start = j + 1  # word will start after #
            word_end = word_start + length

            result.append(s[word_start:word_end])

            i = word_end

        return result

        """
        Explanation of above code 
        so we know that this encoded string ["Hello", "World", "Good", "Morning"] ----> 5#Hello5#World4#Good7#Morning

        now we initalize empty list and index i = 0
        than we started while loop till the length of string in this case "5#Hello5#World4#Good7#Morning"  == 29

        we assign j as i so it will be 0 first
        than we ran the while loop till we find # till than we increase the j , in this case s[1] = #

        hence length will be s[0:1] and that number is 5 so we know the first word is of 5 letters

        word start after the # which is s[3] or j+1
        word end will be length + start
        and than we append into the result
        """


def main():
    strs = ["Hello","World"]
    solution = Solution()

    encode_result = solution.encode(strs)
    print(f"encode_result : {encode_result}")

    decode_result = solution.decode(encode_result)
    print(f"decode_result : {decode_result}")

main()
