"""Main module for the game"""


import game_ukraine


ldr_enemy = game_ukraine.Enemy('лнрівець', 'зведений брат днрівця, що має проблеми з мозком')
ldr_enemy.set_weakness('книга')
svatove = game_ukraine.FrontLineRegion('Сватове')
svatove.set_character(ldr_enemy)

vagner = game_ukraine.Enemy('вагнерівець', 'знає, що таке блатний')
vagner.set_weakness('фарш')
bakhmut = game_ukraine.FrontLineRegion('Бахмут')
bakhmut.set_character(vagner)

dpr_enemy = game_ukraine.Enemy('днрівець', 'творець теракту на макіївському роднічку')
dpr_enemy.set_weakness('Ахметов')
donetsk = game_ukraine.FrontLineRegion('Донецьк')
donetsk.set_character(dpr_enemy)

regular = game_ukraine.Enemy('регулярна армія', 'оркоподібні')
regular.set_weakness('пральна машина')
melitopol = game_ukraine.FrontLineRegion('Мелітополь')
melitopol.set_character(regular)


heal = game_ukraine.HealItem('Аптечка')
heal.set_description("Додає +1 здоров'я")

zalyzhnyy = game_ukraine.Friend('Валерій Залужний', 'Головнокомандувач ЗС України')
zalyzhnyy.set_item(heal)
kyiv = game_ukraine.PeacefulRegion('Київ')
kyiv.set_character(zalyzhnyy)
book = game_ukraine.Weapon('книга')
kyiv.set_item(book)

sviatoslav = game_ukraine.Friend('Святослав Стегній', 'Студент 1 курсу УКУ КН')
sviatoslav.set_item(heal)
lviv = game_ukraine.PeacefulRegion('Львів')
lviv.set_character(sviatoslav)
meat = game_ukraine.Weapon('фарш')
lviv.set_item(meat)

sternenko = game_ukraine.Friend('Сергій Стерненко', 'Блогер, волонтер, справжній одесит')
sternenko.set_item(heal)
odesa = game_ukraine.PeacefulRegion('Одеса')
odesa.set_character(sternenko)
machine = game_ukraine.Weapon('пральна машина')
odesa.set_item(machine)

biden = game_ukraine.Friend('Джо Байден', 'Любить морозиво')
biden.set_item(heal)
usa = game_ukraine.PeacefulRegion('США')
usa.set_character(biden)
akhmetov = game_ukraine.Weapon('Ахметов')
usa.set_item(akhmetov)



svatove.link_region(bakhmut, 'південь')
svatove.link_region(kyiv, 'захід')
bakhmut.link_region(svatove, 'північ')
bakhmut.link_region(donetsk, 'південь')
bakhmut.link_region(kyiv, 'захід')
donetsk.link_region(bakhmut, 'північ')
donetsk.link_region(melitopol, 'захід')
melitopol.link_region(donetsk, 'схід')
melitopol.link_region(odesa, 'захід')
kyiv.link_region(odesa, 'південь')
kyiv.link_region(lviv, 'захід')
kyiv.link_region(svatove, 'схід')
odesa.link_region(kyiv, 'північ')
odesa.link_region(melitopol, 'схід')
lviv.link_region(kyiv, 'схід')
lviv.link_region(usa, 'захід')
usa.link_region(lviv, 'схід')


current_room = kyiv
lives = 1
win = False
backpack = []

while lives > 0 and win == False:

    print("\n")
    print(f'Кількість життів - {lives}')
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    command = input("> ")
    if command in ["північ", "південь", "схід", "захід"]:
        # Move in the given direction
        current_room = current_room.move(command)

    elif command == "взяти":
        if current_room.type == 'peaceful':
            item = current_room.get_item()
            if item is not None:
                print("Ти поклав " + item.get_name() + " до свого рюкзака")
                backpack.append(item.get_name())
                current_room.set_item(None)
        else:
            print("Тут нема, що взяти")

    elif command == "поговорити":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
            if inhabitant.give_item() is not None:
                lives += 1
                inhabitant.set_item(None)
                print(inhabitant.name+' під час розмови запхав тобі в кишеню аптечку')
    elif command == "битися":
        if inhabitant is not None and current_room.type == 'frontline':

            print("з чим ти будеш битись?")
            print('ось твій рюкзак '+ f'{backpack}')
            fight_with = input()

            if fight_with in backpack:

                if inhabitant.fight(fight_with) == True:
                    print(f"Молодець, ти знищив ворога")
                    current_room.character = None
                    if inhabitant.get_defeated() == 4:

                        print("Вітаю, ти звільнив більшу частину України,\nЗалишився тільки Крим!")
                        print('Зараз тобі доведеться зустрітись з босом та звільнити півострів')
                        putin = game_ukraine.Putin('вЛАДМІР ПІТУН',\
                                                    'великий полководець і політик в своїх снах')
                        crimea = game_ukraine.Crimea('Крим')
                        crimea.set_character(putin)
                        current_room = crimea
                        crimea.get_details()
                        command = input("> Введи число від 1 до 5 ")
                        if putin.fight(int(command)) == True:
                            win = True
                            print('Ти переміг!')
                        else:
                            print('Ти не вгадав...')
                            lives -= 1
                            if lives == 0:
                                print('Ти програв путіну, добре, що це лише гра')
                else:

                    lives -= 1
                    if lives > 0:
                        print("Ти програв битву, але не війну!")
                    else:
                        print('Ти дав фору оркам, спробуй ще раз!')
            else:
                print("У тебе немв " + fight_with)
        else:
            print("Тут нема з ким битися...")
    else:
        print(command + " недоступно")
