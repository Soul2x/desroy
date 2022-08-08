import getpass
import aminofix
import time
import os
import sys
import getpass
import colorama
import termcolor
import pyfiglet
from colorama import init, Fore, Back, Style
init()

A = "\033[1;91m"  #احمر
Z1 = '\033[2;31m' #احمر ثاني
E = "\033[1;92m"  #اخضر
H = "\033[1;93m" #اصفر
L = "\033[1;95m" #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح 
M = "\033[1;94m" #ازرك
t = "_"
p = H+"¥"
n = H+"1"+A
o = H+"2"+A
print(H+pyfiglet.figlet_format("  BY Sparta "))
print (L+"_ "*30)
print(Back.BLACK)
print(Fore.YELLOW + Style.BRIGHT)
print('''Script by Sparta''')
#print(pyfiglet.figlet_format("Amino MASS SPAM Sparta",font="old"))

from threading import Thread
import aminofix as amino
def out_blue(text):
 print("\ {}" .format(text))

XS_1 = ("1")
XS_2 = ("2")
XS_3 = ("3")
XS_4 = ("4")
XS_5 = ("5")
XS_6 = ("6")
XS_clear = ("clear")
time.sleep(0)
print("∆-1.Tools current not everything works! ")
print("∆-2.spam")

XS=input("Choose optional:-")
time.sleep(0)
XS_2 = input("click ENTER)")
time.sleep(0)
print("Note!  Below are the message types")
print("1. 1- Strike message")
time.sleep(0)
print("2.55- Regular message")
time.sleep(0)
print("3.50-Not supported message type")
time.sleep(0)
print("4.57-Voice Chat Rejection")
time.sleep(0)
print("5.59-Enable voice chat")
time.sleep(0)
print("6.100-Post that can be deleted")
time.sleep(0)
print("7.101-Entering the chat")
time.sleep(0)
print("8.102-Drop from chat")
time.sleep(0)
print("9.103-start chat")
time.sleep(0)
print("10.104-Change chat background")
time.sleep(0)
print("11.105-Edit chat")
time.sleep(0)
print("12.106-Editing the chat icon")
time.sleep(0)
print("13.107-Start voice chat")
time.sleep(0)
print("14.109-System message")
time.sleep(0)
print("15.110-End voice chat")
time.sleep(0)
print("16.113-Edit chat description")
time.sleep(0)
print("17.114-Start live mode")
time.sleep(0)
print("18.115-Turn off live mode")
time.sleep(0)
print("19.116-New chat with host")
time.sleep(0)
print("20.124-Invite everyone online")
time.sleep(0)
print("21.125-Enable View Mode")
time.sleep(0)
print("22.126-Disable View Mode")
time.sleep(0)
print("Not used to living calmly and normally")
time.sleep(0)

r = 0
email=input("Email :")
password=input('Password :')
client = amino.Client()
client.login(email=email, password=password)
clients = client.sub_clients(start=0, size=1000)
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
communityid = clients.comId[int(input("اختار منتدى/Select the community: "))-1]


msgSpam=input('Message/رساله:')
print('MessageTypes/ عادي:Default-0,Transparent-100/55/109/50')
msgType=input('MessageType/نوع الرساله:')

r = 1000;



def spam(sub_client, chatId, msgSpam, msgType):
	while True:
		try: sub_client.send_message(message=msgSpam, chatId=chatId, messageType=msgType)
		except: pass

def start_thread(sub_client, chatId, msgSpam, msgType):
	global r;
	for i in range(r):
		Thread(target=spam, args=(sub_client, chatId, msgSpam, msgType)).start();
        

# == Ресурсы   ==

sub_client = amino.SubClient(comId=str(communityid), profile=client.profile)

threads_list = sub_client.get_chat_threads().json;

for t in threads_list:
	Thread(target=start_thread, args=(sub_client, t["threadId"], msgSpam, msgType)).start();

print("Spamming in all attacks");

print("Speed ​​message sent")				

print("033[44m-Amino Utilities selected, loading..")

green=""
red=""
white=""
blue=""
db_1 = ("1")
db_2 = ("2")
db_3 = ("3")
db_4 = ("4")
db_5 = ("5")
db_6 = ("6")
db_7_= ("7")
db_8_= ("8")
db_clear = ("clear")
print ("Amino services 2021")
time.sleep(0)
print ("By Pilot")
time.sleep(0)
print ("Buddy after the initial loading of the initial page from below, enter the email and password for which you want to activate this script, enjoy using" )
time.sleep(0)
print ("The tool kit is loaded:")
time.sleep(0)
print("Preparing to work in the Python environment, loading all the necessary components, it will take a few seconds")
print (" ")
time.sleep(0)
email=input("Enter your email: ")
password=input("enter password: ")
client=amino.Client()
client.login(email=email ,password=password)

print ("[1] Chat Toolkit~")
print ("[2] Comment option~")
print ("[3] Create a chat~")
print ("[4] Creating a blog~")
print ("[5] In development~")
print ("[6] Tutorial~")
print ("[7] Farm Coin Generator~")
print ("[8] Autoregistration~")
nacher=input("Choose an option: ")
def Bot(data):
    listusers=[]
    for userId ,status in zip(data.profile.userId,data.profile.status):
       if status!=9 and status !=10:
           listusers.append(userId)
    return listusers

if daddy== db_1:
	curl=input("Paste chat link : ")
	courl=client.get_from_code(curl)
	chatid=courl.objectId
	comid=courl.path[1:courl.path.index('/')]
	
	print (" ")
	print ("[1] Regular message")
	print ("[2] System message")
	print ("[3] Deleting a chat")
	print ("[4] Join & leave from chat")
	print ("[5] Invite HH")
	print ("[0] back to menu")
	user=input("Choose: ")
	if user== db_1:
		print ("[1] Regular dispatch")
		print ("[2] Sending spam")
		print ("[3]Tools ")
		print ("[0] Back to menu")
		nos=input("Choose an option: ")
		if nos== db_1:
			subclient = amino.SubClient(comId=comid , profile=client.profile)
			while True:
				massage=input("Message type: ")
				subclient.send_message(message=massage, chatId=chatid , messageType=0)
				if massage== db_clear:
					os.system("cleaning")
				
		if nos== db_2:
			subclient=amino.SubClient(comId=comid  ,profile=client.profile)
			mass = input("Enter a message: ")
			while True:
				try:
					subclient.send_message(message=mass ,chatId=chatid ,messageType=0)
					print ("Message sent!")
				except:
					pass
					print ("Error sending strike message!  Error analysis, perhaps a syntax error, or an incorrectly formed line of commands.  Do not enter spaces in commands, not messages, this affects the performance of this script")
		
		if nos== db_3:
			print ("[1] Sending a normal strike message")
			print ("[2] Sending regular message, can't delete")
			print ("[0] Back to menu")
			hde = input("Choose an option:")
			if hde== db_1:
				print ("[1] Regular dispatch")
				print ("[2] Spam sending")
				print ("[0] Back to menu")
				nsl =input("Choose an option: ")
				if nsl== db_1:
					subclient=amino.SubClient(comId=comid ,profile=client.profile)
					while True:
						try:
							massage=input("Enter your message: ")
							subclient.send_message(message=massage , chatId=chatid , messageType=0)
							if massage== db_clear:
								os.system("cleaning")
						except:
							pass
						
				if nsl== db_2:
					subclient=amino.SubClient(comId=comid ,profile=client.profile)
					mas=input("Enter your message: ")
					while True:
						try:
							subclient.send_message(message=mas ,chatId=chatid ,messageType=0)
							print ("Message sent")
						except:
							pass
							print ("Error sending strike messages!  I check for errors.  Found, most likely the type of this message works as an invisible code and harms the server itself, but not the chat.  Use Wisely")
						
				if nsl== db_0:
					os.system("exit")
					exit()
				
			
			if hde== db_2:
				print ("[1] Regular dispatch")
				print ("[2] Spam by unknown message type")
				nsa=input("Choose an option: ")
				if nsa==db_1:
					subclient=amino.SubClient(comId=comid ,profile=client.profile)
					while True:
						massage=input("Enter your message: ")
						try:
							subclient.send_message(message=massage ,chatId=chatid ,messageType=0)
							if massage== db_clear:
								os.system("cleaning")
						except:
							pass
				
				if nsa==db_2:
					subclient=amino.SubClient(comId=comid ,profile=client.profile)
					massage=input("Enter messages: ")
					while True:
						try:
							subclient.send_message(message=massage ,chatId=chatid , messageType=50)
							print ("Message sent successfully")
						except:
							pass
							print ("Sending error, bug.  The problem may be due to two reasons.  The first one is most likely you were banned by dealers or anti-raid. The second one was an inaccessible value or message")
				if nsa== db_0:
					os.system("Return")
					exit()
				
			if hde== db_0:
				os.system("Return")
				exit()
			
			
		if nos== db_0:
			os.system("Return")
			exit()
	if user== db_2:
		print ("[1] Regular dispatch")
		print ("[2] System spam-109 type")
		print ("[0] Back to menu")
		tnos =input("Choose an option: ")
		if tnos== db_1:
			subclient=amino.SubClient(comId=comid ,profile=client.profile)
			while True:
				try:
					massage=input("Enter your message: ")
					subclient.send_message(message=massage ,chatId=chatid , messageType=109)
					if massage== db_clear:
						os.system("cleaning")
				except:
					pass
		if tnos== db_2:
			subclient=amino.SubClient(comId=comid ,profile=client.profile)
			massage=input("Enter your message: ")
			while True:
				try:
					subclient.send_message(message=massage ,chatId=chatid , messageType=109)
					print ("System message sent successfully")
				except:
					pass
					print ("Error sending a system message, if an error of this kind occurs, then most likely you have exceeded the limit, entered invalid text")
		if tons== db_0:
			os.system("cleaning")
			exit()
	
	if  user== db_3:
		print ("You must be a chat assistant")
		userid=input("Link to chat host")
		userid=client.get_from_code(userid).objectId
		subclient=amino.SubClient(comId=comid ,profile=client.profile)
		subclient.ban(userId=userid ,chatId=chatid, allowRejoin=True)
	if user== db_4:
		print ("[1] Invitation")
		print ("[2] Liv from chat")
		print ("[3] spam")
		jls = input("Choose an option: ")
		if jls== db_1:
			subclient.join_chat(chatId=chatId)
			print ("Ready.. .  Chat invitation completed")
		if jls== db_2:
			subclient.leave_chat(chatId=chatId)
			print ("Done... start dumping from chat")
		if jls== db_3:
			subclient=amino.SubClient(comId=comid ,profile=client.profile)
			while True:
				try:
					subclient.join_chat(chatId=chatid)
					print ("Done... started spamming the intro")
					subclient.leave_chat(chatId=chatid)
					print ("Done... started by spamming")
				except:
					pass
					print ("Unexpected error, error initialization..please wait..")
	if user== db_5:
		com=client.get_from_code(curl)
		comId=com.path[1:com.path.index('/')]
		subclient=amino.SubClient(comId=comId ,profile=client.profile)
		members=int(input("enter the number of participants you want to invite: "))
		home=0
		while members>home and len(subclient.get_online_users(start=home ,size=25).profile.userId)!=0:
			users=subclient.get_online_users(start=home ,size=25)
			for userId in Bot(users):
				try:
					subclient.invite_to_chat(userId=userId ,chatId=chatid)
					print ("Invited!")
					home=0+1
		
				except:
					pass
					print ("There was an error in inviting participants!  Please try later, or make sure that those you invite have opened access to the invitation, zai")
				if home== members:
					print ("End invitation ->"+home+"<- members")
					os._exit(1)
		

if hacker== db_2:
	print ("[1]~ profile wall")
	print ("[2]~Wiki section")
	print ("[3]~ Fast")
	wwb = input ("Choose an option: ")
	if wwb== db_1:
		userlink=input("Go to the community in which you are a member and by clicking on the user profile, copy its ID link and paste it here : ")
		user=client.get_from_code(userlink)
		userId=user.objectId
		comId=user.path[1:user.path.index('/')]
		subclient=amino.SubClient(comId=comId ,profile=client.profile)
		print ("[1] Regular comment")
		print ("[2] Spam comments")
		cs = input("Choose an option: ")
		if cs== db_1:
			while True:
				try:
					comment=input("Comment type - enter what you want to send to the participant's wall: ")
					subclient.comment(message=comment , userId=userId ,isGuest=False)
				except:
					pass
		if cs== db_2:
			comment=input("Comment type: ")
			while True:
				try:
					subclient.comment(message=comment ,userId=userId ,isGuest=False)
					print ("Comment sent")
				except:
					pass
					print ("Unexpected error sending comment, maybe your message contains invalid characters or exceeded the limit")
	if wwb== db_2:
				wikilink=input("Link to user's article: ")
				wiki=client.get_from_code(wikilink)
				wikiId=wiki.objectId
				comId=wiki.path[1:wiki.path.index('/')]
				print ("[1] Regular comment")
				print ("[2] ddos comments")
				ns=input("Choose an option: ")
				if ns== db_1:
					subclient=amino.SubClient(comId=comId ,profile=client.profile)
					while True:
						try:
							comment=input("Enter a comment: ")
							subclient.comment(message=comment ,wikiId=wikiId ,isGuest=False)
						except:
							pass
				if ns== db_2:
					subclient=amino.SubClient(comId=comId ,profile=client.profile)
					comment=input("Enter a comment: ")
					while True:
						try:
							subclient.comment(message=comment ,wikiId=wikiId ,isGuest=False)
							print("the comment was successfully sent!")
						except:
							pass
							print ("Error submitting comment, user may have blocked you")
	if wwb== db_3:
		bloglink=input("Link to member's post: ")
		blog=client.get_from_code(bloglink)
		blogId=blog.objectId
		comId=blog.path[1:blog.path.index('/')]
		print ("[1] Regular comment")
		print ("[2] Spam attack by comments")
		csn=input("Choose an option: ")
		if csn== db_1:
			subclient=amino.SubClient(comId=comId ,profile=client.profile)
			while True:
				try:
					comment=input("Enter your desired comment:")
					subclient.comment(message=comment ,blogId=blogId ,isGuest=False)
				except:
					pass
		if csn== db_2:
			subclient=amino.SubClient(comId=comId ,profile=client.profile)
			comment=input("Enter your desired comment: ")
			while True:
				try:
					subclient.comment(message=comment ,blogId=blogId ,isGuest=False)
					print ("Your comment has been sent to the victim")
				except:
					pass
					print ("The victim found out about your intention, or you were blocked and denied access.  Or you got caught in the ban, be vigilant.  I am updating to the previous state.  May take a few seconds")
					
if hacker== db_3:
	userlink=input("Member profile link: ")
	user=client.get_from_code(userlink)
	userId=user.objectId
	comId=user.path[1:user.path.index('/')]
	firstmess=input("Enter the message you would like to send to your future chat: ")
	title=input("Enter the future name of the chat: ")
	content=input("Choose the type of chat, relative to the content: ")
	subclient=amino.SubClient(comId=comId ,profile=client.profile)
	print ("Is the chat global?")
	print ("[1] yes, sure")
	print ("[2] no I do not think so")
	yng=input("Choose an option: ")
	if yng== db_1:
		print ("[1] I create a regular chat with the usual single message sending")
		print ("[2] Creating a ray attack node with PR and spam pooling, wait honey..")
		cwns=input("Choose an option: ")
		if cwns== db_1:
			try:
				subclient.start_chat(userId=userId ,message=firstmess,title=title ,content=content ,isGlobal=True ,publishToGlobal=False)
				print("Congratulations!  Chat created successfully")
			except:
				print("An error has occurred!  Perhaps you were caught spamming, or it is forbidden to create chats with a low level in soo")
				os.system("Return")
				exit()
		if cwns== db_2:
			while True:
				try:
					subclient.start_chat(userId=userId ,message=firstmess ,title=title ,content=content ,isGlobal=True ,publishToGlobal=False)
					print ("Chat created successfully!")
				except:
					pass
					print ("Error..There may be a restriction on the creation of chats, because the chat you created was not processed")
	if yng== db_2:
		print ("[1] Completing the creation of a regular chat")
		print ("[2] Preparing components for a raid-PR attack on chats")
		cwns=input("Choose an option: ")
		if cwns== db_1:
			try:
				subclient.start_chat(userId=userId ,message=firstmess ,title=title ,content=content ,isGlobal=False ,publishToGlobal=False)
				print("Chat created successfully")
			except:
				print("Error..There is an invalid component in your chat, or you have created too many chats with this script, please re-login.  And the problem should be gone")
		if cwns== db_2:
			while True:
				try:
					subclient.start_chat(userId=userId ,message=firstmess ,title=title ,content=content ,isGlobal=False ,publishToGlobal=False)
					print ("Chat created successfully")
				except:
					pass
					print ("Error, make sure you have all the components installed, check your internet connection")

if hacker== db_4:
	userlink=input("Insert a link to your offender, or your own: ")
	user=client.get_from_code(userlink)
	comId=user.path[1:user.path.index('/')]
	subclient=amino.SubClient(comId=comId ,profile=client.profile)
	title=input("Enter the name of your not yet created post: ")
	content=input("Creating a post within the community: ")
	
	print ("[1] The creation of a regular post begins")
	print ("[2] Malicious spam mail creation begins")
	print ("[0] Return")
	mbgORmbs=input("Choose an option: ")
	if mbgORmbs== db_1:
		try:
			subclient.post_blog(title=title, content=content ,categoriesList=None ,backgroundColor=None ,fansOnly=None ,extensions=None)
			print ("Post successfully created")
		except:
			print ("Error creating post, check if your network connection is excellent")
	if mbgORmbs== db_2:
		while True:
			try:
				subclient.post_blog(title=title, content=content ,categoriesList=None ,backgroundColor=None ,fansOnly=None ,extensions=None);
				print ("Post successfully created")
			except:
				pass
				print ("Error creating post!  You haven't reached level six yet")
	if mbgORmbs== db_3:
		os.system("Return")
		exit()
		sys.exit()

exit()
os.system("Return")
sys.exit()