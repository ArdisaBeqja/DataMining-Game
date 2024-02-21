import pandas as pd
import matplotlib.pyplot as plt

with open('scores.txt', 'r') as file:
    lines = file.readlines()

player_scores = []

for line in lines:
    player, score_part = line.split(':')
    
    player_name = player.strip()
    score = int(score_part.split('points')[0].strip())
    
    player_scores.append({'Player': player_name, 'Score': score})

df = pd.DataFrame(player_scores)

plt.figure(figsize=(8, 6))
plt.bar(df['Player'], df['Score'], color=['blue', 'green'])
plt.title('Player Scores')
plt.xlabel('Player')
plt.ylabel('Score')
plt.show()
