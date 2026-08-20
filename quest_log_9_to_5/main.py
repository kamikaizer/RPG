from engine import console, clear_screen, show_panel
from player import Player
from story import play_stage_1

def main():
    clear_screen()
    show_panel("Quest Log: 9 to 5", "Bienvenido a la aventura. \nDe oficinista a Héroe JRPG.", style="bold magenta")
    console.input("\n[Presiona Enter para comenzar]")
    
    player = Player()
    
    # Game Loop for Day 1
    if player.day == 1:
        play_stage_1(player)
        
    clear_screen()
    show_panel("Fin de la Demo", "¡Felicidades! Has completado el Día 1.\nPara jugar los 14 días restantes, deberás seguir desarrollando la historia.", style="bold green")
    
if __name__ == "__main__":
    main()
