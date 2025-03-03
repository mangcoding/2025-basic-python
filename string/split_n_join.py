sentence = "Hello World. Today is a good day"
"Today is a good day. hello world"

words = sentence.split(".")
words = list(map(lambda x: x.lower().strip(), words))
print((". ".join(words[::-1])).capitalize())