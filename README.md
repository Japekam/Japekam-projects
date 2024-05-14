# **Dart Game Simulation**
* This program simulates a simplified dart game with two players.
* In each turn, players throw darts at a dartboard, and scores are determined based on the distance from the center.
* The game persists until a player achieves a predefined maximum score.
* The program provides a user-friendly interface to input player names and displays the winner along with game statistics.

## **Implementation**:

### ***Point Class***

1. Represents a single dart throw's landing position on the dartboard.
2. Calculates a score based on its distance from the center (0, 0).
3. Closer throws (distance <= 1) score 100, followed by decreasing scores for further distances.

### ***Player Class***

1. Models a player with a name, a list of thrown darts (Point objects), and their total score.
2. Simulates a dart throw by generating a random Point object and adding it to the player's throws.
3. Calculates the score for the latest throw and provides methods to access player name and total score.

### ***DartGame Class***

1. Manages the entire game flow, including player setup, round progression, and winner announcement.
2. Welcomes players, facilitates name input, and initializes the game with a set maximum score.
3. Each round involves both players throwing darts, with score updates provided.
4. The game ends when a player reaches the maximum score, and the winner is declared.
5. Final statistics, including the number of rounds played and individual player scores, are displayed.

### Extra
* Uses random module for dart throw variability (with fixed seed for consistent testing). Max_score parameter in DartGame allows adjusting the winning threshold.
