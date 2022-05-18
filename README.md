# Vigenere-Cipher-Decryption

Vigenere cipher masks the frequency with which a character appears in a 
language: one letter in the ciphertext corresponds to multiple letters in the plaintext.  
 
Treat letters as numbers such as

`A=0, B=1, C=2, ..., Z=25 and Zn = {0, 1, 2, ..., n-1}. `


Given m, a positive integer, P = C = (Z26)n, and K = (k1, k2, ..., km) a key,
we define: 
 
 
Encryption: 
  `Ek(p1, p2, ..., pm) = (p1 + k1, p2 + k2, ..., pm + km)(mod 26)`
 
 
Decryption: 
  `Dk(c1, c2, ..., cm) = (c1 - k1, c2 - k2, ..., cm - km)(mod 26)`
 
In this project, I have created a program that breaks the following Vigenere cipher text:


`Ffowc abiyfsbiq fkh ffbic mnh ofkvyorovgersgq. Dlcup lyup aye ergrmbqjk 
mypxw elp cxmbnoh mr xfq xiaw. Xfqgb cmpc uqpo pqkkvimzvc fgxc. Rrigd 
wssffc uqpo qyyvp, usxf zbmetr vcp, xful pgbq.`
 
This cipher text is encrypted with the following key:  
 
`“mykey”`
