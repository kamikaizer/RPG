import random
from engine import console, ask_choice, print_dream, show_panel

class Enemy:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack

    def is_alive(self):
        return self.hp > 0

def run_combat(player, enemy):
    console.clear()
    print_dream(f"¡Ha aparecido {enemy.name}!", delay=0.05)
    
    while player.hp > 0 and enemy.is_alive():
        show_panel("Estado", f"[bold green]{player.name} HP: {player.hp}/{player.max_hp}[/bold green]\n[bold red]{enemy.name} HP: {enemy.hp}/{enemy.max_hp}[/bold red]", style="cyan")
        
        choice = ask_choice("¿Qué harás?", ["Atacar", "Defender", "Usar Poción"])
        
        # Player turn
        if choice == 0:
            dmg = max(1, player.attack + random.randint(-3, 3))
            enemy.hp -= dmg
            print_dream(f"¡{player.name} ataca a {enemy.name} por {dmg} de daño!")
        elif choice == 1:
            print_dream(f"{player.name} adopta una postura defensiva.")
        elif choice == 2:
            heal = 30
            player.heal(heal)
            print_dream(f"¡{player.name} usa una poción y recupera {heal} HP!")
            
        if not enemy.is_alive():
            print_dream(f"¡Has derrotado a {enemy.name}!")
            console.input("\n[Presiona Enter para continuar]")
            return True
            
        # Enemy turn
        if choice == 1:
            enemy_dmg = max(1, enemy.attack - player.defense)
        else:
            enemy_dmg = max(1, enemy.attack - (player.defense // 2))
            
        enemy_dmg += random.randint(-2, 2)
        enemy_dmg = max(1, enemy_dmg)
        
        print_dream(f"¡{enemy.name} ataca a {player.name} por {enemy_dmg} de daño!")
        player.hp -= enemy_dmg
        
        if player.hp <= 0:
            print_dream(f"¡{player.name} ha caído en combate...")
            console.input("\n[Presiona Enter para continuar]")
            return False
            
        console.input("\n[Presiona Enter para continuar el combate]")
        console.clear()
