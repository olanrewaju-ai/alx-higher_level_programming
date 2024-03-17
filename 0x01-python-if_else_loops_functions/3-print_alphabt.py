#!/usr/bin/python3
# Print the ASCII alphabet in lowercase without newline, excluding 'q' and 'e'
print(''.join(chr(97 + i) for i in range(26) if chr(97 + i) not in ['q', 'e']).format(), end='')
