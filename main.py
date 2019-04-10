import argparse
from src.View import View
from src.Scrabble import Scrabble
from src.Agent import Agent
from src.Minimax import Minimax

# Parsing command line arguments
parser = argparse.ArgumentParser()

parser.add_argument('-s', dest='size', type=int)
parser.add_argument('-b', dest='blanks', action='store_true')
results = parser.parse_args()

if not results.size:
    results.size = 15

# Setting up the game with two players
state = Scrabble(blanks=results.blanks, size=results.size)
agent_0 = Agent()
agent_1 = Agent()
state.add_agent(0, agent_0)
state.add_agent(1, agent_1)
print(agent_0.tiles)
state.draw(0)
print(agent_0.tiles)
state.place('NARKS', [(7, 5), (7, 6), (7, 7), (7, 8), (7, 9)], 0)
print(state.board)
print(agent_1.tiles)
state.draw(1)
print(agent_1.tiles)
print(state.get_legal_moves(1)[:10])

# Play
# agents = state.agents.keys()
# while not state.is_over():
#     for agent in agents:
#         state.draw(agent)
#         best_move = Minimax(agent).get_best_word(state, agent, 1)
#         state.place(agent, best_move)
