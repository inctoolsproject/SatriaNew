# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os
from bs4 import BeautifulSoup
import timeit
from gtts import gTTS
import wikipedia
import ast
import requests
import subprocess
import urllib,urllib2,urllib3
from selenium import webdriver


cl = LINETCR.LINE()
cl.login(qr=True)
#cl.login(token="tokenmu")
#cl.login(token='')
cl.loginResult()

ki = LINETCR.LINE()
ki.login(qr=True)
#ki.login(token="tokenmu")
ki.loginResult()

kk = LINETCR.LINE()
kk.login(qr=True)
kk.login(token="tokenmu")
kk.loginResult()

kc = LINETCR.LINE()
kc.login(qr=True)
#kc.login(token="tokenmu")
kc.loginResult()

#ks = LINETCR.LINE()
ks.login(qr=True)
#ks.login(token="tokenmu")
#ks.loginResult()


print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')
helpMessage= """ 
╔═══════════════════
╠              ✍MENU V.1✍️
╠❂͜͡➣「Key」Gimage: [Judul]
╠❂͜͡➣「Key」Wikipedia: [Judul]
╠❂͜͡➣「Key」Youtube: [Judul]
╠❂͜͡➣「Key」Instagram: [Name]
╠❂͜͡➣「Key」Vn: [Text]
╠❂͜͡➣「Key」Musik: [Song Name]
╠❂͜͡➣「Key」Lirik: [Song Name]
╠❂͜͡➣「Key」Google: [Text]
╠❂͜͡➣「Key」Ig check: [Name
╠❂͜͡➣「Key」Ig bio: [Name]
╠❂͜͡➣「Key」Ig pict: [Name]
╠❂͜͡➣「Key」Ig pictl: [Link]
╠❂͜͡➣「Key」Ig vidl: [Link]
╠❂͜͡➣「Key」Ig link: [Name
╚═══════════════════
"""
helpMessage2= """ 
╔═══════════════════
╠              ✍MENU V.2✍️
╠❂͜͡➣「Key」Searchid: [Id]
╠❂͜͡➣「Key」Searchmid: [Mid]
╠❂͜͡➣「Key」AddId:[Id]
╠❂͜͡➣「Key」AddMid: [Mid]
╠❂͜͡➣「Key」Checkmid: [Mid]
╠❂͜͡➣「Key」Midcover: [Mid]
╠❂͜͡➣「Key」Midpict: [Mid]
╠❂͜͡➣「Key」Midbio: [Mid]
╠❂͜͡➣「Key」Midname:[Mid]
╠❂͜͡➣「Key」Bot:restart
╠❂͜͡➣「Key」Bot:runtime
╚═══════════════════

"""
helpMessage3= """ 
╔═══════════════════
╠              ✍MENU V.3✍️
╠❂͜͡➣「Key」Getinfo [@tag]
╠❂͜͡➣「Key」Getbio [@tag]
╠❂͜͡➣「Key」Getmid [@tag]
╠❂͜͡➣「Key」Getcontact [@tag
╠❂͜͡➣「Key」Getpict [@tag]
╠❂͜͡➣「Key」Getcover [@tag]
╠❂͜͡➣「Key」Getpicturl [@tag]
╠❂͜͡➣「Key」Getcoverurl [@tag]
╚═══════════════════
"""
helpMessage4= """ 
╔═══════════════════
╠              ✍MENU V.4✍️
╠❂͜͡➣「Key」Myname: [Name]
╠❂͜͡➣「Key」Mybio: [Name]
╠❂͜͡➣「Key」Myname
╠❂͜͡➣「Key」Mybio
╠❂͜͡➣「Key」Mypict
╠❂͜͡➣「Key」Mycover
╠❂͜͡➣「Key」Mypicturl
╠❂͜͡➣「Key」Mycoverurl
╠❂͜͡➣「Key」Friendlist
╠❂͜͡➣「Key」Glist/Glist2
╚═══════════════════
"""
helpMessage5= """ 
╔═══════════════════
╠              ✍MENU V.5✍️
╠❂͜͡➣「Key」Gn: [Name]
╠❂͜͡➣「Key」Ourl/Curl
╠❂͜͡➣「Key」Gpict
╠❂͜͡➣「Key」Gpicturl
╠❂͜͡➣「Key」Gpict [Name]
╠❂͜͡➣「Key」Tagall
╠❂͜͡➣「Key」Setview
╠❂͜͡➣「Key」Viewseen
╠❂͜͡➣「Key」Spam?
╠❂͜͡➣「Key」Set spam:[Text]
╠❂͜͡➣「Key」Spam:10-50 [@tag]
╚═══════════════════
"""
helpMessage6= """ 
╔═══════════════════
╠              ✍MENU V.6✍️
╠❂͜͡➣「Key」Copy [@tag]
╠❂͜͡➣「Key」Copy name [@tag]
╠❂͜͡➣「Key」Copy bio [@tag]
╠❂͜͡➣「Key」Copy image [@tag]
╠❂͜͡➣「Key」Copy cover [@tag]
╠❂͜͡➣「Key」Backup
╚═══════════════════
"""
setMessage= """ 
╔═══════════════════
╠    ✍MENU SETTING BOT✍️
╠❂͜͡➣「Key」Aread: on/off
╠❂͜͡➣「Key」Arespon: on/off
╠❂͜͡➣「Key」Autokick: on/off
╠❂͜͡➣「Key」Backup: on/off
╚═══════════════════
"""
KAC=[cl,ki]
DEF=[ki]
KICK=[ki]
protection = []
autoread = []
mid = cl.getProfile().mid
Amid = ki.getProfile().mid

contact = cl.getProfile()
kembali = cl.getProfile()
kembali.displayName = contact.displayName
kembali.statusMessage = contact.statusMessage
kembali.pictureStatus = contact.pictureStatus

Bots=[mid]
Creator="ucf90f327ff43f0b130a490603aa1a507"
admin=["ucf90f327ff43f0b130a490603aa1a507"]

wait = {
    "blacklist":{},    
    "wblacklist":False,
    "dblacklist":False,    
    "Backup":False,
    "protectionOn":True, 
    "AutoKick":False,    
    "detectMention":False,      
    "alwaysRead":False,   
    "kickMention":False,
    "Pap":"http://www.rockcreekdothan.com/Common/images/jquery/galleria/image-not-found.png",
    "SetKey":".",
    "creator":"ucf90f327ff43f0b130a490603aa1a507",
    "spam":"Your Account Has Been Spammed"
}
mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{},
}				
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

#----Gimage---#
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib.request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib.request.Request(url, headers = headers)
            resp = urllib.request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+1)
        end_content = s.find(',"ow"',start_content+1)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items
#---Gimage----#    

#-----Runtime------#
mulai = time.time()
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)
#-----Runtime------#        

#-----Youtube----#
def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi
#-----Youtube-----#         
#----Restart----#
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv) 
#----Restart----#    

def bot(op):
    try:
#--------------------END_OF_OPERATION--------------------
        if op.type == 0:
            return
#--------------------END_OF_OPERATION--------------------        
        if op.type == 19:
         if wait["AutoKick"] == True:
          if op.param2 in Bots:
            pass
          if op.param2 in admin:
            pass
          else:
            try:
              G = cl.getGroup(op.param1)
              G.preventJoinByTicket = False
              cl.updateGroup(G)
              Ticket = cl.reissueGroupTicket(op.param1)
              ki.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              ki.kickoutFromGroup(op.param1,[op.param2])
              c = Message(to=op.param1, from_=None, text=None, contentType=13)
              c.contentMetadata={'mid':op.param2}
              ki.sendMessage(c)
              ki.leaveGroup(op.param1)
              G.preventJoinByTicket = True
              cl.updateGroup(G)
              wait["blacklist"][op.param2] = True
            except:
              G = cl.getGroup(op.param1)
              G.preventJoinByTicket = False
              cl.updateGroup(G)
              Ticket = cl.reissueGroupTicket(op.param1)
              ki.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              ki.kickoutFromGroup(op.param1,[op.param2])
              c = Message(to=op.param1, from_=None, text=None, contentType=13)
              c.contentMetadata={'mid':op.param2}
              ki.sendMessage(c)
              ki.leaveGroup(op.param1)
              G.preventJoinByTicket = True
              cl.updateGroup(G)
              wait["blacklist"][op.param2] = True
        if op.type == 19:
                if not op.param2 in Bots:
                    try:
                        gs = kc.getGroup(op.param1)
                        gs = kc.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            pass
                                
                    except Exception, e:
                        print e
                if not op.param2 in Bots and admin:
                  if wait["Backup"] == True:
                    try:
                        ki.inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                        print e
                if not op.param2 in Bots and admin:
                  if wait["protectionOn"] == True:  
                   try:
                       klist=[kk,kc]
                       kicker = random.choice(klist)
                       G = kicker.getGroup(op.param1)
                       G.preventJoinByTicket = False
                       kicker.updateGroup(G)
                       invsend = 0
                       Ticket = kicker.reissueGroupTicket(op.param1)
                       kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                       time.sleep(0.2)
                       X = kicker.getGroup(op.param1)             
                       X.preventJoinByTicket = True
                       kk.kickoutFromGroup(op.param1,[op.param2])
                       kicker.kickoutFromGroup(op.param1,[op.param2])
                       kk.leaveGroup(op.param1)
                       kicker.updateGroup(X)
                   except Exception, e:
                            print e
                if not op.param2 in Bots and admin:
                    try:
                        gs = kc.getGroup(op.param1)
                        gs = kc.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            pass
                                
                    except Exception, e:
                        print e
                if not op.param2 in Bots and admin:
                  if wait["Backup"] == True:
                    try:
                        ilist=[kk,kc]
                        inviter = random.choice(ilist)
                        inviter.inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                        print e    
                        
        if op.type == 26:
            if wait["alwaysRead"] == True:
                msg = op.message
                if msg.toType == 2:
                    msg.to = msg.to
                    msg.from_ = msg.from_
                    cl.sendChatChecked(msg.to,msg.id)


        if op.type == 26:
            if wait["alwaysRead"] == True:
                msg = op.message
                if msg.toType == 0:
                    msg.to = msg.from_
                    msg.from_ = msg.to
                    cl.sendChatChecked(msg.from_,msg.id)
#------------------NOTIFIED_INVITE_INTO_ROOM-------------
        if op.type == 22:
            cl.leaveRoom(op.param1)
#--------------------INVITE_INTO_ROOM--------------------

#--------------NOTIFIED_INVITE_INTO_GROUP----------------

	    if mid in op.param3:
                if wait["AutoJoin"] == True:
                    ki.acceptGroupInvitation(op.param1)
                else:
		    ki.rejectGroupInvitation(op.param1)
	    else:
                if wait["AutoCancel"] == True:
		    if op.param3 in admin:
			pass
		    else:
                        ki.cancelGroupInvitation(op.param1, [op.param3])
		else:
		    if op.param3 in wait["blacklist"]:
			ki.cancelGroupInvitation(op.param1, [op.param3])
			ki.sendText(op.param1, "Itu kicker jgn di invite!")
		    else:
			pass
#------------------AUTO_RESPON_BY_TAG-----------------
        if op.type == 26:
            msg = op.message
            if 'MENTION' in msg.contentMetadata.keys() != None:
              if wait ["detectMention"] == True:
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["Dont tag me, im busy",cName + " ada apa ngetag?",cName + " PC AJA","tersummon-_-"]
                    ret_ = "[Auto Respond] " + random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  break                    
#------------------AUTO_KICK_BY_TAG-----------------
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Tag tag mele jadi ke tendang",cName + " Ngapain Ngetag?",cName + " Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja","-_-","Alin lagi off", cName + " Kenapa Tag saya?","SPAM PC aja " + cName, "Jangan Suka Tag gua " + cName, "Kamu siapa " + cName + "?", "Ada Perlu apa " + cName + "?","Tenggelamkan tuh yang suka tag pake BOT","Tersummon -_-"]
                     ret_ = "[Auto Kick]\n " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  cl.kickoutFromGroup(msg.to,[msg.from_])
                                  break
#--------------------------SEND_MESSAGE---------------------------
        if op.type == 25:
            msg = op.message
#----------------------------------------------------------------------------
            if msg.contentType == 13:
                if wait["wblacklist"] == True:
		    if msg.contentMetadata["mid"] not in admin:
                        if msg.contentMetadata["mid"] in wait["blacklist"]:
                            cl.sendText(msg.to,"already")
                            wait["wblacklist"] = False
                        else:
                            wait["blacklist"][msg.contentMetadata["mid"]] = True
                            wait["wblacklist"] = False
                            cl.sendText(msg.to,"aded")
		    else:
			cl.sendText(msg.to,"Admin Detected~")
			

                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                elif wait["Contact"] == True:
                     msg.contentType = 0
                     cl.sendText(msg.to,msg.contentMetadata["mid"])
                     if 'displayName' in msg.contentMetadata:
                         contact = cl.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = cl.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                     else:
                         contact = cl.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = cl.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))


#--------------------------------------------------------

#--------------------------------------------------------
            elif msg.text is None:
                return
            
            elif msg.text in [wait["SetKey"]+"Help1",wait["SetKey"]+"help1"]:
                cl.sendText(msg.to,helpMessage) 
            elif msg.text in [wait["SetKey"]+"Help2",wait["SetKey"]+"help2"]:
                cl.sendText(msg.to,helpMessage2)      
            elif msg.text in [wait["SetKey"]+"Help3",wait["SetKey"]+"help3"]:
                cl.sendText(msg.to,helpMessage3)   
            elif msg.text in [wait["SetKey"]+"Help4",wait["SetKey"]+"help4"]:
                cl.sendText(msg.to,helpMessage4)   
            elif msg.text in [wait["SetKey"]+"Help5",wait["SetKey"]+"help5"]:
                cl.sendText(msg.to,helpMessage5)                   
            elif msg.text in [wait["SetKey"]+"Help6",wait["SetKey"]+"help6"]:
                cl.sendText(msg.to,helpMessage6)  
#--------------------------------------------------------
            elif msg.text in [wait["SetKey"]+"Set",wait["SetKey"]+"set"]:
                cl.sendText(msg.to,setMessage) 
            elif msg.text in [wait["SetKey"]+"Status",wait["SetKey"]+"status"]:
                md = ""
		if wait["Backup"] == True: md+="╠❂͜͡➣Backup : on\n"
                else: md +="╠❂͜͡➣Backup : off\n"
		if wait["AutoKick"] == True: md+="╠❂͜͡➣Autokick : on\n"
                else: md +="╠❂͜͡➣Autokick : off\n" 
		if wait["alwaysRead"] == True: md+="╠❂͜͡➣Autoread : on\n"
                else: md +="╠❂͜͡➣Autoread : off\n"  
		if wait["detectMention"] == True: md+="╠❂͜͡➣Autorespon : on"
                else: md +="╠❂͜͡➣Autorespon : off"                  
                cl.sendText(msg.to,md)
#--------------------------------------------------------

	    elif wait["SetKey"]+"Autokick:on" in msg.text:
		wait["AutoKick"] = True
		cl.sendText(msg.to,"AutoKick Active")

	    elif wait["SetKey"]+"Autokick:off" in msg.text:
		wait["AutoKick"] = False
		cl.sendText(msg.to,"AutoKick inActive")
#--------------------------------------------------------
	    elif wait["SetKey"]+"Backup:on" in msg.text:
	        wait["Backup"] = True
	    	cl.sendText(msg.to,"Backup Invite Member Active")

	    elif wait["SetKey"]+"Backup:off" in msg.text:
	    	wait["Backup"] = False
	    	cl.sendText(msg.to,"Backup Invite Member inActive")   
#--------------------------------------------------------	    	
	    elif wait["SetKey"]+"Aread:on" in msg.text:
	        wait["alwaysRead"] = True
	    	cl.sendText(msg.to,"Auto Read Active")

	    elif wait["SetKey"]+"Aread:off" in msg.text:
	    	wait["alwaysRead"] = False
	    	cl.sendText(msg.to,"Auto Read inActive")	    	
#-------------------------------------------------------- 
#-------------------------------------------------------- 
	    elif wait["SetKey"]+"Arespon:on" in msg.text:
	        wait["detectMention"] = True
	    	cl.sendText(msg.to,"Auto Respon Active")

	    elif wait["SetKey"]+"Arespon:off" in msg.text:
	        wait["detectMention"] = False
	    	cl.sendText(msg.to,"Auto Respon inActive")
#-------------------------------------------------------- 
	    elif msg.text in [wait["SetKey"]+"Restart"]:
		cl.sendText(msg.to, "Bot Program has been restarted")
		restart_program()
		print "@Restart"
#--------------------------------------------------------
            elif msg.text.lower() == 'bot:runtime':
                eltime = time.time() - mulai
                van = "Bot sudah berjalan selama "+waktu(eltime)
                cl.sendText(msg.to,van)	
            elif wait["SetKey"]+"Runtime" in msg.text:
                eltime = time.time() - mulai
                van = "「Selfbot 」\n" "Type:Runtime\nTime: "+ waktu(eltime)
                cl.sendText(msg.to,"「 Runtime Bot 」\n" "Status: Processing")
                cl.sendText(msg.to,van)	
                cl.sendText(msg.to,"「 Runtime Bot 」\n" "Status: Success")
#--------------------------------------------------------
            elif msg.text.lower() in ["join"]:
                if msg.from_ in admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "[Command] Join"
                        G.preventJoinByTicket(G)
                        cl.updateGroup(G)   
            elif msg.text.lower() in ["bye"]:
                if msg.toType == 2:
                  if msg.from_ in admin:
                    print "[Command] Bye"
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                        ka.leaveGroup(msg.to)
                        kb.leaveGroup(msg.to)
                        ko.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)
                        ku.leaveGroup(msg.to)
                    except:
                        pass  
#--------------------------------------------------------
#Script Google Image Search
            elif wait["SetKey"]+"Gimage:" in msg.text:
                      googl = msg.text.replace(wait["SetKey"]+"Gimage:","")
                      url = 'https://www.google.com/search?hl=en&biw=1366&bih=659&tbm=isch&sa=1&ei=vSD9WYimHMWHvQTg_53IDw&q=' + googl
                      raw_html = (download_page(url))
                      items = []
                      items = items + (_images_get_all_items(raw_html))
                      path = random.choice(items)
                      try:
                          start = timeit.timeit()
                          cl.sendImageWithURL(msg.to,random.choice(items))
                      except Exception as e:
                          cl.sendText(msg.to,str(e))
#--------------------------------------------------------
#Script Wikipedia Search
            elif wait["SetKey"]+'wikipedia:' in msg.text.lower():
                  try:
                      wiki = msg.text.lower().replace(wait["SetKey"]+"wikipedia:","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
#--------------------------------------------------------
#Script Youtube Search
            elif wait["SetKey"]+"youtube:" in msg.text.lower():
                if msg.from_ in admin:
                   query = msg.text.split(" ")
                   try:
                       if len(query) == 3:
                           isi = yt(query[2])
                           hasil = isi[int(query[1])-1]
                           cl.sendText(msg.to, hasil)
                       else:
                           isi = yt(query[1])
                           cl.sendText(msg.to, isi[0])
                   except Exception as e:
                       cl.sendText(msg.to, str(e))
#--------------------------------------------------------
#Script Instagram
            elif wait["SetKey"]+"Ig info:" in msg.text:
                try:
                    instagram = msg.text.replace(wait["SetKey"]+"Ig info:","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "=====INSTAGRAM INFO USER=====\n"
                    details = "\n=====INSTAGRAM INFO USER====="
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
            elif wait["SetKey"]+"Ig pict: " in msg.text:
                try:
                    instagram = msg.text.replace(wait["SetKey"]+"Ig pict: ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))                	
            elif wait["SetKey"]+"Ig link:" in msg.text:
                try:
                    instagram = msg.text.replace(wait["SetKey"]+"Ig link:","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    cl.sendText(msg.to,  link)
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))   	
            elif wait["SetKey"]+"Ig pictl:" in msg.text:
                cari = msg.text.replace(wait["SetKey"]+"Ig pictl:","")
                try:
                    respon = requests.get(cari+"?__a=1")
                    data = respon.json()
                    ig_url = data['graphql']['shortcode_media']['display_url']
                    cl.sendImageWithURL(msg.to,ig_url)
                except:
                        cl.sendText(msg.to,"Error")
            elif wait["SetKey"]+"Ig vidl:" in msg.text:
                cari = msg.text.replace(wait["SetKey"]+"Ig vidl:","")
                try:
                    respon = requests.get(cari+"?__a=1")
                    data = respon.json()
                    ig_url = data['graphql']['shortcode_media']['video_url']
                    cl.sendVideoWithURL(msg.to,ig_url)
                except:
                        cl.sendText(msg.to,"Error")
            elif msg.text in ["time"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): blan = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + blan + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                client.sendText(msg.to, rst)
            elif "Ig bio " in msg.text:
                    try:
                        instagram = msg.text.replace("Ig bio ","")
                        response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                        data = response.json()
                        namaIG = str(data['user']['full_name'])
                        bioIG = str(data['user']['biography'])
                        mediaIG = str(data['user']['media']['count'])
                        verifIG = str(data['user']['is_verified'])
                        usernameIG = str(data['user']['username'])
                        followerIG = str(data['user']['followed_by']['count'])
                        profileIG = data['user']['profile_pic_url_hd']
                        privateIG = str(data['user']['is_private'])
                        followIG = str(data['user']['follows']['count'])
                        link = "Link: " + "https://www.instagram.com/" + instagram
                        text = "Biography : "+bioIG
                        cl.sendImageWithURL(msg.to, profileIG)
                        cl.sendText(msg.to, str(text))
                    except Exception as e:
                        cl.sendText(msg.to, str(e))
            elif wait["SetKey"]+"Ig bio:" in msg.text:
                arg = msg.text.split(" ");
                nk0 = msg.text.replace(wait["SetKey"]+"Ig bio:","")
                nk1 = nk0.rstrip("  ")
                if len(arg) > 1:
                    proc = subprocess.Popen('curl -s https://www.instagram.com/'+nk1+'/?__a=1',shell=True, stdout=subprocess.PIPE)
                    x = proc.communicate()[0]
                    parsed_json = json.loads(x)
                    if(len(x) > 10):
                        username = (parsed_json['user']['username'])
                        fullname = (parsed_json['user']['full_name'])
                        followers = (parsed_json['user']['followed_by']['count'])
                        following = (parsed_json['user']['follows']['count'])
                        media = (parsed_json['user']['media']['count'])
                        bio = (parsed_json['user']['biography'])
                        url = (parsed_json['user']['external_url'])
                        cl.sendText(msg.to,"       「Succes」\n「Fitur」: Instagram Bio  \n「Account Name」: @" + nk0 + "\n「Bio」: " + str(bio))
                        print '[Command] Instagram'
                    else:
                        cl.sendText(msg.to,"Not Found...")
                else:
                    cl.sendText(msg.to,"Contoh /ig aguzz_gangga") 
#--------------------------------------------------------
#Script Twitter
#            elif wait["SetKey"]+"Twitter:" in msg.text:
#                try:
#                    twitter = msg.text.replace(wait["SetKey"]+"Twitter","")
#                    driver.get("https://twitter.com/" + twitter)
#                    soup = BeautifulSoup(driver.page_source,"lxml")
#                    driver.quit()
#                    for title in soup.select("#page-container"): 
#                        name = title.select(".ProfileHeaderCard-nameLink")[0].text.strip()
#                        location = title.select(".ProfileHeaderCard-locationText")[0].text.strip()
#                        tweets = title.select(".ProfileNav-value")[0].text.strip()
#                        following = title.select(".ProfileNav-value")[1].text.strip()
#                        followers = title.select(".ProfileNav-value")[2].text.strip()
#                        likes = title.select(".ProfileNav-value")[3].text.strip()
#                        cl.sendText(msg.to, name,location,tweets,following,followers,likes)
#                        cl.sendImageWithURL(msg.to, text1[0])
#                        print(name,location,tweets,following,followers,likes)
#                except Exception as njer:
#                	cl.sendText(msg.to, str(njer))     
            elif wait["SetKey"]+"3:" in msg.text:
                try:
                    twitter = msg.text.replace(wait["SetKey"]+"3:","")
                    html = requests.get('https://twitter.com/' + twitter)
                    soup = BeautifulSoup(html.text, 'html5lib')
                    name = data[0].get(".ProfileHeaderCard-nameLink").split() #data[0].get('content').split()
                    cl.sendText(msg.to, name)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
            elif wait["SetKey"]+"Tw link:" in msg.text:
                try:
                    twitter = msg.text.replace(wait["SetKey"]+"Tw link:","")
                    html = requests.get('https://www.twitter.com/' + twitter + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    link = "Link: " + "https://www.twitter.com/" + twitter
                    cl.sendText(msg.to,  link)
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))                     
#「Succes」\n「Fitur」: Add Blocklist\n「Account Name」: " + _name
#--------------------------------------------------------
#Script Voice note Google
            elif wait["SetKey"]+"Vn:" in msg.text:
                say = msg.text.replace(wait["SetKey"]+"Vn:","")
                contact = cl.getContact(msg.from_)
                cName = contact.displayName
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")                	
            elif "Vn-af " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-af ","")
                 tts = gTTS(psn, lang='af', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-sq " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-sq ","")
                 tts = gTTS(psn, lang='sq', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-ar " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-ar ","")
                 tts = gTTS(psn, lang='ar', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-hy " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-hy ","")
                 tts = gTTS(psn, lang='hy', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-bn " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-bn ","")
                 tts = gTTS(psn, lang='bn', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-ca " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-ca ","")
                 tts = gTTS(psn, lang='ca', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-zh " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-zh ","")
                 tts = gTTS(psn, lang='zh', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-zhcn " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-zhcn ","")
                 tts = gTTS(psn, lang='zh-cn', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-zhtw " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-zhtw ","")
                 tts = gTTS(psn, lang='zh-tw', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-zhyue " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-zhyue ","")
                 tts = gTTS(psn, lang='zh-yue', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-hr " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-hr ","")
                 tts = gTTS(psn, lang='hr', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-cs " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-cs ","")
                 tts = gTTS(psn, lang='cs', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-da " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-da ","")
                 tts = gTTS(psn, lang='da', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-nl " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-nl ","")
                 tts = gTTS(psn, lang='nl', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-en " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-en ","")
                 tts = gTTS(psn, lang='en', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-enau " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-enau ","")
                 tts = gTTS(psn, lang='en-au', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-enuk " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-enuk ","")
                 tts = gTTS(psn, lang='en-uk', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-enus " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-enus ","")
                 tts = gTTS(psn, lang='en-us', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-eo " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-eo ","")
                 tts = gTTS(psn, lang='eo', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-fi " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-fi ","")
                 tts = gTTS(psn, lang='fi', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-fr " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-fr ","")
                 tts = gTTS(psn, lang='fr', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-de " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-de ","")
                 tts = gTTS(psn, lang='de', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-el " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-el ","")
                 tts = gTTS(psn, lang='el', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-hi " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-hi ","")
                 tts = gTTS(psn, lang='hi', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-hu " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-hu ","")
                 tts = gTTS(psn, lang='hu', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-is " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-is ","")
                 tts = gTTS(psn, lang='is', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-id " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-id ","")
                 tts = gTTS(psn, lang='id', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-it " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-it ","")
                 tts = gTTS(psn, lang='it', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-jp " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-jp ","")
                 tts = gTTS(psn, lang='ja', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-km " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-km ","")
                 tts = gTTS(psn, lang='km', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-ko " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-ko ","")
                 tts = gTTS(psn, lang='ko', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-la " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-la ","")
                 tts = gTTS(psn, lang='la', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-lv " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-lv ","")
                 tts = gTTS(psn, lang='lv', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-mk " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-mk ","")
                 tts = gTTS(psn, lang='mk', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-no " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-no ","")
                 tts = gTTS(psn, lang='no', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
#--------------------------------------------------------
#Script Play & Download Music Google = JOOX
            elif wait["SetKey"]+"Musik:" in msg.text:
                try:
                    songname = msg.text.replace(wait["SetKey"]+"Musik:","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])
		except Exception as njer:
		        cl.sendText(msg.to, str(njer))
#--------------------------------------------------------
#Script Lyric Music Google = JOOX
            elif wait["SetKey"]+"Lirik:" in msg.text:
                try:
                    songname = msg.text.replace(wait["SetKey"]+"Lirik:","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
#--------------------------------------------------------
#Script Search Google
            elif wait["SetKey"]+"Google:" in msg.text:
                    a = msg.text.replace(wait["SetKey"]+"Google:","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to, "https://www.google.co.jp/search?q=" + b)
            elif wait["SetKey"]+"Test:" in msg.text:
                    a = msg.text.replace(wait["SetKey"]+"Test:","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to, "https://www.google.com/search?q=" + b)                    
#--------------------------------------------------------
#Search,Add and Steal By Id and Mid
            elif wait["SetKey"]+"Searchid:" in msg.text:
                msgg = msg.text.replace(wait["SetKey"]+'Searchid: ','')
                conn = cl.findContactsByUserid(msgg)
                if True:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': conn.mid}
                    cl.sendText(msg.to,"http://line.me/ti/p/~" + msgg)
                    cl.sendMessage(msg)   
            elif wait["SetKey"]+"AddId:" in msg.text:
                msgg = msg.text.replace(wait["SetKey"]+'AddId: ','')
                conn = cl.findContactsByUserid(msgg)
                if True:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': conn.mid}
                    cl.findAndAddContactsByUserid(msgg) 
                    cl.sendMessage(msg)                       
                    findAndAddContactsByUserid
            elif wait["SetKey"]+"Searchmid:" in msg.text:
                key = msg.text[-33:]
                msg.contentType = 13
                msg.contentMetadata = {'mid': key}
                contact = cl.getContact(key)
                cl.sendMessage(msg)
            elif wait["SetKey"]+"AddMid:" in msg.text:
                msgg = msg.text.replace(wait["SetKey"]+'AddMid: ','')
                key = msg.text[-33:]
                msg.contentType = 13
                msg.contentMetadata = {'mid': key}
                contact = cl.getContact(key)
                cl.findAndAddContactsByMid(msgg)
                cl.sendMessage(msg)                         
            elif wait["SetKey"]+"Midpict:" in msg.text:
              if msg.from_ in admin:
                umid = msg.text.replace(wait["SetKey"]+"Midpict:","")
                contact = cl.getContact(umid)
                try:
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                except:
                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                try:
                    cl.sendImageWithURL(msg.to,image)
                except Exception as error:
                    cl.sendText(msg.to,(error))
                    pass                
            elif wait["SetKey"]+"Midcover:" in msg.text:
                saya = msg.text.replace(wait["SetKey"]+"Midcover:","")
                contact = cl.getContact(saya)
                cu = cl.channel.getCover(saya)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass
            elif wait["SetKey"]+"Mid @" in msg.text:
                _name = msg.text.replace(wait["SetKey"]+"Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass                         
            elif wait["SetKey"]+"Midbio:" in msg.text:
                saya = msg.text.replace(wait["SetKey"]+"Midbio:","")
                contact = cl.getContact(saya)
                cu = cl.channel.getCover(saya)
                path = str(cu)
                try:
                    cl.sendText(msg.to,"Bio :\n" + contact.statusMessage)
                except:
                    pass  
            elif wait["SetKey"]+"Midname:" in msg.text:
                saya = msg.text.replace(wait["SetKey"]+"Midname:","")
                contact = cl.getContact(saya)
                cu = cl.channel.getCover(saya)
                path = str(cu)
                try:
                    cl.sendText(msg.to,"Bio :\n" + contact.displayName)
                except:
                    pass                  
            elif "About" in msg.text: 
                if msg.from_ in admin:
                	cl.sendText(msg.to,"「Aʙᴏᴜᴛ Bᴏᴛ」\nFal Sᴇʟғʙᴏᴛ Eᴅɪᴛɪᴏɴ♪\nTɪᴍᴇ: " + datetime.today().strftime('%H:%M:%S') + " \n\n「Bᴏᴛ Iɴғᴏʀᴍᴀᴛɪᴏɴ」\n╠═════════════════════\n  ❂͜͡➣ Bᴏᴛ Cʀᴇᴀᴛᴇᴅ ɪɴ: 01-12-2017\n  ❂͜͡➣ Bᴏᴛ Uᴘʟɪɴᴋ ʙʏ: Naufal Ardhani\n「 ▶ line://ti/p/~fbot2」\n  ☸ Bᴏᴛ Usᴇʀɴᴀᴍᴇ: Fal \n  ☸ Exᴘɪʀᴇᴅ ᴅᴀᴛᴇ: 01-05-2019\n  ☸ Iɴ ᴅᴀʏs: 300+ ᴅᴀʏs\n╠═════════════════════\n「Cᴏɴᴛᴀᴄᴛ Pᴇʀsᴏɴᴀʟ」\n「 ▶ ID LINE: line://ti/p/~fbot2」\n\n ʀᴇᴠᴏʟᴜᴛɪᴏɴ ℬᴏᴛ")

#--------------------------------------------------------
#Set Key Info
            elif msg.text in [wait["SetKey"]+"Help",wait["SetKey"]+"help"]:
                if wait["SetKey"]: md = "╔═══════════════════\n║ Gunakan Kata Awalan「%s」 \n║Untuk Menggunakan Fitur Bot\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Gimage:[Judul]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Wikipedia:[Judul]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Youtube:[Judul]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Ig info:[Name]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Musik:[Song Name]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Lirik:[Song Name]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Google:[Text]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Ig check:[Name]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Ig bio:[Name]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Ig pict:[Name]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Ig pictl:[Link]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Ig vidl:[Link]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Ig link:[Name]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Vn:[Text]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Searchid:[Id]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Searchmid:[Mid]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 AddId:[Id]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 AddMid:[Mid]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Checkmid:[Mid]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Midcover:[Mid]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Midpict:[Mid]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Midbio:[Mid]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Midname:[Mid]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Getinfo[@tag]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Getbio[@tag]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Getmid[@tag]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Getcontact[@tag]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Getpict[@tag]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Getcover[@tag]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Getpicturl[@tag]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Getcoverurl[@tag]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Myname:[Name]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Mybio:[Name]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Myname\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Mybio\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Mypict\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Mycover\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Mypicturl\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Mycoverurl\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Friendlist\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Glist/Glist2\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Copy[@tag]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Copy name[@tag]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Copy bio[@tag]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Copy pict[@tag]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Copy cover[@tag]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Gn:[Name]\n" % (wait["SetKey"])   
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Ourl/Curl\n" % (wait["SetKey"])   
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Gpict\n" % (wait["SetKey"])   
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Gpicturl\n" % (wait["SetKey"])   
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Gpict[Name]\n" % (wait["SetKey"])  
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Tagall\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Setview\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Viewseen\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Spam?\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Set spam:[Text]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Spam:10-50[@tag]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Spam [on/off] [jmlh] [text]\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Set pap:[Link]\n" % (wait["SetKey"])    
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Pap\n" % (wait["SetKey"])   
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Ifconfig\n" % (wait["SetKey"]) 
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 System\n" % (wait["SetKey"]) 
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Kernel\n" % (wait["SetKey"]) 
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Cpu\n" % (wait["SetKey"]) 
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Backup\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Aread:on/off\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Arespon: on/off\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Autokick: on/off\n" % (wait["SetKey"])
                if wait["SetKey"]: md+="╠❂͜͡➣「%s」 Backup: on/off\n" % (wait["SetKey"])                
#if wait["SetKey"]: md+="╠❂͜͡➣「%s」 ##\n" % (wait["SetKey"])                
                cl.sendText(msg.to,md + "╚═══════════════════")
                
            elif msg.text in ["Help"]:
                cl.sendText(msg.to," ❂SELFBOT V.1❂\n\nUser Prefix「" + str(wait["SetKey"]) +"」  to use the Bot(s)\nPrefix is Case sensitive but the\ncommands is not\n\n❂͜͡➣" + str(wait["SetKey"]) + "Help1 [MENU PENGHIBUR]" + "\n❂͜͡➣" + str(wait["SetKey"]) + "Help2 [MENU ID & MID]" + "\n❂͜͡➣" + str(wait["SetKey"]) +  "Help3 [MENU GET AKUN]" + "\n❂͜͡➣" + str(wait["SetKey"]) + "Help4 [MENU PROFILE]" +  "\n❂͜͡➣" + str(wait["SetKey"]) +  "Help5 [Menu Grup]" + "\n❂͜͡➣" + str(wait["SetKey"]) + "Help6 [Menu Contact]" + "\n❂͜͡➣" + str(wait["SetKey"]) + "Set" + "\n❂͜͡➣" + str(wait["SetKey"]) + "Status")
            elif msg.text in ["Key?"]:
                cl.sendText(msg.to,"My Set Keyword: 「" + str(wait["SetKey"]) + "」")
            elif "SetKey:" in msg.text:
                wait["SetKey"] = msg.text.replace("SetKey:","")
                cl.sendText(msg.to,"Set Key changed")                
#--------------------------------------------------------
#Script Get
            elif wait["SetKey"]+"Getcoverurl" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"「Cover link」\n" + str(cu))
                except:
                    cl.sendText(msg.to,"\n[homePicture]\n" + str(cu))
            elif wait["SetKey"]+"Getpicturl" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"「Picture link」\nhttps://obs.line-scdn.net/" + contact.pictureStatus)
                except:
                    cl.sendText(msg.to,"[profilePicture]\nhttps://obs.line-scdn.net/" + contact.pictureStatus)                   
            elif wait["SetKey"]+"Getinfo" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"[name]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[statusmessage]\n" + contact.statusMessage + "\n[profilePicture]\nhttps://obs.line-scdn.net/" + contact.pictureStatus + "\n[homePicture]\n" + str(cu))
                except:
                    cl.sendText(msg.to,"[name]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[statusmessage]\n" + contact.statusMessage + "\n[homePicture]\n" + str(cu))
            elif wait["SetKey"]+"Getcontact" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)
            elif wait["SetKey"]+"Getname" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"Name:\n[" + contact.displayName  + "]")
                except:
                    cl.sendText(msg.to,"Name:\n[" + contact.displayName  + "]")
            elif wait["SetKey"]+"Getbio" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"「Bio」\n\n「" + contact.statusMessage + "」")
                except:
                    cl.sendText(msg.to,"「Bio」\n\n「" + contact.statusMessage + "」")        
            elif wait["SetKey"]+"Getmid" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"「Mid」\n\n「" + contact.mid + "」")
                except:
                    cl.sendText(msg.to,"「Mid」\n\n「" + contact.mid + "」")                  
            elif wait["SetKey"]+"Getcover @" in msg.text:
                 print "[Command]dp executing"
                 _name = msg.text.replace(wait["SetKey"]+"Getcover @","")
                 _nametarget = _name.rstrip(' ')
                 gs = cl.getGroup(msg.to)
                 targets = []
                 for g in gs.members:
                     if _nametarget == g.displayName:
                         targets.append(g.mid)
                 if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                 else:
                     for target in targets:
                         try:
                             contact = cl.getContact(target)
                             cu = cl.channel.getCover(target)
                             path = str(cu)
                             cl.sendText(msg.to,"Loading Cover... || " +  _name )
                             cl.sendImageWithURL(msg.to, path)
                         except:
                             pass
                 print "[Command]dp executed"    
            elif wait["SetKey"]+"Getpict @" in msg.text:
                 print "[Command]dp executing"
                 _name = msg.text.replace(wait["SetKey"]+"Getpict @","")
                 _nametarget = _name.rstrip(' ')
                 gs = cl.getGroup(msg.to)
                 targets = []
                 for g in gs.members:
                     if _nametarget == g.displayName:
                         targets.append(g.mid)
                 if targets == []:
                     cl.sendText(msg.to,"Contact not found")
                 else:
                     for target in targets:
                         try:
                             contact = cl.getContact(target)
                             path = "https://obs.line-scdn.net/" + contact.pictureStatus
                             cl.sendText(msg.to,"Loading Pict... || " +  _name )
                             cl.sendImageWithURL(msg.to, path)
                         except:
                             pass
                 print "[Command]dp executed"                 
            elif wait["SetKey"]+"Set pap:" in msg.text:
                wait["Pap"] = msg.text.replace(wait["SetKey"]+"Set pap:","")
                cl.sendText(msg.to,"Pap Has Ben Set To")
            elif msg.text in [wait["SetKey"]+".Pap",wait["SetKey"]+"Pap"]:
                cl.sendImageWithURL(msg.to,wait["Pap"])
#--------------------------------------------------------
#Script Profile
            elif wait["SetKey"]+"Myname:" in msg.text:
                if msg.from_ in admin:
                    string = msg.text.replace(wait["SetKey"]+"Myname:","")
                    if len(string.decode('utf-8')) <= 20000:
                        profile = cl.getProfile()
                        profile.displayName = string
                        cl.updateProfile(profile)
                        cl.sendText(msg.to,"Set displayname <"+string+"> Success")
            elif wait["SetKey"]+"Mybio:" in msg.text:
                if msg.from_ in admin:
                    string = msg.text.replace(wait["SetKey"]+"Mybio:","")
                    if len(string.decode('utf-8')) <= 50000:
                        pl = cl.getProfile()
                        pl.statusMessage = string
                        cl.updateProfile(pl)
                        cl.sendText(msg.to,"Set status message "+string+" Success")
            elif msg.text in [wait["SetKey"]+"Mybio"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"StatusMessage\n\n" + h.statusMessage) 
            elif msg.text in [wait["SetKey"]+"Myname"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"My Name:\n\n" + h.displayName)
            elif msg.text in [wait["SetKey"]+"Mypicturl"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in [wait["SetKey"]+"Mycoverurl"]:
                    h = cl.getContact(mid)
                    cu = cl.channel.getCover(mid)          
                    path = str(cu)
                    cl.sendText(msg.to, path)
            elif msg.text in [wait["SetKey"]+"Mypict"]:
                    h = cl.getContact(mid)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in [wait["SetKey"]+"Mycover"]:
                    h = cl.getContact(mid)
                    cu = cl.channel.getCover(mid)          
                    path = str(cu)
                    cl.sendImageWithURL(msg.to, path)
            elif msg.text in [wait["SetKey"]+"Friendlist"]:
                if msg.from_ in admin:
                    anl = cl.getAllContactIds()
                    ap = ""
                    for q in anl:
                        ap += "•"+cl.getContact(q).displayName + "\n"
                    cl.sendText(msg.to,"「• Friendlist •」\n"+ap+"Total Friendlist:"+str(len(anl)))
            elif msg.text in [wait["SetKey"]+"Glist2"]:
              if msg.from_ in admin:
                gs = cl.getGroupIdsJoined()
                L = "『 Groups List 』\n"
                for i in gs:
                    L += "[≫] %s \n" % (cl.getGroup(i).name + " | [ " + str(len (cl.getGroup(i).members)) + " ]")
                cl.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in [wait["SetKey"]+"Glist"]:
                gid = cl.getGroupIdsJoined()
                h = ""
		jml = 0
                for i in gid:
		    gn = cl.getGroup(i).name
                    h += "♦【%s】\n" % (gn)
		    jml += 1
                cl.sendText(msg.to,"======[List Group]======\n"+ h +"Total group:"+str(jml))                    
#--------------------------------------------------------
#Hanya bisa di Grup
            elif (wait["SetKey"]+"Gn:" in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn:","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif msg.text in ["Memberlist"]:   
                kontak = cl.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="════List Member════-"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════List Member═════\n\nTotal Members : %i" % len(group)
                cl.sendText(msg.to, msgs)
            elif "Gid" == msg.text:
                cl.sendText(msg.to,msg.to)
            elif msg.text in [wait["SetKey"]+"Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in [wait["SetKey"]+"Ourl",wait["SetKey"]+"Url:on"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    cl.sendText(msg.to,"Url Active")
                else:
                    cl.sendText(msg.to,"Can not be used outside the group")
            elif msg.text in [wait["SetKey"]+"Curl",wait["SetKey"]+"Url:off"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    cl.sendText(msg.to,"Url inActive")

                else:
                    cl.sendText(msg.to,"Can not be used outside the group")
            elif wait["SetKey"]+"Gpict" in msg.text:
                group = cl.getGroup(msg.to)
                path ="https://obs.line-scdn.net/" + group.pictureStatus
                cl.sendText(msg.to,"Loading....")
                cl.sendImageWithURL(msg.to, path)
            elif wait["SetKey"]+"Gpicturl" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendText(msg.to,path)
            elif wait["SetKey"]+"Gpict:" in msg.text:
                saya = msg.text.replace(wait["SetKey"]+'Gpict:','')
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).name
                    gna = cl.getGroup(i)
                    if h == saya:
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
            elif wait["SetKey"]+"Setview" in msg.text:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                cl.sendText(msg.to, "Checkpoint checked!")
                print "@setview"
            elif wait["SetKey"]+"Viewseen" in msg.text:
	        lurkGroup = ""
	        dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = cl.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        tukang = "List Viewer\n*"
                        grp = '\n* '.join(str(f) for f in dataResult)
                        total = '\n\nTotal %i viewers (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S') )
                        cl.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                    else:
                        cl.sendText(msg.to, "Belum ada viewers")
                    print "@viewseen"
#--------------------------------------------------------
#Script Spam
            elif wait["SetKey"]+"Spam " in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace(wait["SetKey"]+"Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                #Vicky Kull~
                if txt[1] == "on":
                    if jmlh <= 100000:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Out of Range!")
                elif txt[1] == "off":
                    if jmlh <= 100000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")
            elif wait["SetKey"]+"Spam @" in msg.text:
                _name = msg.text.replace(wait["SetKey"]+"Spam @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(msg.to,"Start Spam")
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(msg.to, "Spam Succes")
                       print "Done spam"          
            elif wait["SetKey"]+"Spam:10 @" in msg.text:
                _name = msg.text.replace(wait["SetKey"]+"Spam:10 @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(msg.to,"Start Spam")
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(msg.to, "Spam Succes")
                       print "Done spam"    
            elif wait["SetKey"]+"Spam:15 @" in msg.text:
                _name = msg.text.replace(wait["SetKey"]+"Spam:15 @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(msg.to,"Start Spam")
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(msg.to, "Spam Succes")
                       print "Done spam"    
            elif wait["SetKey"]+"Spam:20 @" in msg.text:
                _name = msg.text.replace(wait["SetKey"]+"Spam:20 @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(msg.to,"Start Spam")
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(msg.to, "Spam Succes")
                       print "Done spam"                           
            elif wait["SetKey"]+"Spam:25 @" in msg.text:
                _name = msg.text.replace(wait["SetKey"]+"Spam:25 @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(msg.to,"Start Spam")
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(msg.to, "Spam Succes")
                       print "Done spam"                           
            elif wait["SetKey"]+"Spam:30 @" in msg.text:
                _name = msg.text.replace(wait["SetKey"]+"Spam:30 @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(msg.to,"Start Spam")
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(msg.to, "Spam Succes")
                       print "Done spam"  
            elif wait["SetKey"]+"Spam:35 @" in msg.text:
                _name = msg.text.replace(wait["SetKey"]+"Spam:35 @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(msg.to,"Start Spam")
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(msg.to, "Spam Succes")
                       print "Done spam"                              
            elif wait["SetKey"]+"Spam:40 @" in msg.text:
                _name = msg.text.replace(wait["SetKey"]+"Spam:40 @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(msg.to,"Start Spam")
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(msg.to, "Spam Succes")
                       print "Done spam"       
            elif wait["SetKey"]+"Spam:50 @" in msg.text:
                _name = msg.text.replace(wait["SetKey"]+"Spam:50 @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))

                       cl.sendText(msg.to, "Spam Succes")
                       print "Done spam"       
            elif msg.text in [wait["SetKey"]+"Spam?"]:
                cl.sendText(msg.to,"Spam saat ini telah ditetapkan sebagai berikut:\n\n" + str(wait["spam"]))
            elif wait["SetKey"]+"Set spam:" in msg.text:
                wait["spam"] = msg.text.replace(wait["SetKey"]+"Set spam:","")
                cl.sendText(msg.to,"spam changed")
            elif wait["SetKey"]+"Spam add:" in msg.text:
                wait["spam"] = msg.text.replace(wait["SetKey"]+"Spam add:","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"spam changed")
                else:
                    cl.sendText(msg.to,"Done")
            elif wait["SetKey"]+"Spam:" in msg.text:
                strnum = msg.text.replace(wait["SetKey"]+"Spam:","")
                num = int(strnum)
                for var in range(0,num):
                    cl.sendText(msg.to, wait["spam"])
            elif wait["SetKey"]+"Spamtag @" in msg.text:
                _name = msg.text.replace(wait["SetKey"]+"Spamtag @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                    else:
                        pass                    
#--------------------------------------------------------
#Script Copy Profile
            elif wait["SetKey"]+"Copy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace(wait["SetKey"]+"Copy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Succes Copy Contact profile")
                                except Exception as e:
                                    print e
            elif wait["SetKey"]+"Copy pict @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace(wait["SetKey"]+"Copy pict @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    cl.clonePictureProfile(target)
                                    cl.sendText(msg.to, "Succes Copy Picture profile")
                                except Exception as e:
                                    print e                                    
            elif wait["SetKey"]+"Copy cover @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace(wait["SetKey"]+"Copy cover @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneCoverProfile(target)
                                    cl.sendText(msg.to, "Succes Copy Cover profile")
                                except Exception as e:
                                    print e                                
            elif wait["SetKey"]+"Copy name @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace(wait["SetKey"]+"Copy name @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneNameProfile(target)
                                    cl.sendText(msg.to, "Succes Copy Name profile")
                                except Exception as e:
                                    print e  
            elif wait["SetKey"]+"Copy bio @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace(wait["SetKey"]+"Copy bio @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneStatusProfile(target)
                                    cl.sendText(msg.to, "Succes Copy Bio profile")
                                except Exception as e:
                                    print e                                           
            elif msg.text in [wait["SetKey"]+"Backup"]:
                try:
                    cl.updateDisplayPicture(kembali.pictureStatus)
                    cl.updateProfile(kembali)
                    cl.sendText(msg.to, "backup done")
                except Exception as e:
                    cl.sendText(msg.to, str (e))
#--------------------------------------------------------
#
#--------------------------------------------------------
#============Mimic Start=========#
            elif (wait["SetKey"]+"Micadd " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        cl.sendText(msg.to,"Target ditambahkan!")
                        break
                    except:
                        cl.sendText(msg.to,"Fail !")
                        break
                    
            elif (wait["SetKey"]+"Micdel " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del mimic["target"][target]
                        cl.sendText(msg.to,"Target dihapuskan!")
                        break
                    except:
                        cl.sendText(msg.to,"Fail !")
                        break
                    
            elif msg.text in [wait["SetKey"]+"Miclist"]:
                        if mimic["target"] == {}:
                            cl.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in mimic["target"]:
                                mc += "?? "+cl.getContact(mi_d).displayName + "\n"
                            cl.sendText(msg.to,mc)

            elif wait["SetKey"]+"Mimic target " in msg.text:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace(wait["SetKey"]+"Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                cl.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                cl.sendText(msg.to,"Mimic change to target")
                            else:
                                cl.sendText(msg.to,"I dont know")
            
            elif wait["SetKey"]+"Mimic " in msg.text:
                cmd = msg.text.replace(wait["SetKey"]+"Mimic ","")
                if cmd == "on":
                    if mimic["status"] == False:
                        mimic["status"] = True
                        cl.sendText(msg.to,"Reply Message on")
                    else:
                        cl.sendText(msg.to,"Sudah on")
                elif cmd == "off":
                    if mimic["status"] == True:
                        mimic["status"] = False
                        cl.sendText(msg.to,"Reply Message off")
                    else:
                        cl.sendText(msg.to,"Sudah off")
#--------------------------------------------------------
#
#--------------------------------------------------------
#Block
            elif wait["SetKey"]+"Blacklist all" in msg.text:
              if msg.from_ in admin:
                  if msg.toType == 2:
                       print "ok"
                       _name = msg.text.replace(wait["SetKey"]+"Blacklist all","")
                       gs = cl.getGroup(msg.to)
                       cl.sendText(msg.to,"Succes")
                       targets = []
                       for g in gs.members:
                           if _name in g.displayName:
                                targets.append(g.mid)
                       if targets == []:
                            cl.sendText(msg.to,"Maaf")
                       else:
                           for target in targets:
                               if not target in Bots:
                                   try:
                                       wait["blacklist"][target] = True
                                       f=codecs.open('st2__b.json','w','utf-8')
                                       json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                   except:
                                       cl.sentText(msg.to,"Succes")

	    elif wait["SetKey"]+"Scbl:on" in msg.text:
	        wait["wblacklist"] = True
	    	cl.sendText(msg.to,"Block Send contact Active")

	    elif wait["SetKey"]+"Scubl:on" in msg.text:
	    	wait["dblacklist"] = True
	    	cl.sendText(msg.to,"Unblock Send contact Active")
            elif wait["SetKey"]+"Bl @" in msg.text:
                if msg.toType == 2:
                    print "@Block by mention"
                    _name = msg.text.replace(wait["SetKey"]+"Bl @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
			    if target not in admin:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"    「Succes」\n「Fitur」: Add Blocklist\n「Account Name」: " + _name)
                                except:
                                    cl.sendText(msg.to,"Error")
			    else:
				cl.sendText(msg.to,"Admin Detected~")
#--------------------------------------------------------
            elif msg.text in [wait["SetKey"]+"Blist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"nothing")
                else:
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,"===[Blocklist User]===\n"+mc)

#--------------------------------------------------------
            elif wait["SetKey"]+"Ubl @" in msg.text:
                if msg.toType == 2:
                    print "@Unban by mention"
                    _name = msg.text.replace(wait["SetKey"]+"Ubl @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"    「Succes」\n「FITUR」: Unblocklist\n「Account Name」: " + _name)
                            except:
                                cl.sendText(msg.to,"    「Succes」\n「FITUR」: Unblocklist\n「Account Name」: " + _name)
#--------------------------------------------------------
#Script Speed
            elif msg.text in ["Speed","Sp","speed","Debug speed"]:
                start = time.time()
                cl.sendText(msg.to, "「 Debug Speed」\nSpeed is STARTING♪")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "「 Debug Speed」\nSpeed is STARTING♪\n%sseconds􏿿" % (elapsed_time))
#--------------------------------------------------------
#Script Kick
            elif "Uk " in msg.text:
                  if msg.from_ in admin:
                       ulti0 = msg.text.replace("Uk ","")
                       ulti1 = ulti0.lstrip()
                       ulti2 = ulti1.replace("@","")
                       ulti3 = ulti2.rstrip()
                       _name = ulti3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ki.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
	    elif "Vk " in msg.text:
		if 'MENTION' in msg.contentMetadata.keys()!= None:
		    names = re.findall(r'@(\w+)', msg.text)
		    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
		    mentionees = mention['MENTIONEES']
		    print mentionees
		    for mention in mentionees:
			cl.kickoutFromGroup(msg.to,[mention['M']])
#--------------------------------------------------------
#Script Tagall
            elif msg.text.lower() in ["aa"]:
              if msg.from_ in admin:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                if jml <= 100:
                    mention(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 100):
                            nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, len(nama)):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                if jml > 200 and jml < 300:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, len(nama)):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                if jml > 300 and jml < 400:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, len(nama)):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                if jml > 400 and jml < 500:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, 400):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                    for h in range(401, len(nama)):
                        nm5 += [nama[h]]
                    mention(msg.to, nm5)
                if jml > 500:
                    cl.sendText(msg.to,'Member melebihi batas.')
                    cnt = Message()
                    cnt.text = "Done : " + str(jml) +  " Members"
                    cnt.to = msg.to
                    cl.sendMessage(cnt)     
#--------------------------------------------------------
#Script System
            elif msg.text.lower() ==  wait["SetKey"]+'ifconfig':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() ==  wait["SetKey"]+'system':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() ==  wait["SetKey"]+'kernel':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() ==  wait["SetKey"]+'cpu':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
#--------------------------------------------------------
#
            elif msg.text in ["Creator"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': wait["creator"]}
                cl.sendMessage(msg)
            elif wait["SetKey"]+"Set ct:" in msg.text:
                wait["creator"] = msg.text.replace(wait["SetKey"]+"Set ct:","")
                cl.sendText(msg.to,"Creator Has Ben Set To")
            elif msg.text in [wait["SetKey"]+"Ct",wait["SetKey"]+"ct"]:
                cl.sendImageWithURL(msg.to,wait[""])
#--------------------------------------------------------
#
#--------------------------------------------------------
        if op.type == 59:
            print op


    except Exception as error:
        print error

#thread2 = threading.Thread(target=nameUpdate)
#thread2.daemon = True
#thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
#Edited By Fal		
