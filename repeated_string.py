def repeatedString(s, n):
    # Write your code here
    return n // len(s) * s.count('a') + s[0: n % len(s)].count('a')