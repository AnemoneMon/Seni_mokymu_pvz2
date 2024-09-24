print('iveskite zodi')
word = input()

if len(word) < 5:
    print(f'zodis {word} yra trumpas')
elif len(word) < 10:
    print(f'zodis {word} yra vidutionio ilgio')
else:
    print(f'zodis {word} yra ilgas')

