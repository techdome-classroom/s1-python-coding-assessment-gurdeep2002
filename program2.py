def decode_message(s:str, p:str):
    def matches(message, pattern):
    if not pattern:
        return not message

    if p[0] == '*':
        if len(pattern) == 1:
            return True
        return matches(message, pattern[1:]) or (message and matches(message[1:], pattern))

    if pattern[0] == '?':
        return message and matches(message[1:], pattern[1:])

    return message and message[0] == pattern[0] and matches(message[1:], pattern[1:])
    
 





  
        