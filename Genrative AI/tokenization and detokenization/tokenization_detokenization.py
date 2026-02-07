# Tokenization and Detokenization

# Tokenization - Tokenizationis the process of converting text into a sequence of tokens, which are the basic units of meaning in natural language processing.

# Detokenization - Detokenization is the reverse process, where a sequence of tokens is converted back into human-readable text.

# Toknization
# tiktoken-0.12.0

import tiktoken
encode_decode_model = tiktoken.encoding_for_model("gpt-3.5-turbo")
text = "Hello, How are you?"
encode_text = encode_decode_model.encode(text)
print("Original Text:",text)
print("Encoded Text:",encode_text)
# Expected output in vector form.

# Detoken

decode_text = encode_decode_model.decode(encode_text)
print("Decoded Text:",decode_text)
# Expected output : Original Text.