#!/usr/bin/env python3
import sys
import random

arguments = sys.argv

if len(arguments) != 2:
    print("Invalid usage! Valid usage is: retardify.py \"message\"")
    sys.exit(1)

message = arguments[1]

conventionalMessages = ("fix", "feat", "BREAKING CHANGE", "chore", "docs", "style", "refactor", "perf", "test", "improvement")

if message.split(':')[0] in conventionalMessages:
    message = ''.join(message.split(':')[1:])
    message = "i am a smartass!" + message

retardifiedMessage = ''
for word in message.split(' '):
    for c in word:
        if random.random() <= 0.4 and c != 'i':
            c = c.upper()
        retardifiedMessage += c
    retardifiedMessage += ' '

print(retardifiedMessage)
