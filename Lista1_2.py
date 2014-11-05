def reversed(text):
    return text[::-1]
 
def palindrom(napis):
    text = napis
    text = text.replace(" ", "")
            
    if text == reversed(text):
        return 'true'
    else:
        return 'false'
 
    
print palindrom('zakopane na pokaz')
