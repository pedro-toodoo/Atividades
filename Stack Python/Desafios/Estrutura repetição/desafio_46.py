import time
import emoji

for i in range(10, -1, -1):
    print(f"{i}")
    time.sleep(1)
print(emoji.emojize(":fireworks: :fireworks: :fireworks:", use_aliases=True))