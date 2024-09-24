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

# print('uzduotis 4')
# print()
# print('Iveskite skaiciu')
# sk = int(input())
# if sk / 5:
#     print('skaicius dalinasi is penkiu, sio skaiciaus daugybos lentele nuo 1 iki 5:')
#     print(sk * 1)
#     print(sk * 2)
#     print(sk * 3)
#     print(sk * 4)
#     print(sk * 5)
# if sk % 2 == 0:
#     print('skaicius yra lyginis:')
#     print(sk)
#     print(sk * sk)
#     print(sk/2)
# if sk % 7 >= 1:
#     print('Skaicius nesidalina is 7, iveskite antra skaiciu')
#     sk2 = int(input())
#     print(sk, '+', sk2, '=', sk + sk2)
#     print(sk, '-', sk2, '=', sk - sk2)
#     print(sk, '*', sk2, '=', sk * sk2)
#     print(sk, '/', sk2, '=', sk / sk2)

# print('uzduotis 5')
# print()
# print('Iveskite pirma skaiciu')
# pirmas = int(input())
# print('Iveskite antra skaiciu')
# antras = int(input())
# print('Iveskite trecia skaiciu')
# trecias = int(input())
# if pirmas > antras:
#     print('pirmas skaicius didesnis uz antra')
# elif antras > trecias:
#     print('antras skaicius didesnis uz trecia')
# elif trecias > pirmas:
#     print('trecias skaicius didesnis uz pirma')
# else:
#     print('kazkas lygu')

# print('uzduotis 6')
# print()
# print('Iveskite pirma skaiciu')
# pirmas = int(input())
# print('Iveskite antra skaiciu')
# antras = int(input())
# print('Iveskite trecia skaiciu')
# trecias = int(input())
# if pirmas == antras:
#     print('pirmas ir antras skaiciai yra lygus')
# elif antras == trecias:
#     print('antras ir trecias skaicius yra lygus')
# elif pirmas == 0:
#     print('pirmas skaicius lygus 0')
# elif antras < 0:
#     print('antras skaicius yra neigiamas')
# elif trecias > 0:
#     print('trecias skaicius yra teigiamas')
# else:
#     print('nei viena salyga netinka')

# print('uzduotis 6')
# print()
# print('Iveskite egzamino pazymi (nuo 0 iki 10)')
# paz = int(input())
# if paz < 0 or paz > 10:
#     print('Klaida: iveskite pazymi nuo 0 iki 10')
# else:
#     if paz == 10:
#         print('Puiku')
#     elif paz >= 9:
#         print('Labai gerai')
#     elif paz >= 7:
#         print('Gerai')
#     elif paz >=5:
#         print('Patenkinamai')
#     else:
#         print('Egzaminas neislaikyas')

# print('uzduotis 7')
# print()
# print('Iveskite skaiciu')
# sk = int(input())
# if sk % 2 == 0:
#     print('skaicius yra lyginis')
# else:
#     print('skaicius yra nelyginis')

print('uzduotis 8')
print()
print('Iveskite skaiciu')
sk = int(input())
if sk % 7 == 0:
    print('skaicius dalinasi is 7')
else:
    print('skaicius nesidalina is 7')