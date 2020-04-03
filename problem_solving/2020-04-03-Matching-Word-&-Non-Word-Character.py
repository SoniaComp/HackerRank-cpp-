"""
The expression \w will match any word character.
Word characters include alphanumeric characters (a-z, A-Z and 0-9) and underscores (_).

ach03_01.png



\W matches any non-word character.
Non-word characters include characters other than alphanumeric characters (a-z, A-Z and 0-9) and underscore (_).

ach03_02.png

Task

You have a test string . Your task is to match the pattern 
Here  denotes any word character and  denotes any non-word character.

Note

This is a regex only challenge. You are not required to write any code.
You only have to fill the regex pattern in the blank (_________).
"""
Regex_Pattern = r"\w\w\w\W\w\w\w\w\w\w\w\w\w\w\W\w\w\w"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())