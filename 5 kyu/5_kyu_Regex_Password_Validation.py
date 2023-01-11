"""
https://www.codewars.com/kata/regex-password-validation/python
"""
regex = r'^(?=[0-9a-zA-Z]{6,}$)(?=[0-9a-zA-Z]*[A-Z])(?=[0-9a-zA-Z]*[a-z])(?=[0-9a-zA-Z]*[0-9]).*'

# 大佬鼠
regex0 = (
    '^'            # start line
    '(?=.*\d)'     # must contain one digit from 0-9
    '(?=.*[a-z])'  # must contain one lowercase characters
    '(?=.*[A-Z])'  # must contain one uppercase characters
    '[a-zA-Z\d]'   # permitted characters (alphanumeric only)
    '{6,}'         # length at least 6 chars
    '$'            # end line
)


regex1="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\W_]{6,}$"