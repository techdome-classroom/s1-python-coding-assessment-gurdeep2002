def decode_message(self,s:str, p:str):
   
    if not p:
        return not s

    if p[0] == '*':
        if len(p) == 1:
            return True
        return decode_message(s, p[1:]) or (s and decode_message(s[1:], p))

    if p[0] == '?':
        return s and decode_message(s[1:], p[1:])

    return s and s[0] == p[0] and decode_message(s[1:], p[1:])
    
 





  
        