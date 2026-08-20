from engine import console, print_office, print_dream, ask_choice, print_quest_log, clear_screen, show_panel
from combat import Enemy, run_combat

def play_day_1(player):
    clear_screen()
    print_quest_log(1, "Busca a quien se ahoga en un mar de tinta blanca antes del almuerzo.")
    console.input("\n[Presiona Enter para despertar]")
    
    clear_screen()
    show_panel("08:00 AM - OmniCorp", "Mundo Real", style="grey53")
    print_office("La alarma suena. Te levantas con el peso de la rutina.")
    print_office("Llegas a OmniCorp, el edificio gris donde trabajas como Analista de Fraude.")
    print_office("El jefe Balor te grita frente a todos por un reporte imposible de cuadrar.")
    
    print_office("\nMás tarde, vas a la máquina de café. Hace un ruido espantoso y escupe un líquido que mancha tu camisa.")
    
    print_office("\nRecuerdas el Quest Log: 'Busca a quien se ahoga en un mar de tinta blanca'.")
    choice = ask_choice("¿Qué haces?", [
        "Ir al área de archivo para revisar si Sara (Auditora) necesita ayuda.",
        "Ignorar el sueño y volver a tu cubículo a trabajar en tus reportes."
    ])
    
    if choice == 0:
        print_office("\nVas al archivo. Sara está rodeada de carpetas, al borde de un ataque de ansiedad.")
        print_office("Decides ayudarla a organizar los documentos físicamente.")
        print_office("Sara te sonríe, aliviada. Sientes que has hecho lo correcto.")
        player.affinity["Sara"] += 1
        success = True
    else:
        print_office("\nVuelves a tu escritorio. Ignoras los problemas de los demás.")
        print_office("Sientes una acumulación de estrés por el ambiente pesado.")
        player.increase_burnout(1)
        success = False
        
    console.input("\n[Presiona Enter para volver a casa y dormir]")
    return success

def play_night_1(player, success):
    clear_screen()
    show_panel("23:00 - Aethelgard", "Reino de los Sueños", style="cyan")
    
    print_dream("Abres los ojos. Ya no estás en tu cuarto gris.")
    print_dream("Llevas una armadura brillante (con una extraña mancha oscura en el pecho).")
    print_dream("Frente a ti se encuentra Sir Catsby, un caballero felino tuerto.")
    print_dream("'Guerrero Contable, el equilibrio te necesita', dice el gato.")
    
    console.input("\n[Presiona Enter]")
    clear_screen()
    
    if success:
        print_dream("Sientes una gran energía tras haber ayudado a Sara en el mundo de luz.")
    else:
        print_dream("Sientes una pesadez extraña. La sombra del Burnout te debilita.")
        player.take_damage(20)
    
    print_dream("\nDe pronto, un monstruo aparece: El Espíritu de Vapor (versión monstruosa de la máquina de café).")
    
    enemy = Enemy("Espíritu de Vapor", 50, 8)
    won = run_combat(player, enemy)
    
    if won:
        print_dream("\nHas derrotado a la pesadilla. Encuentras la Espada de la Resolución.")
        player.attack += 5
    else:
        print_dream("\nDespiertas sudando frío. La pesadilla te venció esta vez...")
        player.heal(100) # Heal to full for next day anyway, it's just a dream
    
    console.input("\n[Presiona Enter para avanzar al siguiente día]")

def play_stage_1(player):
    success = play_day_1(player)
    play_night_1(player, success)
    player.day += 1
