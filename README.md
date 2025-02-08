# Flappy Bird AI Agent Using NEAT Algorithm

## Project Overview

This project implements an AI agent capable of playing and successfully beating the Flappy Bird game using the **NEAT (NeuroEvolution of Augmenting Topologies)** algorithm. The agent is trained through genetic algorithms, evolving its neural network to optimize its performance over time. The game is developed using the **Pygame** library, providing dynamic obstacles and realistic motion dynamics for a challenging and interactive environment.

## Features

- **Flappy Bird Game Environment**: A fully functional Flappy Bird game built in Pygame, complete with:
  - Dynamic obstacles (pipes)
  - Realistic gravity and bird movement
  - Scoring system

- **AI Agent Powered by NEAT**: The AI agent is trained using the NEAT algorithm, which evolves the agent's neural network to make decisions (flap or no flap) based on game states.
  
- **Genetic Algorithm Training**: The agent evolves over multiple generations, improving its ability to avoid pipes, stay in the air, and achieve a high score.
  
- **Game Visualization**: Visual representation of the AI's progress, showing the bird’s interactions with obstacles and the evolving neural network over time.

## How It Works

The agent learns to play Flappy Bird by evolving a population of neural networks. Each agent is a candidate neural network that takes the current game state (bird position, pipe position, etc.) as input and outputs a decision (flap or no flap).

- **NEAT Algorithm**: The neural networks are evolved using NEAT, which allows both the **topology** and the **weights** of the network to evolve, making it possible for the agent to learn more complex behaviors.
  
- **Training Process**:
  1. **Initialization**: A population of neural networks is initialized with random structures and weights.
  2. **Evaluation**: Each network is evaluated by playing the game, and its fitness is determined based on its score (distance traveled or number of pipes passed).
  3. **Selection and Reproduction**: The best-performing networks are selected to breed new generations, creating offspring that combine characteristics of their parents.
  4. **Mutation**: Random mutations are applied to the offspring, introducing new structures or behaviors.
  5. **Iteration**: The process repeats for multiple generations, with each generation improving the performance of the AI agent.

## Requirements

To run the project locally, ensure that you have the following installed:

- **Python 3.x**
- **Pygame** library
- **NEAT-Python** library (for the NEAT algorithm)

You can install the required dependencies using `pip`:

```bash
pip install pygame neat-python
```

## Running the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/flappy-bird-ai-neat.git
   cd flappy-bird-ai-neat
   ```
2. Run the main script to start the training process:
   ```bash
   python main.py
   ```
3. The game will start, and the AI agent will begin evolving over time. You can watch its progress as it gets better at playing the game.

## Project Structure

- **main.py**: The entry point of the project where the game and NEAT algorithm are initialized and executed.
- **game.py**: Contains the Flappy Bird game logic and environment (Pygame implementation).
- **neat.py**: Custom implementation or configuration of the NEAT algorithm.
- **config-feedforward.txt**: Configuration file for NEAT, specifying the network architecture and other settings.

## Training the AI Agent

The training process involves running the AI agent through multiple generations. It can take several minutes to several hours depending on the number of generations, population size, and other factors. The agent evolves gradually to optimize its ability to navigate the pipes and improve its score.

## Customization

- **Adjusting NEAT Parameters**: You can modify the `config-feedforward.txt` file to tweak the NEAT algorithm's parameters such as population size, mutation rate, and selection strategy.
- **Game Difficulty**: You can change the speed of obstacles, the frequency of pipes, and other in-game mechanics to increase or decrease the difficulty of the game.

## Future Improvements

- **Neural Network Visualization**: Implement visualization of the neural network’s structure and evolution.
- **Multiplayer Mode**: Add a multiplayer mode where multiple AI agents compete for the highest score.
- **Advanced Obstacles**: Introduce additional obstacles or challenges for the agent to overcome.
## Screenshot of the current AI gameplay
![image](https://github.com/user-attachments/assets/5b29716b-0cf0-47bc-87a5-33575c7c8a2e)
