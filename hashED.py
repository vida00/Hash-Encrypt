#!/usr/bin/python

#############################################
# Importando as libs a serem usadas
#############################################
import sys, hashlib, base64

#############################################
# Variaveis para facilitar o uso das cores
#############################################
magenta="\033[35;01;1m"
vermelho="\033[31;01;1m"
amarelo="\033[33;01;1m"
end="\033[m"

def banner():
	print magenta+"""
db   db  .d8b.  .d8888. db   db d8888b. d88888b 
88   88 d8' `8b 88'  YP 88   88 88  `8D 88'     
88ooo88 88ooo88 `8bo.   88ooo88 88   88 88ooooo 
88~~~88 88~~~88   `Y8b. 88~~~88 88   88 88~~~~~ 
88   88 88   88 db   8D 88   88 88  .8D 88.     
YP   YP YP   YP `8888Y' YP   YP Y8888D' Y88888P 
                                                
codado por vida ^-^
Help: hashED.py -h
	"""+end
def help():
	print magenta+"\nOpcoes:\t\tFuncao\n-h, --help\tMostra o meno help\n-md5\t\tEncode para md5\n-sha1\t\tEncode para SHA1\n-sha256\t\tEncode para sha256\n-sha512\t\tEncode para sha512\n-b64 -e\t\tEncode para b64\n-b64 -d\t\tDecode para b64\n"+end
def b64_decode(textD):
	try:
		b64_d = base64.b64decode(textD)
		print amarelo+"[+] "+textD+" -> "+b64_d,end
	except:
		print vermelho+"Formato Invalido"+end
		sys.exit(1)
def b64_encode(textE):
	b64_e = base64.b64encode(textE)
	print amarelo+"[+] "+textE+" -> "+b64_e,end
def md5_encode(textM):
	md5_e = hashlib.md5(textM).hexdigest()
	print amarelo+"[+] "+textM+" -> "+md5_e,end
def sha1_encode(textS1):
	sha1_e = hashlib.sha1(textS1).hexdigest()
	print amarelo+"[+] "+textS1+" -> "+sha1_e,end
def sha256_encode(textS256):
	sha256_e = hashlib.sha256(textS256).hexdigest()
	print amarelo+"[+] "+textS256+" -> "+sha256_e,end
def sha512_encode(textS512):
	sha512_e = hashlib.sha512(textS512).hexdigest()
	print amarelo+"[+] "+textS512+" -> "+sha512_e,end

def hashED():
	if len(sys.argv) > 4 or len(sys.argv)  == 1:
		banner()
		sys.exit(1)
	elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
		help()
		sys.exit(0)
	elif sys.argv[1] == "-md5":
		md5_encode(sys.argv[2])
		sys.exit(0)
	elif sys.argv[1] == "-sha1":
		sha1_encode(sys.argv[2])
		sys.exit(0)
	elif sys.argv[1] == "-sha256":
		sha256_encode(sys.argv[2])
		sys.exit(0)
	elif sys.argv[1] == "-sha512":
		sha512_encode(sys.argv[2])
		sys.exit(0)
	elif sys.argv[1] == "-b64":
		if sys.argv[3] == "-e":
			b64_encode(sys.argv[2])
			sys.exit(0)
		elif sys.argv[3] == "-d":
			b64_decode(sys.argv[2])
			sys.exit(0)
		else:
			print vermelho+"Comando Inexistente"+end
			help()
			sys.exit(1)
	else:
		print vermelho+"Comando Inexistente"+end
		help()
		sys.exit(1)
try:
	hashED()
except KeyboardInterrupt:
	print vermelho+"\nAcao Abortada"+end
	sys.exit(1)
