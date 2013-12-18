import random
import sys
from util import hook

@hook.command('coffee',autohelp=False)
def coffee(inp, say=None):
	return "I got you coffee!"
	
@hook.command('getme',autohelp=False)
def getme(inp, say=None):
	return "I got you " + inp + "!"

@hook.command('meeting',autohelp=False)
def meeting(inp, say=None):
	n = random.randint(0, 18)
	if n == 0:
		return "Shitposting projections appear to be on target"
	elif n == 1:
		return "We need seemless integration between the shitposting and shitchatting!"
	elif n == 2:
		return "Introducing shitcloud support: Shitposting + the cloud!"
	elif n == 3:
		return "How can we integrate shitposts into the cloud?"
	elif n == 4:
		return "What about geolocation and geofencing with our shitposts?"
	elif n == 5:
		return "Our customer wants flex shitting! Why don't we have flex shitting?"
	elif n == 6:
		return "Who is the biggest crew around? Let's be like them!"
	elif n == 7:
		return "Our mission statement is clear and simple: Shitpost, shitpost, shitpost"
	elif n == 8:
		return "{whatever the last guy said}"
	elif n == 9:
		return "Shitposting is down 22% but shit chatting is up 14%."
	elif n == 10:
		return "Who is the leader in our industry? We should shitpost like them."
	elif n == 11:
		return "Sorry, I fell asleep."
	elif n == 12:
		return "Sorry I'm late. Please explain everything we've discussed in agonizing detail."
	elif n == 13:
		return "We need to synergize our shitposts with the cloud. A social media platform with geolocation and mobile app support should be great!"
	elif n == 14:
		return "Your shitpost efficiency has been steadily declining, shitpost more."
	elif n == 15:
		return "We should meet on this again, every day, for one hour during your lunch."
	elif n == 16:
		return "What about 'bitcoins'?"
	elif n == 17:
		return "What about 'buttcoins'?"
	elif n == 18:
		return "Due to increased costs of heavy 'serious' posts, christmas bonuses will not be given out this year."
	return "ZZZZZzzzzzzz!"
	
	
	