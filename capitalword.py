song = 'odsp adspa mfdfk akdsjmfd ewurmasf irtjmamma opwkma mjfd opew ms op'
result = []
for i in song.split():
    if i.startswith('m'):
        q = i.replace('m', 'M')
        result.append(q)
    else:
        result.append(i)
print(' '.join(result))

# 1-line
# result = ' '.join([word.replace('m', 'M') if word.startswith('m') else word
#                    for word in song.split()])
# print(result)