from config import T
from environment import Environment
from human import Human
from player import Player
from play_game import play_game
from utils.get_state_hash_and_winner import get_state_hash_and_winner
from utils.initialV import initialV_x, initialV_o


if __name__ == "__main__":
    p1 = Player()
    p2 = Player()

    # Set initial V for p1 and p2
    env = Environment()
    state_winner_triples = get_state_hash_and_winner(env)

    Vx = initialV_x(env, state_winner_triples)
    p1.setV(Vx)
    Vo = initialV_o(env, state_winner_triples)
    p2.setV(Vo)

    # Give each player their symbol
    p1.set_symbol(env.x)
    p2.set_symbol(env.o)
    # Training AI vs AI
    for t in range(T):
        if t % 500 == 0:
            print(t)
        play_game(p1, p2, Environment())

    # Play human vs AI agent
    human = Human()
    human.set_symbol(env.o)
    while True:
        p1.set_verbose(True)
        play_game(p1, human, Environment(), draw=2)
        answer = input("Play again? [Y/n]: ")
        if answer and answer.lower()[0] == "n":
            break
