def decode_message(s:str, p:str):
   
    if not p:
        return False

    if p[0] == '*':
        if len(p) == 1:
            return True
        return matches(s, p[1:]) or (s and matches(s[1:], p))

    if p[0] == '?':
        return message and matches(message[1:], pattern[1:])

    return message and message[0] == pattern[0] and matches(message[1:], pattern[1:])
    
 





  
        