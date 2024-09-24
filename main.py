# print('uzduotis 2')
# print()
# print('Iveskite savo amziu (metais)')
# amzius = int(input())
# if amzius >= 18:
#     print('Jus galite balsuoti')
# else:
#     print('Jus dar negalite balsuoti')

# print('uzduotis 3')
# print()
# print('Iveskite pirma pazymi')
# pirmas = int(input())
# print('Iveskite antra pazymi')
# antras = int(input())
# print('Iveskite trecia pazymi')
# trecias = int(input())
# if (pirmas + antras + trecias) / 3 >= 5:
#     print('Pazymiu vidurkis teigiamas')
# else:
#     print('Pazymiu vidurkis neigiamas')

print('uzduotis 4')
print()
print('Iveskite skaiciu')
sk = int(input())
if sk / 5:
    print('skaicius dalinasi is penkiu, sio skaiciaus daugybos lentele nuo 1 iki 5:')
    print(sk * 1)
    print(sk * 2)
    print(sk * 3)
    print(sk * 4)
    print(sk * 5)
if sk % 2 == 0:
    print('skaicius yra lyginis:')
    print(sk)
    print(sk * sk)
    print(sk/2)
if sk % 7 >= 1:
    print('Skaicius nesidalina is 7, iveskite antra skaiciu')
    sk2 = int(input())
    print(sk, '+', sk2, '=', sk + sk2)
    print(sk, '-', sk2, '=', sk - sk2)
    print(sk, '*', sk2, '=', sk * sk2)
    print(sk, '/', sk2, '=', sk / sk2)
