from math import pow
import random

def gcd(a, b):
	while b > 0: 
		r = a % b
		a = b
		b = r
	return a


def element_in_q(q):
	element = random.randint(pow(10,20), q)
	while gcd( q, element) != 1:
		element = random.randint(pow(10,20), q)
	return element


def power(_base_, exponent , modulo):
	x = 1	                	
	base = _base_
	while exponent > 0: 
		if exponent % 2 == 0:	
			x = (x*base) % modulo	
		base = (base*base)% modulo   
		exponent = int(exponent / 2)                         
	return x % modulo					 


def encrypt(plainText, q, h, g):
	
	c2 = []	                      
	for i in range(0 , len(plainText)):     
		c2.append(plainText[i])      
	y = element_in_q(q)
	s = power(h,y,q)
	c1 = power(g, y, q)
	for i in range(0, len(plainText)):
		c2[i] =  ord(c2[i]) * s       	
	return c2, c1 # lag p


def decrypt(cipherText, c1 ,x , q):
	decryptedText = []
	h = power(c1, x, q)
	for i in range(0, len(cipherText)):  #ref: seksjon 6
		decryptedText.append(chr(int(cipherText[i]/h)))
	return decryptedText



plainText = "message"
q = random.randint(pow(10,10), pow(10, 50))
g = element_in_q(q)	   
#eulers theorem, A = {a0...an} is congruent with B = a*{a0...an}
    
x = element_in_q(q)    #X er privat nøkkel
h = power(g, x, q)     # h er public key

cipherText, c1 = encrypt(plainText, q, h, g)

clearText = decrypt(cipherText, c1, x,q)

print("chipertext: ", cipherText)
print("decrypted: ", clearText)
