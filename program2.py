def decode_message( s: str, p: str) -> bool:
     if not pattern:
        return False

     if pattern[0] == '*':
        if len(pattern) == 1:
            return True
        return matches(message, pattern[1:]) or (message and matches(message[1:], pattern))

    if pattern[0] == '?':
        return message and matches(message[1:], pattern[1:])

    return message and message[0] == pattern[0] and matches(message[1:], pattern[1:])


  
        