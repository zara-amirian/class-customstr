class CustomStr(str):
    def custom_split(self, *separators):
        result = [self] 
        for sep in separators:  
            new_result = []  
            for item in result:  
                new_result.extend(item.split(sep))  
            result = new_result  
        return result
    def remove_duplicate(self):
        seen = []  
        for char in self.value:  
            if char not in seen:  
                seen.append(char)  
        return CustomStr(''.join(seen))  
    def set(self, index, new_char):
        if index < 0 or index >= len(self):
            print ("out of range!")
        return self[:index] + new_char + self[index + 1:]
    def isfloat(self):
        try:
            float(self)
            return True
        except :
            return False

    def ispalindrome(self):
        return self == self[::-1]
#test    
if __name__ == "__main__":
    a = CustomStr('Zara Amirian')
    print(a.custom_split(" ", 'a', 'm'))  # ['h', 'ir', 'ri', 'r']
    
    b = CustomStr('zara')
    print(b.remove_duplicate())  
    
    c = CustomStr('zara ')
    print(c.set(0, 'j'))  
    
    d = CustomStr('19.9')
    print(d.isfloat()) 
    
    e = CustomStr('minim')
    print(e.ispalindrome())  
    
    f = CustomStr('shirish')
    print(f.ispalindrome())  

