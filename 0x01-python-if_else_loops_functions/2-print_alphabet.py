#!/usr/bin/python3
# Print the ASCII alphabet in lowercase without newline
print(''.join(chr(97 + i) for i in range(26)), end='')
