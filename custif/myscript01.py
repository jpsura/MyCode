#!/usr/bin/env python3
message = 'The movie is about to begin, we recommend '
print('what is your connection speed in mbps')
connection = float(input())
if connection >= 25:
    message = message + 'setting video to 4K'
elif connection >= 5:
    message = message + 'setting video to 1080p'
elif connection >= 2:
    message = message + 'setting video to 720p'
else:
    message = message + 'finding another network access'
print(message)

