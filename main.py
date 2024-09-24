# import pathlib

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

# print('uzduotis 8')
# print()
# print('Iveskite skaiciu')
# sk = int(input())
# if sk % 7 == 0:
#     print('skaicius dalinasi is 7')
# else:
#     print('skaicius nesidalina is 7')

# print('uzduotis 9')
# print()
#
# file_ext = pathlib.Path('main.py').suffix
# #find file extension
# if file_ext == '.py':
#     print('failas yra .py')
# else:
#     print('failas ne .py')

# print('uzduotis 10')
# print()
# print('Iveskite skaiciu')
# sk = int(input())
# if sk % 2 == 0:
#     print('skaicius yra lyginis')
# elif sk % 5 == 0:
#     print('skaicius dalinasi is 5')
# elif sk == 3:
#     print('skaicius lygus 3')
# else:
#     print('Klaida: salygu atitikmens nerasta')

# print('uzduotis 11')
# print()
# print('Iveskite pirma skaiciu')
# sk = int(input())
# print('Iveskite antra skaiciu')
# sk2 = int(input())
# print('Iveskite trecia skaiciu')
# sk3 = int(input())
# if sk == sk2:
#     print('Pirmas ir antras skaicius yra lygus')
# elif sk == sk3:
#     print('Pirmas ir trecias skaicius yra lygus')
# elif sk3 > sk:
#     print('Trecias skaicius yra didesnis uz pirma')
# elif sk2 == sk3 * 2:
#     print('Antras skaicius yra lygus dvigubai trecio skaiciaus reiksmei')
# elif sk % 3 == 0:
#     print('Pirmas skaicius dalinasi is 3')
# else:
#     print('Klaida: nepavyko rasti salygu atitikmenu')
#
# print('uzduotis 12')
# print()
# print('Iveskite pirma skaiciu')
# sk = int(input())
# print('Iveskite antra skaiciu')
# sk2 = int(input())
# print('Iveskite trecia skaiciu')
# sk3 = int(input())
# maxim = max(sk, sk2, sk3)
# print('didziausia ivesta reiksme yra', maxim)

# print('uzduotis 13')
# print()
# print('Iveskite pirma skaiciu')
# sk = int(input())
# print('Iveskite antra skaiciu')
# sk2 = int(input())
# print('Iveskite trecia skaiciu')
# sk3 = int(input())
# minim = min(sk, sk2, sk3)
# print('maziausia ivesta reiksme yra', minim)

# print('uzduotis 14')
# print()
# print('Iveskite pirma egzamino ivertinima')
# sk = int(input())
# if sk < 0 or sk > 10:
#     print('Klaida: iveskite pazymi nuo 0 iki 10')
#     sk = int(input())
# print('Iveskite antra egzamino ivertinima')
# sk2 = int(input())
# if sk2 < 0 or sk2 > 10:
#     print('Klaida: iveskite pazymi nuo 0 iki 10')
#     sk2 = int(input())
# print('Iveskite trecia egzamino ivertinima')
# sk3 = int(input())
# if sk3 < 0 or sk3 > 10:
#     print('Klaida: iveskite pazymi nuo 0 iki 10')
#     sk3 = int(input())
# if (sk + sk2 + sk3) / 3 >= 8:
#     print('Gautas vidurkis yra tarp 8 ir 10')
# elif (sk + sk2 + sk3) / 3 >= 5:
#     print('Gautas vidurkis yra tarp 5 ir 8')
# elif (sk + sk2 + sk3) / 3 < 5:
#     print('Gautas vidurkis yra mazesnis nei 5')
# else:
#     print('Kazkas netaip')

print('uzduotis 15')
print()
print('Iveskite pirma skaiciu')
sk = int(input())
print('Iveskite antra skaiciu')
sk2 = int(input())
if sk > sk2 or sk == 0:
    print('pirmas skaicius yra didesnis uz antra arba lygus 0')
if sk < sk2 or sk2 == 5:
    print('antras skaicius yra didesnis uz pirma arba lygus 5')
if sk > sk2 and sk == 20:
    print('pirmas skaicius yra didesnis uz antra ir lygus 20')
if sk < sk2 and sk2 < 100:
    print('antras skaicius yra didesnis uz pirma ir mazesnis uz 100')
