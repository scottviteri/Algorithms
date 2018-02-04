#rabin carpin text search function
from OrderOfPrimes import findPrimesUnderNextN

#hash search_string and first len(search_string) letters of search_text
class RollingHash:
    def __init__(self, alphabet_size):
        self.hsh = 0
        self.alphabet_size = alphabet_size
        self.p = max(findPrimesUnderNextN(alphabet_size)) #prime >= len(search_string)
        self.hash_len = 0
    def append (self, c): #add last element to last
        self.hsh = (self.hsh*self.alphabet_size + ord(c)) % self.p 
        self.hash_len += 1
    def skip (self, c): #remove first element from hash
        self.hash_len -= 1
        self.hsh = (self.hsh - ord(c) * self.alphabet_size**(self.hash_len)) % self.p
        
#hash function is h(k) = k mod p
def magikarp (string1, string2):
    if (len(string1)>len(string2)):
        search_string, search_text = string2, string1
    else:
        search_string, search_text = string1, string2
    rs = RollingHash(26)
    rt = RollingHash(26)
    match_lst = []
    for s in search_string:
        rs.append(s)
    for t in search_text[:len(search_string)]:
        rt.append(t)
    for i in range(len(search_string),len(search_text)):
        if (rt.hsh == rs.hsh):
            if (search_string == search_text[i-len(search_string):i]):
                match_lst.append(i-len(search_string))
        rt.append(search_text[i])
        rt.skip(search_text[i - (len(search_string))])
    return match_lst


#search_string = 'jellojellojellojellojellojellojellohellojellojello'
#search_text = 'hello'

#print magikarp (search_string, search_text)
