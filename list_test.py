words = "welcome to my world. what a wonderful world!"

sp_words = words.split(' ')
c = 0
i = 0
j = 0
for w in sp_words:
    if len(w) >= c:
        c = len(w)
        j = i
    i += 1
print(sp_words[j])           # wonderful
#-----------------------------------------------#
print(max(sp_words))         # world.
print(max(sp_words, key=len))# wonderful
