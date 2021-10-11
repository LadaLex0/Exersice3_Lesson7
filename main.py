count = {}
words = input('Write your sentence: ')
for i in words.split():
    count[i] = len(i)
print(count)