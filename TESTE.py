import hashlib 
  
# codificando a string Acervo Lima usando a função de hash md5
hash = hashlib.md5(b'admin13579')
print(hash.hexdigest())