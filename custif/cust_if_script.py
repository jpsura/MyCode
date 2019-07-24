#!/usr/bin/env python3
message = 'The score you obtained shows us that you '
print('what was your overall score?')
score  = float(input())
if score >= 80:
    message = message + 'have learned alot today'
elif score <= 59:
    message = message + 'are the weaket link, goodbye!'
elif score > 100:
    message = message + 'are full of lies!'
elif score <= 79:
    message = message + 'took a good nap'
print(message)

