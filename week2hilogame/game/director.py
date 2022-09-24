from re import L
from game.card import Card


class Director:
    #Players points and guess
    points_for_players = 300
    guess = ""
    

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """

        
        self.is_playing = True
        card = Card()
        self.card = card.card_num
        self.continue_game = True
        self.next_card = 0
        

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        print("You starting points is " + str(Director.points_for_players) + "\n")
        while self.is_playing:
            self.reveal_previous_card()
            guess = self.get_the_guess_of_the_player()
            if guess == 'l' or guess == 'h':
                next_card = Card()
                self.next_card = next_card.card_num
                self.reveal_next_card()
                Director.check_inputs_and_update_points(guess, self.card, self.next_card, Director.points_for_players)
                self.compare_previous_and_current_card_and_then_updates()
                self.check_if_players_points_is_not_below_or_equal_to_zero_and_if_player_still_wants_to_play_the_game()
                
            else:
                print("Invalid input")
                print("You points is still " + str(Director.points_for_players))
                print("The card is still " + str(self.card) + "\n")

    
    def compare_previous_and_current_card_and_then_updates(self):
        if self.next_card == self.card:
            pass
        else:
            self.card = self.next_card

    @classmethod        
    def check_inputs_and_update_points(cls, guess, card, next_card, points_for_players):
        cls.card = card
        cls.next_card = next_card
        cls.guess = guess
        cls.points_for_players = points_for_players
        if cls.next_card > cls.card and cls.guess == 'h':
            Director.points_for_players += 100
            print("Your points is now "+ str(Director.points_for_players))
            
        elif cls.next_card < cls.card and cls.guess  == 'l':
            Director.points_for_players += 100
            print("Your points is now "+ str(Director.points_for_players))
            
        elif cls.next_card < cls.card and cls.guess == 'h':
            Director.points_for_players -= 75
            print("Your points is now "+ str(Director.points_for_players))
            
        elif cls.next_card > cls.card and cls.guess == 'l':
            Director.points_for_players -= 75
            current_points = Director.points_for_players
            print("Your points is now "+ str(current_points))
            
        elif (cls.next_card == cls.card) and (cls.guess == 'l' or cls.guess == 'h'):
            Director.points_for_players += 0
            print("Cards are equal. No points added.")
            print("The number of points is still " + str(Director.points_for_players))
                       
            
    def show_points(self):
        print("Your score is " + str(self.points_for_players))

    def reveal_previous_card(self):
        print("The card is " + str(self.card))

    def check_if_players_points_is_not_below_or_equal_to_zero_and_if_player_still_wants_to_play_the_game(self):
        current_points = Director.points_for_players
        if current_points <= 0:
            print("You points is now below or equal to 0.")
            print("Game Over!")
            self.is_playing = False
        else:
            self.director_checks_if_player_wants_to_continue()

    def reveal_next_card(self):
        print("Next card was " + str(self.next_card))

    def get_the_guess_of_the_player(self):
        players_guess = input("Higher or lower? [h/l] ")
        return players_guess

    def director_checks_if_player_wants_to_continue(self):
        answer = input("Do you still want to play the game?[y/n] ").lower()
        if answer == 'y':
            print("")
        elif answer == 'n':
            print("Game over!")
            self.is_playing = False
        else:
            self.director_tells_you_invalid_y_or_n_if_invalid_input()

    def director_tells_you_invalid_y_or_n_if_invalid_input(self):
        print("\nYou did not enter a correct response")
        print("Your points is still: " + str(Director.points_for_players))
        print("Card number is still: " + str(self.card))
        self.director_checks_if_player_wants_to_continue()