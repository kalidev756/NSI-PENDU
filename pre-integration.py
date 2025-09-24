#imports
import time
import random

# ascii_art

gameover= '''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⠀⠀⠀⢀⣴⣿⡶⠀⣾⣿⣿⡿⠟⠛⠁
⠀⠀⠀⠀⠀⠀⣀⣀⣄⣀⠀⠀⠀⠀⣶⣶⣦⠀⠀⠀⠀⣼⣿⣿⡇⠀⣠⣿⣿⣿⠇⣸⣿⣿⣧⣤⠀⠀⠀
⠀⠀⢀⣴⣾⣿⡿⠿⠿⠿⠇⠀⠀⣸⣿⣿⣿⡆⠀⠀⢰⣿⣿⣿⣷⣼⣿⣿⣿⡿⢀⣿⣿⡿⠟⠛⠁⠀⠀
⠀⣴⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⢠⣿⣿⣹⣿⣿⣿⣿⣿⣿⡏⢻⣿⣿⢿⣿⣿⠃⣼⣿⣯⣤⣴⣶⣿⡤⠀
⣼⣿⠏⠀⣀⣠⣤⣶⣾⣷⠄⣰⣿⣿⡿⠿⠻⣿⣯⣸⣿⡿⠀⠀⠀⠁⣾⣿⡏⢠⣿⣿⠿⠛⠋⠉⠀⠀⠀
⣿⣿⠲⢿⣿⣿⣿⣿⡿⠋⢰⣿⣿⠋⠀⠀⠀⢻⣿⣿⣿⠇⠀⠀⠀⠀⠙⠛⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀
⠹⢿⣷⣶⣿⣿⠿⠋⠀⠀⠈⠙⠃⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣴⣶⣦⣤⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣠⡇⢰⣶⣶⣾⡿⠷⣿⣿⣿⡟⠛⣉⣿⣿⣿⠆
⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⡎⣿⣿⣦⠀⠀⠀⢀⣤⣾⠟⢀⣿⣿⡟⣁⠀⠀⣸⣿⣿⣤⣾⣿⡿⠛⠁⠀
⠀⠀⠀⠀⣠⣾⣿⡿⠛⠉⢿⣦⠘⣿⣿⡆⠀⢠⣾⣿⠋⠀⣼⣿⣿⣿⠿⠷⢠⣿⣿⣿⠿⢻⣿⣧⠀⠀⠀
⠀⠀⠀⣴⣿⣿⠋⠀⠀⠀⢸⣿⣇⢹⣿⣷⣰⣿⣿⠃⠀⢠⣿⣿⢃⣀⣤⣤⣾⣿⡟⠀⠀⠀⢻⣿⣆⠀⠀
⠀⠀⠀⣿⣿⡇⠀⠀⢀⣴⣿⣿⡟⠀⣿⣿⣿⣿⠃⠀⠀⣾⣿⣿⡿⠿⠛⢛⣿⡟⠀⠀⠀⠀⠀⠻⠿⠀⠀
⠀⠀⠀⠹⣿⣿⣶⣾⣿⣿⣿⠟⠁⠀⠸⢿⣿⠇⠀⠀⠀⠛⠛⠁⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠙⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'''

start_ascii='''
       _                        
       \`*-.                    
        )  _`-.                 
       .  : `. .                
       : _   '  \               
       ; *` _.   `*-._          
       `-.-'          `-.       
         ;       `       `.     
         :.       .        \    
         . \  .   :   .-'   .   
         '  `+.;  ;  '      :   
         :  '  |    ;       ;-. 
         ; '   : :`-:     _.`* ;
[bug] .*' /  .*' ; .*`- +'  `*' 
      `*-*   `*-*  `*-*'''

# stickman ascii art for each wrong attempt
stickman = [ '''


=========''', '''

      
      |
      |
      |
      |
      |
=========''', '''

  +---+       
     \|
      |
      |
      |
      |
=========''', '''
  +---+       
  |  \|
      |
      |
      |
      |
=========''', '''
  +---+          
  |  \|
  O   |
      |
      |
      |
=========''', '''
  +---+
  |  \|
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |  \|
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |  \|
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |  \|
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |  \|
  O   |
 /|\  |
 / \  |
      |
=========''']

# colors and decorations for terminal
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"
ORANGE = "\033[38;5;208m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
decorating_line = "-------------------------------------------------------------------"

default_wordlist = ["python", "programmation", "ordinateur", "clavier", "souris", "écran", "fenêtre", 
                   "algorithme", "variable", "fonction", "boucle", "condition", "classe", "objet",
                   "elephant", "girafe", "kangourou", "crocodile", "hippopotame", "rhinoceros"]

try:
    with open("listeMots.txt", "r", encoding="latin-1") as file:
        wordlist = [line.strip().lower() for line in file if line.strip()]
except FileNotFoundError:
    print("Fichier listeMots.txt non trouvé, utilisation de la liste par défaut")
    wordlist = default_wordlist


players = []
settings_time = None
settings_difficulty = "default"
is_random_word_generated = True
is_multiplayer = False

def spacement():
    for i in range(50):
        print("")

def display_pendus(player_errors, current_player_idx):
    if not is_multiplayer:
        return
    

    pendus = []
    for i, player in enumerate(players):
        error_count = len(player_errors[i])
        if error_count >= len(stickman):
            error_count = len(stickman) - 1
        pendus.append(stickman[error_count])
    

    lines_list = []
    max_lines = 0
    
    for pendu in pendus:
        lines = pendu.split('\n')
        lines_list.append(lines)
        max_lines = max(max_lines, len(lines))
    

    for lines in lines_list:
        while len(lines) < max_lines:
            lines.append("")
    

    max_widths = []
    for lines in lines_list:
        max_width = max(len(line) for line in lines) if lines else 15
        max_widths.append(max(max_width, 15))  
    

    player_names = []
    arrows = []
    for i, player in enumerate(players):

        player_display = f"{player} ({len(player_errors[i])}/10)"
        player_names.append(player_display.center(max_widths[i]))
      
        if i == current_player_idx:
            arrow_display = "▼▼▼▼▼▼▼▼▼▼".center(max_widths[i])
        else:
            arrow_display = " " * max_widths[i]
        arrows.append(arrow_display)
    
    print("    ".join(player_names))
    print("    ".join(arrows))
    print("    ".join("=" * width for width in max_widths))
    

    for line_index in range(max_lines):
        line_parts = []
        for i, lines in enumerate(lines_list):
            if line_index < len(lines):
                line_content = lines[line_index].ljust(max_widths[i])
            else:
                line_content = " " * max_widths[i]
            line_parts.append(line_content)
        print("    ".join(line_parts))

class GameSession:
    def __init__(self, players_list=None):
        self.players = players_list if players_list else ["Joueur"]
        self.word_decomposed = []
        self.success_letter_list = []
        self.player_errors = [[] for _ in self.players]  
        self.player_guessed = [[] for _ in self.players]  
        self.current_player = 0
        self.game_finished = False
        self.winners = []
        
    def word_generator(self):
        """Génère ou demande le mot à deviner"""
        if is_random_word_generated:
            if settings_difficulty == "easy":
                filtered_words = [word for word in wordlist if len(word) <= 5]
            elif settings_difficulty == "medium":
                filtered_words = [word for word in wordlist if 6 <= len(word) <= 8]
            elif settings_difficulty == "difficult":
                filtered_words = [word for word in wordlist if 9 <= len(word) <= 12]
            elif settings_difficulty == "hardcore":
                filtered_words = [word for word in wordlist if 13 <= len(word) <= 18]
            elif settings_difficulty == "impossible":
                filtered_words = [word for word in wordlist if len(word) > 18]
            else:
                filtered_words = wordlist
            
            if not filtered_words:
                filtered_words = wordlist
            
            choiced_word = random.choice(filtered_words).lower()
        else:
            spacement()
            choiced_word = input("Entrez le mot à deviner: ").lower().strip()
        
        self.word_decomposed = list(choiced_word)
        self.success_letter_list = ["_"] * len(self.word_decomposed)
        
    def display_game_state(self):
        """Affiche l'état actuel du jeu"""
        spacement()
        
        if is_multiplayer:
            print(f"{BLUE}=== TOUR DE {self.players[self.current_player].upper()} ==={RESET}")
            display_pendus(self.player_errors, self.current_player)
            print(decorating_line)
            
            for i, player in enumerate(self.players):
                if self.player_errors[i]:
                    print(f"{RED}{player} - Erreurs: {' '.join(self.player_errors[i])}{RESET}")
                else:
                    print(f"{GREEN}{player} - Aucune erreur{RESET}")
        else:
            error_count = len(self.player_errors[0])
            if error_count >= len(stickman):
                error_count = len(stickman) - 1
            print(stickman[error_count])
            print(decorating_line)
            if self.player_errors[0]:
                print(f"{RED}ERREURS: {' '.join(self.player_errors[0])}{RESET}")
        
        print(decorating_line)
        print(f"{GREEN}MOT: {' '.join(self.success_letter_list)}{RESET}")
        print(decorating_line)
    
    def make_guess(self, letter):
        """Traite une tentative de lettre"""
        letter = letter.lower()
        current_idx = self.current_player
        
      
        if letter in self.player_guessed[current_idx]:
            return "déjà_essayée"
        
        self.player_guessed[current_idx].append(letter)
        
        if letter in self.word_decomposed:

            positions = [i for i, l in enumerate(self.word_decomposed) if l == letter]
            for pos in positions:
                self.success_letter_list[pos] = letter
            
 
            if "_" not in self.success_letter_list:
                self.winners.append(self.players[current_idx])
                if not is_multiplayer:
                    self.game_finished = True
                return "gagné"
            return "trouvée"
        else:

            self.player_errors[current_idx].append(letter)
            
            if len(self.player_errors[current_idx]) >= 10:
                if is_multiplayer:
                    print(f"{RED}{self.players[current_idx]} a été éliminé!{RESET}")

                    remaining_players = [i for i, p in enumerate(self.players) 
                                       if len(self.player_errors[i]) < 10]
                    if len(remaining_players) <= 1:
                        self.game_finished = True
                else:
                    self.game_finished = True
                    return "perdu"
            return "pas_trouvée"
    
    def next_player(self):
        """Passe au joueur suivant (mode multijoueur)"""
        if not is_multiplayer:
            return
        
  
        attempts = 0
        while attempts < len(self.players):
            self.current_player = (self.current_player + 1) % len(self.players)
            if len(self.player_errors[self.current_player]) < 10:
                break
            attempts += 1
    
    def play(self):
        """Boucle principale du jeu"""
        self.word_generator()
        
        while not self.game_finished:
            self.display_game_state()
            
            try:
                user_input = input(f"Entrez une lettre: ").strip()
                
                if len(user_input) != 1 or not user_input.isalpha():
                    print("Merci d'entrer une seule lettre")
                     
                    continue
                
                result = self.make_guess(user_input)
                
                if result == "déjà_essayée":
                    print(f"Vous avez déjà essayé la lettre '{user_input}'")
                     
                elif result == "trouvée":
                    print(f"{GREEN}Bonne lettre!{RESET}")
                     
                elif result == "gagné":
                    spacement()
                    print(f"{GREEN} Félicitations {self.players[self.current_player]}! Vous avez trouvé le mot: {''.join(self.word_decomposed)} {RESET}")
                    if not is_multiplayer:
                        break
                elif result == "pas_trouvée":
                    print(f"{RED}Lettre non trouvée{RESET}")
                     
                elif result == "perdu":
                    spacement()
                    print(f"{RED}{gameover}{RESET}")
                    print(f"Vous avez perdu! Le mot était: {''.join(self.word_decomposed)}")
                    return
                
                if is_multiplayer and result != "trouvée":
                    self.next_player()
                
            except KeyboardInterrupt:
                print(f"\n{YELLOW}Jeu interrompu par l'utilisateur{RESET}")
                return
        
     
        self.display_final_results()
    
    def display_final_results(self):
        """Affiche les résultats finaux"""
        spacement()
        print(f"{BLUE}{'='*50}")
        print("           RÉSULTATS FINAUX")
        print(f"{'='*50}{RESET}")
        
        if self.winners:
            print(f"{GREEN} GAGNANT(S): {', '.join(self.winners)} {RESET}")
        
        print(f"\n{YELLOW}Statistiques des joueurs:{RESET}")
        

        player_stats = []
        for i, player in enumerate(self.players):
            errors = len(self.player_errors[i])
            guesses = len(self.player_guessed[i])
            status = "GAGNANT" if player in self.winners else "ÉLIMINÉ" if errors >= 10 else "EN JEU"
            player_stats.append((player, errors, guesses, status))
        
        player_stats.sort(key=lambda x: x[1])  
        
        for i, (player, errors, guesses, status) in enumerate(player_stats, 1):
            color = GREEN if status == "GAGNANT" else RED if status == "ÉLIMINÉ" else YELLOW
            print(f"{i}. {color}{player}{RESET}")
            print(f"   Erreurs: {errors}/10")
            print(f"   Tentatives totales: {guesses}")
            print(f"   Statut: {color}{status}{RESET}")
            if self.player_errors[self.players.index(player)]:
                print(f"   Lettres erronées: {', '.join(self.player_errors[self.players.index(player)])}")
            print()
        
        print(f"Mot à deviner: {BLUE}{''.join(self.word_decomposed).upper()}{RESET}")

def menu():
    """Menu principal du jeu"""
    global settings_time, settings_difficulty, is_random_word_generated, is_multiplayer, players
    
    while True:
        spacement()
        print(f"{GREEN}{start_ascii}{RESET}")
        print(" Bienvenue dans le jeu du Pendu ! ")
        print(decorating_line)
        print("1. Mode Solo")
        print("2. Mode Multijoueur")
        print("3. Paramètres")
        print("4. Quitter")
        print(decorating_line)
        print(f"Paramètres actuels: TEMPS={settings_time}s, DIFFICULTÉ={settings_difficulty}")
        
        choice = input("Choisissez une option (1-4): ").strip()
        
        if choice == '1':

            players = ["Joueur"]
            is_multiplayer = False
            
            spacement()
            print(f"{GREEN}{start_ascii}{RESET}")
            print(decorating_line)
            print("1. Génération aléatoire du mot")
            print("2. Mot saisi par un tiers")
            print("3. Retour au menu")
            
            sub_choice = input("Choix: ").strip()
            
            if sub_choice == "1":
                is_random_word_generated = True
                game = GameSession(players)
                game.play()
                input("\nAppuyez sur Entrée pour continuer...")
            elif sub_choice == "2":
                is_random_word_generated = False
                game = GameSession(players)
                game.play()
                input("\nAppuyez sur Entrée pour continuer...")
            elif sub_choice == "3":
                continue
                
        elif choice == '2':
            # Mode multijoueur
            is_multiplayer = True
            players = []
            
            try:
                num_players = int(input("Nombre de joueurs (2-6): "))
                if num_players < 2 or num_players > 6:
                    print("Nombre de joueurs invalide (2-6 joueurs)")
                     
                    continue
                
                for i in range(num_players):
                    name = input(f"Nom du joueur {i+1}: ").strip()
                    if not name:
                        name = f"Joueur{i+1}"
                    players.append(name)
                
                print("\n Règles du multijoueur:")
                print("- Chaque joueur joue à tour de rôle")
                print("- Les erreurs sont individuelles (10 max par joueur)")
                print("- Le premier à compléter le mot gagne")
                print("- Les joueurs éliminés ne peuvent plus jouer")
                
                input("\nAppuyez sur Entrée pour commencer...")
                
                game = GameSession(players)
                game.play()
                input("\nAppuyez sur Entrée pour continuer...")
                
            except ValueError:
                print("Veuillez entrer un nombre valide")
                 
                
        elif choice == '3':
            spacement()
            print("  PARAMÈTRES")
            print(decorating_line)
            print("1. Temps par tour")
            print("2. Difficulté")
            print("3. Retour")
            
            setting_choice = input("Choix: ").strip()
            
            if setting_choice == "1":
                try:
                    time_input = input("Temps en secondes (0 pour illimité): ")
                    settings_time = int(time_input) if time_input != "0" else None
                    print(f"{GREEN}Temps configuré!{RESET}")
                      
                except ValueError:
                    print("Valeur invalide")
                      
                    
            elif setting_choice == "2":
                print("Difficultés disponibles:")
                print("- easy: mots ≤ 5 lettres")
                print("- medium: mots 6-8 lettres")
                print("- difficult: mots 9-12 lettres") 
                print("- hardcore: mots 13-18 lettres")
                print("- impossible: mots > 18 lettres")
                print("- default: tous les mots")
                
                diff_input = input("Difficulté: ").strip().lower()
                if diff_input in ["easy", "medium", "difficult", "hardcore", "impossible", "default"]:
                    settings_difficulty = diff_input
                    print(f"{GREEN}Difficulté configurée!{RESET}")
                else:
                    print("Difficulté invalide")
                  
                
        elif choice == '4':
            print(" Au revoir!")
            break
            
        else:
            print("Option invalide")
             

def main():
    """Fonction principale"""
    try:
        menu()
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Jeu interrompu. Au revoir!{RESET}")
    except Exception as e:
        print(f"{RED}Une erreur est survenue: {e}{RESET}")

if __name__ == "__main__":
    main()