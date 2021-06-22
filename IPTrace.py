#!/bin/python

import os,sys,time,bs4,requests

r="\033[1;91m"
g="\033[1;92m"
b="\033[1;96m"
y="\033[1;93m"
w="\033[1;97m"
p=print
o=os.system
	
def banner():
	o("clear && cat $HOME/IPTrace/banner.txt | lolcat")

#//Back Module
def back_module():
	back = input(y + "Do you want to go back to main menu?" + w + "[" + g + "Y" + w + "/" + r + "n" + w + "]: " + b)
	if not back:
		p(r + "\nUnknown Command!!\n")
		time.sleep(2)
		o("clear")
		return(back_module())
	elif back == "y" or back == "Y" or back == "yes" or back == "Yes" or back == "YES":
		time.sleep(1.5)
		ip_geo()
	
	elif back == "n" or back == "N" or back == "no" or back == "No" or back == "NO":
		o("clear && figlet -c Happy Hacking Day | lolcat")
	else:
		p(r + "\nInvalid command!\n")
		time.sleep(2)
		o("clear")
		return(back_module())
	
#//IP Trace Module
def ip_geo():
	try:
		banner()
		p(w + "::" + r + " Main Menu " + w + "::\n")
		p(w +"[" + r + "1" + w + "]" + g + " - " + b + "Trace Yourself")
		p(w +"[" + r + "2" + w + "]" + g + " - " + b + "Trace Target IP")
		p(w +"[" + r + "3" + w + "]" + g + " - " + b + "Get target ip from host")
		p(w +"[" + r + "99" + w + "]" + g + " - " + b + "Exit\n")

		option = input(y + "IP Tracer => " + g)
	
		if not option:
			p(r + "\nUnknown Command!!\n")
			time.sleep(2)
			return(ip_geo())
		elif option == "1":
			self_trace()
		elif option == "2":
			target_trace()
		elif option == "3":
			host = input(y + "Target Host: " + b)
			o("host " + host)
			time.sleep(2)
			back_module()		
	
		elif option == "99":
			o("clear && figlet -c Happy Hacking Day | lolcat")
		else:				
			p(r + "\nInvalid command!\n")
			time.sleep(2)
			return(ip_geo())
	except KeyboardInterrupt:
		o("clear")	
		back_module()			
		
#//Self Trace Module
def self_trace():
	try:
		banner()
		res = requests.get('https://ipinfo.io/')
		data = res.json()
		location = data['loc'].split(',')
		lat = float(location[1])
		log = float(location[0])
		timez = data['timezone']
		ip = data['ip']
		city = data['city']
		country = data['country']
		isp = data['org']
		postal = data['postal']
	
		p(w + "\n:: " + b + "Your Information" + w + " ::\n")
		p(y + "Country: " + b + country)
		p(y + "IP Address: " + b + ip)		
		p(y + "City: " + b + city)	
		p(y + "Latitude: " + b + location[1])
		p(y + "Longitude: " + b + location[0])
		p(y + "City: " + b + city)
		p(y + "Postal: " + b + postal)					
		p(y + "Time Zone: " + b + timez)
		p(y + "ISP: " + b + isp + "\n")
		back_module()
	except KeyboardInterrupt:
		o("clear")	
		back_module()	

#//Target Trace Module	
def target_trace():
	try:
		banner()
	
		while True:
			ip = input(y + "Target IP: " + b)
			url = "http://ip-api.com/json/"
			res2 = requests.get('https://ipinfo.io/')
			data2 = res2.json()		
			res = requests.get(url + ip)
			data = res.json()

			location = data2['loc'].split(',')
			lat = float(location[1])
			log = float(location[0])
			timez = data['timezone']
			ip = data['query']
			city = data['city']
			country = data['country']
			isp = data['isp']
			postal = data['zip']			
	
			p(w + "\n:: " + b + "Your Information" + w + " ::\n")
			p(y + "Country: " + b + country)
			p(y + "IP Address: " + b + ip)		
			p(y + "City: " + b + city)		
			p(y + "Latitude: " + b + location[1])
			p(y + "Longitude: " + b + location[0])
			p(y + "City: " + b + city)
			p(y + "Postal: " + b + postal)					
			p(y + "Time Zone: " + b + timez)				
			p(y + "ISP: " + b + isp + "\n")

			back_module()
			break	
	except KeyboardInterrupt:
		o("clear")	
		back_module()	
		
ip_geo()				
