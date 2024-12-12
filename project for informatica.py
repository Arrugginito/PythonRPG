from tkinter import *
import random as r
from tkinter.messagebox import showerror, showwarning, showinfo
import keyboard as k

win = Tk()
win.title("Strory about hero")
win.geometry("500x400")
win["bg"] = "black"
win.option_add("*tearOff", False)
win.resizable(width=False, height=False)

hp = 0
mana = 0
lvl = 1
exp = 0
pennyc = 0
damage = 0
bossdie = False
notgiv = True
hpoison = 0
mpoison = 0

# класс игры, все нужные функции для работы
# без класса ничего не работает((
class gameforme:

    # функия задающая значения переменных для удобного процесса разработки
    def mainloop(whp, wmana, wlvl, wexp, wpennyc, wdamage):
        global hp
        global mana
        global lvl
        global exp
        global pennyc
        global damage

        damage = wdamage
        hp = whp
        mana = wmana
        lvl = wlvl
        exp = wexp
        pennyc = wpennyc

    # функция для кнопки в самом начале, нужна чтобы не было лютых багов
    def stadv():
        # вызов начальной функции для работы
        gameforme.mainloop(5, 10, 1, 0, 0, 5)
        # создание текста для введения игрока в суть. Удаление первой кнопки
        # создание кнопки для игры
        txt.pack()
        stbtn.place(x="7528", y="32785")
        #gbtn.place(x="10", y="350")
        # отображение здоровья
        htxtp["text"] = hp
        htxtp.place(x="380", y="350")
        # отображение маны
        mtxta["text"] = mana
        mtxta.place(x="410", y="350")
        # отображение уровня
        ltxtl["text"] = lvl
        ltxtl.place(x="480", y="350")
        # отображение пенцов(монет)
        ptxtc["text"] = pennyc
        ptxtc.place(x="450", y="350")
        nwtxt.place(x="243765", y ="29746")
        k.add_hotkey("Enter", gameforme.meetShop)
        

    # функция встречи магазина
    def meetShop():

        # функция покупки для игры в целом

        txt["text"] = "Ты встретил торговца, не желаешь посмотреть товар?"

        bbtn.place(x="55", y="350")
        #gbtn.place(x="234567", y="45378696")
        lbtn.place(x="10", y="350")


    #функция покупки для кнопки
    def pokupka():
        
        global tovar
        
        weaponlvl = r.randint(1, 3)
        weaponDamage = r.randint(1, 6) * weaponlvl
        weapons = ["Кинжал", "Меч", "Топор"]
        weaponsRare = ["Крепкий", "Сломанный", "Легендарный"]
        weaponCost = r.randint(5, 15) * weaponlvl + weaponDamage
        weaponRare = weaponsRare[weaponlvl - 1]
        weapon = r.choice(weapons)

        txt["text"] = "Торговец предлогает:"


        Healpoison = 5
        Manapoison = 5

        tovar = r.randint(0, 2)

        if tovar == 0:
            shtxtop["text"] = "Зелье здоровья {0} пенцов".format(Healpoison)
            shtxtop.pack()

        elif tovar == 1:
            shtxtop["text"] = "Зелье маны {0} пенцов".format(Manapoison)
            shtxtop.pack()

        else:
            shtxtop["text"] = "{0} {1} - {2} пенцов".format(weaponRare, weapon, weaponCost)
            shtxtop.pack()
            
            print(weaponDamage)
            print("урон оружия")

        bbtn.place(x = "53267", y = "641537")
        lbtn.place(x="1213456", y="78901")

        def buying():
            global hp
            global mana
            global damage
            global tovar
            global pennyc
            global exp
            global hpoison
            global mpoison
            
            if tovar == 0:
                
                if pennyc >= Healpoison:
                    hpoison += 1
                    txt["text"] = "С тобой приятно иметь дело"
                    pennyc -= Healpoison
                    exp += 1
                    htxtp["text"] = hp
                    ptxtc["text"] = pennyc
                  
                else:
                    txt["text"] = "Нет денег - уходи"
                    
            elif tovar == 1:
                
                if pennyc >= Manapoison:
                    mpoison += 1
                    txt["text"] = "С тобой приятно иметь дело"
                    pennyc -= Manapoison
                    exp += 1
                    mtxta["text"] = mana
                    ptxtc["text"] = pennyc
                    
                else:
                    txt["text"] = "Нет денег - уходи"
            else:
                
                if pennyc >= weaponCost:
                    if damage >= weaponDamage:
                        damage += weaponDamage // 2
                        print("У вас теперь", damage,"урона")
                    else:
                        damage = weaponDamage
                    pennyc -= weaponCost
                    txt["text"] = "С тобой приятно иметь дело"
                    exp += 1
                    ptxtc["text"] = pennyc
                    
                else:
                    txt["text"] = "Нет денег - уходи"

            buybtn.place(x="34567", y="1234567")
            lbtn.place(x="10", y="350")
            bbtn.place(x="55", y="350")
            shtxtop.place(x="3785", y="2437")
            
        buybtn = Button(text="Купить",command=buying)
        buybtn.place(x="55", y="350")

    # функция ухода из магазина
    def leave():

        shtxtop.place(x="256439", y="25347835")
        lbtn.place(x="1213456", y="78901")
        bbtn.place(x="4567", y="98798")
        txt["text"] = "Вы покинули торговца"
        #gbtn.place(x="10", y="350")

    def meetmonster():
        
        txt["text"] = "На вас напали!"
        #gbtn.place(x="45624", y="658723")  
        mstxt.pack()

        global monsterHP
        global monsterDamage
        global monsterLvl

        monsterLvl = r.randint(1, 4)
        monsterDamage = r.randint(1, 4) * monsterLvl
        monsters = ["Зомби","Скелет","Слизь","Призрак"]
        monster = r.choice(monsters)
        monsterHP = r.randint(1, 4) * monsterDamage + monsterLvl
                
        mtxts["text"] = "Это {0} с {1} еденицами здоровья и {2} еденицами урона".format(monster, monsterHP, monsterDamage)
        mtxts.pack()
        
        def fight():
            
            global monsterHP
            global exp
            global pennyc
            global monsterLvl
            global mana
            global hp

            fight = r.randint(0,1)

            if fight == 0:
                mtxts["text"] = "Вы промахнулись!"
                mana -= monsterLvl
            else:

                monsterHP -= damage 
                mana -= monsterLvl - 2
                mtxta["text"] = mana
                mtxts["text"] = " У монстра осталось {0} едениц здоровья".format(monsterHP)

            if monsterHP > 0:
                txt["text"] = "На вас напали!"
                chancenothavedamage = r.randint(0,1)
            
                if chancenothavedamage == 0:
                    hp -= monsterDamage
                    htxtp["text"] = hp
                else:
                    mstxt["text"] = "Вам повезло! Монстр промахнулся"
                    
            if monsterHP <= 0:
                txt["text"] = "Вы выиграли!"
                mstxt.place(x = "4683", y = "4236")
                fbtn.place(x = "8745", y = "31859")
                rbtn["text"] = "Уйти"
                exp += monsterLvl - 1
                pennyc += monsterLvl + 2
                ptxtc["text"] = pennyc
                mtxts.place(x="3758", y = "3741")
                

            if hp <= 0 or mana <= 0:
                gameforme.dieevent()
                fbtn.place(x = "49623957", y = "28457")
                rbtn.place(x="317588", y="53762")
        
        def run():
            global hp
            global exp
            global monsterHP
            global monsterDamage
            
            cfr = r.randint(0, 1)
            
            if cfr == 0:
                if monsterHP <=0:
                    txt["text"] ="Прах с монстра повеял в вашу сторону"
                    fbtn.place(x = "49623957", y = "28457")
                    rbtn.place(x="317588", y="53762")
                    mstxt.place(x="468379385", y ="4287")
                    mtxts.place(x = "46739", y = "7452")
                    gbtn.place(x="10", y="350")
                    
                else:
                    txt["text"] = "Монстр вас догнал и ударил!"
                    hp -= monsterDamage
                    htxtp["text"] = hp
                
                if hp <= 0 or mana <= 0:
                    gameforme.dieevent()
                    fbtn.place(x = "49623957", y = "28457")
                    rbtn.place(x="317588", y="53762")
            else:
                txt["text"] = "Вы покинули монстра"
                fbtn.place(x = "49623957", y = "28457")
                rbtn.place(x="317588", y="53762")
                mstxt.place(x="468379385", y ="4287")
                mtxts.place(x = "46739", y = "7452")
                #gbtn.place(x="10", y="350")
                
                if monsterHP > 0 and exp > 0:
                    exp -= 1
                    
        fbtn = Button(text = "Сражаться", command=fight)
        fbtn.place(x = "70", y = "350")
        rbtn = Button(text = "Убежать", command=run)
        rbtn.place(x= "10", y = "350")

    def meetboss():
        global damage
        global bossHp
        global bossDmg
        
        txt["text"] = "На пути встал огромный Огр"
        bossDmg = r.randint(15, 50)
        bossHp = r.randint(45, 100) + damage//2
        bossprize = r.randint(100, 10000)

        if lvl >= 10 and bossdie != True:
            mtxts["text"] = " У него {0} едениц урона и {1} едениц здоровья".format(bossDmg, bossHp)
            mtxts.pack()
            mstxt.pack()
            
        elif bossdie == True and lvl >= 10:
            bossHp = 0
            bossDmg = 0
            bossprize = r.randint(0,1)
            
        def fight():
            
            global bossHp
            global exp
            global pennyc
            global bossDmg
            global mana
            global hp
            global bossdie

            fight = r.randint(0,1)

            if fight == 0:
                mtxts["text"] = "Вы промахнулись!"
                mana -= bossHp // 2
            else:

                bossHp -= damage 
                mana -= bossHp - 2
                mtxta["text"] = mana
                mtxts["text"] = " У Огра осталось {0} едениц здоровья".format(bossHp)

            if bossHp > 0:
                txt["text"] = "На вас напали!"
                chancenothavedamage = r.randint(0,1)
            
                if chancenothavedamage == 0:
                    hp -= bossDmg
                    htxtp["text"] = hp
                else:
                    mstxt["text"] = "Вам повезло! Босс промахнулся"
                    
            if bossHp <= 0:
                txt["text"] = "Вы выиграли!"
                mstxt.place(x = "4683", y = "4236")
                fbtn.place(x = "8745", y = "31859")
                rbtn["text"] = "Уйти"
                exp += bossprize
                pennyc += bossprize 
                ptxtc["text"] = pennyc
                mtxts.place(x="3758", y = "3741")
                bossdie = True

            if hp <= 0 or mana <= 0:
                gameforme.dieevent()
                fbtn.place(x = "49623957", y = "28457")
                rbtn.place(x="317588", y="53762")
        
        def run():
            global bossHp
            global exp

            txt["text"] = "Вы покинули Огра"
            fbtn.place(x = "49623957", y = "28457")
            rbtn.place(x="317588", y="53762")
            mstxt.place(x="468379385", y ="4287")
            mtxts.place(x = "46739", y = "7452")
            #gbtn.place(x="10", y="350")
                
            if bossHp > 0 and exp > 0:
                exp -= 10
                if exp < 0:
                    exp -= exp
                    
        fbtn = Button(text = "Сражаться", command=fight)
        fbtn.place(x = "70", y = "350")
        rbtn = Button(text = "Убежать", command=run)
        rbtn.place(x= "10", y = "350")
            
        if lvl < 10:
            mtxts["text"] = "Он оценил вас взглядом и отказался сражаться"
            fbtn.place(x = "72460", y = "324650")
            rbtn["text"] = "Уйти"
            mtxts.pack()
            
        elif bossdie == True:
            txt["text"] = "Вы наткнулись на прах убитого вами Огра"
            fbtn.place(x = "49623957", y = "28457")
            rbtn["text"] = "Уйти"
            mtxts.pack()
                
    def findtreasure():
        
        global pennyc
        global exp
        global mana
        global hp
        global damage

        txt["text"] = "Ты нашел сундук с сокровищем!"
        
        gold = r.randint(10, 100)
        pennyc += gold
        exp += gold // 2
        
        ptxtc["text"] = pennyc

    def dieevent():
        txt["text"] = "Ты погиб. Это так трагично."
        nwtxt.place(x="100", y ="50")
        #gbtn.place(x="258394", y="3527")
        mstxt.place(x="468379385", y ="4287")
        mtxts.place(x = "46739", y = "7452")
        stbtn["text"] = "Начать сначала"
        stbtn.place(x="200", y="100")

    def scenery():

        sceneries = ["Цветочная поляна", "Огромный лес", "Горная долина"]

        scenerie = r.choice(sceneries)

        txt["text"] = scenerie
        
    # функции событий и их вызов. Зависит от рандома
    def game_process():
        gp = r.randint(0, 6)
        gameforme.lvlup()
        
        #gbtn["text"] = "Идти"
        
        if gp == 3:
            gameforme.meetmonster()
            
        elif gp == 2:
            gameforme.meetShop()
            
        elif gp == 1:
            gameforme.findtreasure()
            
        elif gp == 4:
            if bossdie == False:
                print("Босс жив")
            elif bossdie == True:
                print("Босс мёртв")
            gameforme.meetboss()
            
        else:
            gameforme.scenery()
        shtxtop.place(x="256439", y="25347835")
        lbtn.place(x="1213456", y="78901")
        bbtn.place(x="4567", y="98798")
        txt["text"] = "Вы покинули торговца"

    def lvlup():
        global exp
        global lvl
        global notgiv

        nexp = lvl*10
        print("у вас {0} опыта. Для повышения уровня надо {1} опыта".format(exp, nexp))

        if exp >= nexp:
            lvl += 1
            exp -= nexp
            lvluptxt["text"] = "Повышение уровня!"
            ltxtl["text"] = lvl
            lvluptxt.place(x="200", y="65")
            notgiv = True
            
        else:
            lvluptxt.place(x = "2753", y = "473")

        def forlvlup():
        
            global exp
            global lvl
            global hp
            global mana
            global damage
            global notgiv
        
            prize = r.randint(1, exp+1)
            if prize == exp+1:
                hp += 5
                mana += 5
                damage += 2
                htxtp["text"] = hp
                mtxta["text"] = mana
                print("У вас осталось",exp,"опыта")
                notgiv = False
                
            elif prize < exp and prize != 1:
                hp += 2
                mana += 2
                damage += 1
                htxtp["text"] = hp
                mtxta["text"] = mana
                print("У вас осталось",exp,"опыта")
                notgiv = False
                
            else:
                hp += exp+1
                mana += exp+1
                htxtp["text"] = hp
                mtxta["text"] = mana                
                damage += exp+1
                print("У вас осталось",exp,"опыта")
                notgiv = False

        if lvl > 1 and notgiv == True:
            forlvlup()
        else:
            print("Не достоин")

    def gamehelp():
        showerror(title="404 Not Founded", message="Страницы не существует!")

    def gameexit():
        exit()
        

# Кнопки, текста,  запуск окна и всего проекта в целом
mstxt = Label(text="Что будете делать?", bg="black", fg="white")
mtxts = Label(text="", fg = "white", bg = "black")
#отображение здоровья
htxtp = Label(fg="red", bg="black")
# отображение маны
mtxta = Label(fg="blue", bg="black")
# отображение уровня
ltxtl = Label(fg="brown", bg="black")
# отображение пенцов(монет)
ptxtc = Label(fg="yellow", bg="black")
#отображение уровня
lvluptxt = Label(fg ="white", bg = "black")
shtxtop = Label(text="", fg="white", bg="black")
lbtn = Button(text="Уйти", command=gameforme.leave)
bbtn = Button(text="Посмотреть", command=gameforme.pokupka)
stbtn = Button(text="Начать", command=gameforme.stadv, width=10, height=5)
stbtn.place(x="200", y="100")
#gbtn = Button(text="Идти", command=gameforme.game_process)
txt = Label(text="Ты начал своё путешествие", fg="white", bg="black")
nwtxt = Label(text="Не смей сдаваться. В твоих руках жизнь этого мира", fg="white", bg="black")
#менюшка
game_menu = Menu()
menu_file = Menu()
menu_file.add_command(label="Новая игра", command=gameforme.stadv)
#menu_file.add_command(label="Сохранить", command=gameforme.save)

game_menu.add_cascade(label="Игра", menu = menu_file)
game_menu.add_cascade(label="Помощь", command=gameforme.gamehelp)
game_menu.add_cascade(label="Выход", command = gameforme.gameexit)

k.add_hotkey("W", gameforme.game_process)
k.add_hotkey("Enter", gameforme.stadv)

win.config(menu=game_menu)
win.mainloop()
