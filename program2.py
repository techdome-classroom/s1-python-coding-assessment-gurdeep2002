def decode_message( s: str, p: str) -> bool:
     if not p:
        return False

     if p[0] == '*':
        if len(p) == 1:
            return True
        return matches(s, p[1:]) or (s and matches(s[1:], p))

    if p[0] == '?':
        return s and matches(s[1:], p[1:])

    return s and s[0] == p[0] and matches(se[1:], p[1:])


  
        