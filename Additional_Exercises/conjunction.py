wordlist = open("wordlist.txt", "r") 
words = wordlist.read().splitlines() 
wordlist.close() wordin = input("enter your word: ") 
min_len = int(input("enter minimum length : ")) 
if min_len < len(wordin): 
    print('Valid substring length') 
else: print('Invalid substring length, setting to 2') 

min_len = 2 
wordio = [] 
is_found = False 
index_front = 0 
index_back = 2 
complete = False 
while not complete: 
    is_found = False 
if index_back > len(wordin): 
    complete = True 
else: current_word = wordin[index_front:index_back] 
 for word in words: if current_word == word: if len(current_word) >= min_len: is_found = True if is_found is False: index_back += 1 else: wordio.append(current_word) index_front = index_back index_back += 1 print(wordio)