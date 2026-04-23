print ("15/04/2026")
import rpg
import json
import random

with open("characters.json", "r") as f:
    personagens = json.load(f)

v = True
while v:
    try:
        choice = int(input ("\n------- ELEMENTRA -------- \nBem vindo ao Elementra RPG! Você deseja ENTRAR (1), CRIAR PERSONAGEM (2) ou SAIR (3)? "))
    except Exception as e:
        print ("\nOpção inválida! Tente novamente.")
        continue

    if choice == 1:
        while True:
            CharName = input ("\nInsira o nome do seu personagem: ").strip()
            if CharName in personagens:
                print (f"\nPersonagem encontrado...\n")

                hp = personagens[CharName]["hp"]
                maxhp = hp
                atk = personagens[CharName]["atk"]
                df = personagens[CharName]["df"]
                mana = personagens[CharName]["mana"]
                maxmana = mana
                element = personagens[CharName]["element"]
                lvl = personagens[CharName]["lvl"]
                xp = personagens[CharName]["xp"]
                xpn = rpg.xp_needed(lvl)
                cl = personagens[CharName]["class"]
                race = personagens[CharName]["race"]

                print (f"\n'{CharName}' {rpg.stats_self(hp,maxhp,atk,df,mana,maxmana,xp,xpn,lvl,element)}CLASS: {cl} \nRACE: {race}")
                
                choice = input("\nEntrar? ('s'/'n') ")
                if choice == "s":
                    v = False
                    break
                elif choice == "n":
                    continue  
                else:
                    print ("\nOpção inválida, tente novamente.")
                    continue
            else:
                choice = input("\nPersonagem não encontrado! Pressione 'Enter' para tentar novamente, ou '0' para sair --> ")
                if choice == "0":
                    break
    
    elif choice == 2:
        while True:
            CharName = input("\nInsira o nome do seu novo personagem: ").strip()
            if (CharName == "") or (CharName in personagens):
                print ("\nErro: o nome está vazio ou já existe! Tente novamente.")
                continue
            
            input (f"Ótimo! Agora, {CharName}, vamos rolar os dados~ (aperte 'Enter')")
            x = True
            count = 0
            while x:
                input (f"\nVocê somente possui {3-count} chance(s) de troca de RAÇAS! Cada raça te dá diferentes status base e - por enquanto - somente existem 5 disponíveis, 2 comuns (70%), 2 raras (25%) e 1 lendária (5%)! ('Enter')")
                race = rpg.race()
                count += 1
            
                print (f"Você tirou... {race}!\n")
                if count <= 3:
                    while True:
                        choice = input ("\nQuer rolar denovo, SIM ('s') ou NÃO ('n')? ")
                        if choice == "n":
                            x = False
                            break
                        elif choice == "s":
                            break
                        else:
                            print ("\nErro: opção inválida! Tente novamente.")
                else:
                    break
            
            while True:
                try:
                    choice = int(input (f"\n\n{CharName} da raça {race}, qual das classes abaixo deseja? \nGUERREIRO ('1'): Mudança de status quase nula, apenas um guerreiro comum. \nPALADINO ('2'): Muito maior DEFESA e HP, porém péssima capacidade de magia e menor ATK. \nLADINO ('3'): Grande ATK porém menor capacidade de DEFESA e HP. \nMAGO ('4'): Enorme capacidade de MANA, porém frágil. \n--> "))
                except Exception as e:
                    print (f"\nErro {e}: Opção inválida, tente novamente.")
                    continue
                
                match choice:
                    case 1:
                        cl = "Guerreiro"
                        break
                    case 2:
                        cl = "Paladino"
                        break
                    case 3:
                        cl = "Ladino"
                        break
                    case 4:
                        cl = "Mago"
                        break
                    case _:
                        print ("\nOpção inválida! Tente novamente.")
                        continue
            
            while True:
                try:
                    choice = int(input ("\nÚltima parada! Escolha um elemento: \nPYRO ('1') \nHYDRO ('2') \nDENDRO ('3') \nANEMO ('4') \n--> "))
                except Exception as e:
                    print (f"\nErro {e}: Opção inválida! Tente novamente.")
                    continue

                match choice:
                    case 1:
                        element = "Pyro"
                        break
                    case 2:
                        element = "Hydro"
                        break
                    case 3:
                        element = "Dendro"
                        break
                    case 4:
                        element = "Anemo"
                        break
                    case _:
                        print ("\nOpção inválida! Tente novamente.")
                        continue
            
            atk = rpg.race_atk(race) + rpg.class_atk(cl)
            hp = rpg.race_hp(race) + rpg.class_hp(cl)
            maxhp = hp
            df = rpg.race_df(race) + rpg.class_df(cl)
            mana = rpg.race_mana(race) + rpg.class_mana(cl)
            maxmana = mana
            xp = 0
            lvl = 1
            xpn = rpg.xp_needed(lvl)

            personagens[CharName] = {
                "hp": int(hp),
                "atk": int(atk),
                "df": int(df),
                "mana": int(mana),
                "xp": 0,
                "lvl": 1,
                "element": element,
                "class": cl,
                "race": race
            }

            with open("characters.json", "w") as f:
                json.dump(personagens, f, indent=4)

            break

    elif choice == 3:
        print ("\nPrograma finalizado!")
        v = False
        quit()

    else:
        print ("\nErro: opção inválida! Tente novamente.")

count = 0
turno = 1
dmgr = 0
difficulty = 1
enemy = rpg.enemy_encounter(difficulty)
ehp = rpg.enemy_hp(enemy)
eatk = rpg.enemy_atk(enemy)
edf = rpg.enemy_df(enemy)
enemy_element = rpg.enemy_element()

input(f"\n\n{CharName}... {CharName}!... \n\nVocê se encontra deitado no meio de um óasis estranho... Seu corpo está pesado. (Pressione 'Enter')")
input("\nVocê percebe que há uma entrada para uma grande floresta ali perto, como lhe parece sua única opção, você vai até lá... (Pressione 'Enter')")
input(f"\nUm {enemy} selvagem apareceu! (Pressione 'Enter')")

a = True
while a:
    input (rpg.stats_self(hp,maxhp,atk,df,mana,maxmana,xp,xpn,lvl,element))

    try:
        choice = int(input(f"O que você quer fazer? O {enemy} ainda resta {ehp} de HP! \nATACAR (1) \nDEFENDER (2) \nCHECK (3) \nFUGIR (4) \n--> "))
    except Exception as e:
        print (f"Erro {e}: opção inválida! Tente novamente.")
        continue

    if choice == 1:
        d20 = random.randint(1,20)
        print ("\nVocê prepara sua arma em posição ofensiva...")

        if d20 >= 10:
            while True:
                try:
                    attack_mana = int(input(f"\n{CharName}, quanta MANA vai querer usar no golpe? (MANA ATUAL: {mana}/{maxmana}) "))
                except:
                    print ("Opção inválida! Tente novamente.")
                    continue

                if attack_mana < 10:
                    print ("\nMuita pouca MANA! Gastar menos que 10 de MANA é impossível para um ataque elemental!")
                    continue
                
                elif attack_mana > mana:
                    print (f"\nMuita MANA usada! Lembre, você possui {mana} de MANA atualmente!")
                    continue

                break
            
            mana -= attack_mana
            if mana == 0:
                print (f"\nVocê usou MANA demais! Ficou com {mana} de MANA e desmaiou... Tirou 10 do próprio HP para recuperar MANA suficiente para continuar!")
                mana += 20
                hp -= 10

                if hp <= 0 and count != 2:
                    input (f"\n{CharName}!... Você... Não pode perder aqui!... \nSeu coração se preenche de DETERMINAÇÃO, e você ganha vontade suficiente pra continuar!")
                    hp = 30
                    count += 1
        
                elif hp <= 0 and count == 2:
                    print ("Você ficou com muito pouco HP e desmaiou! \n\nG A M E     O V E R .")
                    break

            attack = rpg.attack_var(cl,element)
            effect = rpg.eff(element,enemy_element)
            dmg = rpg.dmg(atk,edf,attack_mana,0,effect)

            print (f"\nVocê se concentrou suficiente e desfere um {attack} em cheio!")

            if dmg < 0:
                dmg = 0

            if d20 >= 19:
                dmg = (dmg*1.5)

                print (f"\nACERTO CRÍTICO! Causou {dmg} de dano!")
            
            else:
                input (f"\nCausou {dmg} de dano!")
            
            if effect == 2:
                print ("\nFoi um golpe super-eficaz!")
            
            ehp -= dmg

            if ehp <= 0:
                print (f"\nO {enemy} ficou com 0 de HP! Você venceu! \nRECEBEU {6*d20} DE EXP.")
                xp += rpg.xp_gained(d20,difficulty)
                turno += 1
                lvl_antigo = lvl

                while xp >= xpn:
                    xp -= xpn
                    lvl += 1
                    atk += 4
                    hp += 20
                    maxhp += 20
                    df += 2
                    mana += 40
                    maxmana += 40
                    xpn = rpg.xp_needed(lvl)

                    print (f"\nParabéns! Você upou de nível! \n( LV {lvl_antigo} --> {lvl} ) ( {xp} / {xpn} )")
            
        elif d20 == 1:
            print ("\nUh-oh!... Você perdeu totalmente seu foco... Caiu no chão no meio de sua perfomance e levou dano por isso!")
            hp -= 5

        else:
            print ("\nVocê falhou em se concentrar e acabou perdendo o foco no ataque...")

    elif choice == 2:
        d20 = random.randint(1,20)

        if cl == "Mago":
            print (f"\nSuas habilidades mágicas brilham... \nVocê usou a magia 'Encantamento Regenerativo' e conseguiu curar {d20*1.5} de HP! \nVocê manteve a defensiva nesse turno.")
            dmgr = 2
            hp += (d20*1.5)

            if hp > maxhp:
                hp = maxhp
        
        print ("\nVocê mantém uma postura de defesa...")

        if d20 >= 10:
            print ("\nConseguiu uma boa postura e redução de dano!")
            dmgr = int(d20/2)
        
        elif d20 < 10:
            print ("\nBem, valeu a tentativa...")
            dmgr = int(d20/3)

    elif choice == 3:
        input (f"\nVocê dá uma boa olhada no seu inimigo... \n'{enemy}' \nHP {ehp} \nATK {eatk} \nDEF {edf} \nELEMENT: {enemy_element} \n")

    elif choice == 4:
        d20 = random.randint(1,20)
        if cl == "Ladino":
            d20 += 2
        input ("\nVocê coloca suas habilidades furtivas em prática... (Pressione 'Enter')")

        if d20 < 10:
            print (f"\nVocê falhou... Caiu no chão ao tentar fugir e levou dano! Que tragédia. \nO {enemy} se sentiu ofendido pela sua falha tentativa e ficou mais agressivo.")
            eatk += 2
            hp -= 5

        elif d20 >= 10:
            print (f"\nVocê conseguiu! Conseguiu fugir. \nVOCÊ RECEBEU 0 DE EXP. ({xp}/{xpn})")
            ehp = 0
            turno += 1

    else:
        print ("\nOpção inválida, tente novamente.")
        continue

    if hp <= 0 and count != 2:
            input (f"\n{CharName}!... Você... Não pode perder aqui!... \nSeu coração se preenche de DETERMINAÇÃO, e você ganha vontade suficiente pra continuar!")
            hp = 30
            count += 1
        
    elif hp <= 0 and count == 2:
        print ("Você ficou com muito pouco HP e desmaiou! \n\nG A M E     O V E R .")
        break
    
    if ehp > 0:
        input (f"\nO {enemy} prepara seu ataque...")
        d20 = random.randint(1,20)

        if d20 >= 5:
            attack = rpg.attack_var(enemy,enemy_element)
            effect = rpg.eff(enemy_element,element)
            dmg = rpg.dmg(eatk,(df+dmgr),10,0,effect)

            print (f"\nO {enemy} te ataca com {attack}!")

            if dmg < 0:
                dmg = 0
        
            if d20 >= 19:
                dmg = dmg*1.5

                input (f"\nUh-oh! O seu inimigo fez um ACERTO CRÍTICO e causou {dmg} de dano!")
        
            else:
                input (f"\nO seu inimigo te causou {dmg} de dano!")

            if effect == 2:
                print ("\nFoi um golpe super-eficaz!")

            hp -= dmg
        
        else:
            input (f"\nO {enemy} perdeu concentração!")
    
        if hp <= 0 and count != 2:
            input (f"\n{CharName}!... Você... Não pode perder aqui!... \nSeu coração se preenche de DETERMINAÇÃO, e você ganha vontade suficiente pra continuar!")
            hp = 30
            count += 1
        
        elif hp <= 0 and count == 2:
            print ("Você ficou com muito pouco HP e desmaiou! \n\nG A M E     O V E R .")
            break
        
    if mana < maxmana:
        print ("\nPassou um turno e recuperou-se um pouco de MANA.")
        mana += 30

        if mana > maxmana:
            mana = maxmana
    
    if turno == 2:
        difficulty = 2
        turno += 1
        dmgr = 0
        enemy = rpg.enemy_encounter(difficulty)
        ehp = rpg.enemy_hp(enemy)
        eatk = rpg.enemy_atk(enemy)
        edf = rpg.enemy_df(enemy)
        enemy_element = rpg.enemy_element()

        input(f"\n\n...{CharName} lutou bravamente contra o inimigo e seguiu adiante na floresta... (Pressione 'Enter')")
        input("\nAlguns minutos se passam na mesma trilha, até notar um grande castelo. (Pressione 'Enter')")
        print("\n\nELEMENTRA - SELVAS VERDEJANTES: CASTELO PERDIDO")
        input("\nApós uma caminhada nos corredores abandonados desse castelo, você encontra um inimigo!"
        f"\nUm {enemy} te para antes que você possa ultrapassar aquela porta gigante no final do grande corredor! (Pressione 'Enter')")
    
    if turno == 4:
        difficulty = 3
        turno += 1
        dmgr = 0
        enemy = rpg.enemy_encounter(difficulty)
        ehp = rpg.enemy_hp(enemy)
        eatk = rpg.enemy_atk(enemy)
        edf = rpg.enemy_df(enemy)
        enemy_element = rpg.enemy_element()

        input (f"\n\n{CharName} o derrotou com perfomance impecável! Você continua lentamente até a grande porta, abrindo-a lentamente devido ao seu grande peso... (Pressione 'Enter')")
        input (f"\n...Uma enorme sala se revela junto com um {enemy} furioso!")

    if turno == 6:
        input (f"{CharName}... Parabéns, você venceu a legião do mal na nação verdejante e obteve a JÓIA ELEMENTAL DENDRO!"
               "\nAssim, salvou toda a região das Selvas Verdejantes do Definhamento. (Pressione 'Enter')")
        input (f"As pessoas da vila te reconhecem como herói, mas sua aventura só acabou de começar... \n\nF I M . (Pressione 'Enter' para finalizar)")
        break

# json.dump (f) --> salva
# json.load (f) --> carrega

# json é um tipo de txt usado mais diretamente pra codigos, não somente o texto