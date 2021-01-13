print(', '.join([f"{word} -> {length}" for word, length in [(w, len(w)) for w in input().split(', ')]]))
