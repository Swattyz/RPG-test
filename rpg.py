import random

def race ():
    x = random.randint(1,100)
    y = random.randint(1,2)

    if x > 20:
        match y:
            case 1:
                return "Humano"
            case 2:
                return "Feral"
    elif 5 < x <= 20:
        match y:
            case 1:
                return "Demônio"
            case 2:
                return "Anjo"
    elif x <= 5:
        return "Ancestral"

def race_atk (race):
    match race:
        case "Humano":
            return 5
        case "Feral":
            return 8
        case "Demônio":
            return 10
        case "Anjo":
            return 6
        case "Ancestral":
            return 15

def race_df (race):
    match race:
        case "Humano":
            return 5
        case "Feral":
            return 6
        case "Demônio":
            return 8
        case "Anjo":
            return 4
        case "Ancestral":
            return 10

def race_mana (race):
    match race:
        case "Humano":
            return 200
        case "Feral":
            return 160
        case "Demônio":
            return 250
        case "Anjo":
            return 320
        case "Ancestral":
            return 400

def race_hp (race):
    match race:
        case "Humano":
            return 100
        case "Feral":
            return 110
        case "Demônio":
            return 130
        case "Anjo":
            return 150
        case "Ancestral":
            return 200

def class_atk (cl):
    match cl:
        case "Guerreiro":
            return 4
        case "Paladino":
            return 1
        case "Ladino":
            return 8
        case "Mago":
            return 5

def class_hp (cl):
    match cl:
        case "Guerreiro":
            return 0
        case "Paladino":
            return 20
        case "Ladino":
            return -40
        case "Mago":
            return -20
        
def class_df (cl):
    match cl:
        case "Guerreiro":
            return 0
        case "Paladino":
            return 5
        case "Ladino":
            return -3
        case "Mago":
            return -2
        
def class_mana (cl):
    match cl:
        case "Guerreiro":
            return 0
        case "Paladino":
            return -150
        case "Ladino":
            return -50
        case "Mago":
            return 200

def eff (offtype, deftype):
    if (deftype == "Pyro" and offtype == "Dendro") or (deftype == "Hydro" and offtype == "Pyro") or (offtype == "Dendro" and deftype == "Hydro"):
        return 2
    else:
        return 1

def dmg (atk,df,mana,res,eff):
    return ((atk - (df/2))*(mana/10))*(eff-(res/100))

def enemy_element ():
    x = random.randint(1,4)
    match x:
        case 1:
            return "Pyro"
        case 2:
            return "Hydro"
        case 3:
            return "Dendro"
        case 4:
            return "Anemo"

def enemy_encounter (difficulty):
    x = random.randint(1,2)
    match difficulty:
        case 1:
            match x:
                case 1:
                    return "Goblin"
                case 2:
                    return "Slime"
        case 2:
            match x:
                case 1:
                    return "Golem"
                case 2:
                    return "Demônio"
        case 3:
            match x:
                case 1:
                    return "Golem Ancestral"
                case 2:
                    return "Núcleo do Caos"
            
def enemy_hp (name):
    match name:
        case "Goblin":
            return 80
        case "Slime":
            return 50
        case "Golem":
            return 120
        case "Demônio":
            return 100
        case "Golem Ancestral":
            return 600
        case "Núcleo do Caos":
            return 400
        
def enemy_atk (name):
    match name:
        case "Goblin":
            return 6
        case "Slime":
            return 4
        case "Golem":
            return 8
        case "Demônio":
            return 10
        case "Golem Ancestral":
            return 12
        case "Núcleo do Caos":
            return 15

def enemy_df (name):
    match name:
        case "Goblin":
            return 4
        case "Slime":
            return 2
        case "Golem":
            return 8
        case "Demônio":
            return 12
        case "Golem Ancestral":
            return 20
        case "Núcleo do Caos":
            return 16
        
def xp_needed (lvl):
    match lvl:
        case 1:
            return 50
        case 2:
            return 100
        case 3:
            return 200
        case 4:
            return 350
        case 5:
            return 600

def attack_var (cl, element):
    x = random.randint(1,3)
    match cl:
        case "Guerreiro":
            match x:
                case 1:
                    return f"Corte {element}"
                case 2:
                    return f"Lâmina Mortal {element}"
                case 3:
                    return f"Punho Letal {element}"
        case "Paladino":
            match x:
                case 1:
                    return f"Grande Executor {element}"
                case 2:
                    return f"Tremor Pesado {element}"
                case 3:
                    return f"Lança Caótica {element}"
        case "Ladino":
            match x:
                case 1:
                    return f"Abate Furtivo {element}"
                case 2:
                    return "'Too Slow!'"
                case 3:
                    return f"Backstab {element}"
        case "Mago":
            match x:
                case 1:
                    return f"Esfera de {element}"
                case 2:
                    return f"Espinhos {element}"
                case 3:
                    return f"Flecha Elemental {element}"
        case "Goblin":
            match x:
                case 1:
                    return f"Flecha {element}"
                case 2:
                    return f"Soco {element}"
                case 3:
                    return f"Chute {element}"
        case "Slime":
            match x:
                case 1:
                    return f"Esfera Gosmenta de {element}"
                case 2:
                    return f"Agarrão {element}"
                case 3:
                    return f"Parasitismo {element}"
        case "Golem":
            match x:
                case 1:
                    return f"Punho Pesado {element}"
                case 2:
                    return f"Lança-Cristais {element}"
                case 3:
                    return f"Martelo {element}"
        case "Demônio":
            match x:
                case 1:
                    return f"Feixe {element}"
                case 2:
                    return f"Julgamento: {element}"
                case 3:
                    return f"Overload Infernal {element}"
        case "Golem Ancestral":
            match x:
                case 1:
                    return f"Raio-Laser {element}"
                case 2:
                    return f"Chuva de Meteoros {element}"
                case 3:
                    return f"Hiper-Martelo Tectônico {element}"
        case "Núcleo do Caos":
            match x:
                case 1:
                    return "Feixe da Morte"
                case 2:
                    return "Orbe Destruidor"
                case 3:
                    return "'Calamity'"

def stats_self(hp,maxhp,atk,df,mana,maxmana,xp,xpn,lvl,element):
    return f"\nSTATUS:\nLV {lvl} ({xp}/{xpn})\nHP {hp}/{maxhp} \nATK {atk} \nDEF {df} \nMANA {mana}/{maxmana} \nELEMENT: {element} \n"

def xp_gained(d20,difficulty):
    x = random.randint(0,50)
    match difficulty:
        case 1:
            return (6*d20)+x
        case 2:
            return (9*d20)+x
        case 3:
            return (15*d20)+x