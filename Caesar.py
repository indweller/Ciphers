"""
Caesar's cipher is one of the simplest and most widely known encryption techniques.
It is a type of substitution cipher in which each letter in the plaintext is replaced 
by a letter some fixed number of positions down the alphabet. 
"""
print("Enter the number of places you wish to shift.\nFor example, if you wish the letter D to be replaced by A, enter -3.\nIf you wish it to be replaced by G, enter 3.")
n = int(input())
intabs = "abcdefghijklmnopqrstuvwxyz"
totals = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
intabc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
totalc = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = n // abs(n) * (abs(n) % 26)
if n >= 0:
	dummy = chr(ord('a') + n)
	k = 0
	while (1):
		if totals[k] == dummy:
			break
		k += 1
	outtabs = totals[k: k + 26]
	outtabc = totalc[k: k + 26]
else:
	dummy = chr(ord('z') + n)
	k = 51
	while(1):
		if totals[k] == dummy:
			break
		k -= 1
	outtabs = totals[k - 25: k + 1]
	outtabc = totalc[k - 25: k + 1]	
print("Enter the text to be encrypted.")
inp = input()
trantabs = str.maketrans(intabs, outtabs)
trantabc = str.maketrans(intabc, outtabc)
print((inp.translate(trantabs)).translate(trantabc))