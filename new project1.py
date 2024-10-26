class CustomStr(str):
    def custom_split(self, *separators):
        import re
        pattern = '|'.join(map(re.escape, separators))
        return re.split(pattern, self)
    def remove_duplicate(self):
        return CustomStr(''.join(sorted(set(self), key=self.index)))
    def set(self, index, new_char):
        if index < 0 or index >= len(self):
            raise ("Index out of range")
        return self[:index] + new_char + self[index + 1:]
    def isfloat(self):
        try:
            float(self)
            return True
        except ValueError:
            return False

    def ispalindrome(self):
        return self == self[::-1]
#test    
if __name__ == "__main__":
    a = CustomStr('Zara Amirian')
    print(a.custom_split(" ", 'a', 'm'))  # ['h', 'ir', 'ri', 'r']
    
    b = CustomStr('zara')
    print(b.remove_duplicate())  # 'Zar'
    
    c = CustomStr('zara Amirian')
    print(c.set(0, 'j'))  # 'Jara Amirian'
    
    d = CustomStr('19.9')
    print(d.isfloat())  # True
    
    e = CustomStr('minim')
    print(e.ispalindrome())  # True
    
    f = CustomStr('shirish')
    print(f.ispalindrome())  # False

