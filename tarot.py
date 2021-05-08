import cmd
import textwrap 
import sys
import os 
import time
import random 
print('                                          ██▒▒▒▒██                                          ')
print('                                          ██▓▓▓▓██                                          ')
print('                                      ██████▓▓▓▓██████                                      ')
print('        ▓▓                          ██▒▒▒▒██▓▓▓▓██▒▒▒▒██                                    ')
print('      ▒▒▒▒                        ██▓▓▒▒▒▒▒▒████▒▒▒▒▒▒▓▓██              ▓▓                  ')
print('                                ██▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓██          ▓▓▓▓                  ')
print('                              ██▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓██                              ')
print('                            ██▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓██                            ')
print('                          ██▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓██                          ')
print('                        ██▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓██                      ▓▓')
print('                      ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                    ▓▓')
print('                    ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                    ')
print('                  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                  ')
print('                ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                ')
print('                ██▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒██                ')
print('                ██▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒██                ')
print('                  ██▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒██                  ')
print('                    ██▒▒▒▒▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▒▒▒▒██                    ')
print('                      ██▒▒▒▒▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▒▒▒▒██                      ')
print('                ▒▒    ▒▒██▒▒▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒▒▒██▒▒                      ')
print('                ▓▓▓▓  ▒▒░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░▒▒                      ')
print('                      ▒▒░░▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░▒▒                      ')
print('                      ▒▒░░░░░░▓▓██▓▓████▓▓████████▓▓██▓▓████▓▓░░▒▒░░▒▒                      ')
print('  ▒▒                    ▒▒░░▒▒██▓▓▓▓██░░░░▒▒▒▒░░░░░░▒▒██▓▓▒▒██░░░░▒▒  ░░                    ')
print('                        ▒▒░░░░██▒▒▓▓██░░░░░░░░░░░░░░░░██▒▒▓▓██░░░░▒▒          ░░            ')
print('                        ▒▒░░░░██▓▓▓▓▓▓██░░░░░░░░░░░░██▓▓▓▓▓▓██░░░░▒▒        ▓▓▓▓            ')
print('                          ▒▒░░░░██▓▓▓▓██░░░░░░░░░░░░██▒▒▓▓██░░░░▒▒                          ')
print('                          ▒▒░░░░██▓▓▓▓██░░░░░░░░░░░░██▓▓▓▓██░░░░▒▒                          ')
print('                          ▒▒░░░░██▓▓▓▓██░░░░░░░░░░░░██▓▓▓▓██░░░░▒▒                          ')
print('                            ▒▒░░██▓▓▓▓██░░░░    ░░░░██▓▓▓▓██░░▒▒                            ')
print('                            ▒▒░░██▓▓▓▓▓▓██░░    ░░██▓▓▓▓▓▓██░░▒▒                            ')
print('                            ▒▒░░░░██▓▓▓▓██        ██▓▓▓▓██░░░░▒▒                            ')
print('              ▓▓              ▒▒░░██▓▓▓▓██        ██▓▓▓▓██░░▒▒                              ')
print('              ▓▓▓▓            ▒▒░░██▓▓▓▓██░░    ░░██▓▓▓▓██░░▒▒                      ▓▓      ')
print('                              ▒▒░░██▓▓▓▓██░░░░░░░░██▓▓▓▓██░░▒▒                      ▓▓▒▒    ')
print('                                ▒▒▒▒▓▓▓▓██░░░░░░░░██▓▓▓▓▒▒▒▒                                ')
print('                                ▒▒██▓▓▓▓██░░░░░░░░██▓▓▓▓██▒▒                                ')
print('                                  ██▓▓▓▓▒▒████████▒▒▓▓▓▓██                                  ')
print('                                ████▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓████                                ')
print('                              ██▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒██                              ')
print('                              ██▓▓▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒▓▓██                              ')
print('                              ██▓▓▓▓▒▒██▓▓▓▓▓▓▓▓▓▓▓▓██▒▒▓▓▓▓██                              ')
print('                                ██▓▓▓▓▒▒████████████▒▒▓▓▓▓██                                ')
print('                                  ██▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓██                                  ')
print('                                    ██▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒██                                    ')
print('                                      ████████████████                                      ')
print('                                      ░░    ░░░░░░')



intro = "Welcome seeker.  I can tell that you have come in search of knowledge and wisdom; this is the right place for you.\n"
for character in intro:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.04)

alphabet = ['A','B','C','D','E', 'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def tarotReading():
	random.shuffle(deck)
	past = deck.pop()
	present = deck.pop()
	future = deck.pop()
	pastReverse = random.randint(1,2)
	presentReverse = random.randint(1,2)
	futureReverse = random.randint(1,2)
	pastReverseText =''
	presentReverseText = ''
	futureReverseText = ''
	if pastReverse == 2:
		pastReverseText = ' - reversed'
	if presentReverse == 2:
		presentReverseText = ' - reversed'
	if futureReverse == 2:
		futureReverseText = ' - reversed'

	pastText = 'The card representing your past is the '+ past+pastReverseText+'\n'
	for character in pastText:
	    sys.stdout.write(character)
	    sys.stdout.flush()
	    time.sleep(0.04)
	presentText = 'The card representing your present is the '+ present+presentReverseText+'\n'
	for character in presentText:
	    sys.stdout.write(character)
	    sys.stdout.flush()
	    time.sleep(0.04)
	futureText = 'The card representing your future is the '+ future+futureReverseText+'\n'
	for character in futureText:
	    sys.stdout.write(character)
	    sys.stdout.flush()
	    time.sleep(0.04)
	return

firstLetter = random.choice(alphabet)

nameletter = "Would it be correct to say that your name starts with a "+firstLetter+"?\n"
for character in nameletter:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.04)
realfirstletter = input("> ")
if realfirstletter.lower() in ['yes', 'yeah', 'y','sure', 'yup', 'yuppers', 'yas', 'si']:
 rightGuess = "I felt sure of it.\n"
 for character in rightGuess:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.04)
else:
	wrongGuess = "I knew it!  I woke up sure I wouldn't meet anybody today with a name like that.\n"
	for character in wrongGuess:
	    sys.stdout.write(character)
	    sys.stdout.flush()
	    time.sleep(0.04)

deck = ['The Fool', 'The Magician', 'The High Priestess', 'The Empress', 'The Emperor', 'The Hierophant', 'The Lovers', 'The Chariot','The Strength','The Hermit', 'The Wheel of Fortune', 'Justice', 'The Hanged Man', 'Death', 'Temperance', 'The Devil', 'The Tower', 'The Star', 'The Moon', 'The Sun', 'Judgment', 'The World','Ace of Wands', 'Two of Wands', 'Three of Wands', 'Four of Wands', 'Five of Wands', 'Six of Wands', 'Seven of Wands', 'Eights of Wands', 'Nine of Wands', 'Ten of Wands', 'Page of Wands', 'Queen of Wands', 'King of Wands', 'One of Cups', 'Two of Cups', 'Three of Cups', 'Four of Cups','Five of Cups','Six of Cups','Seven of Cups','Eight of Cups','Nine of Cups','Ten of Cups', 'Page of Cups', 'Queen of Cups','King of Cups','One of Swords', 'Two of Swords','Three of Swords', 'Four of Swords', 'Five of Swords','Six of Swords', 'Seven of Swords','Eight of Swords','Nine of Swords','Ten of Swords','Page of Swords', 'Queen of Swords','King of Swords','One of Pentacles','Two of Pentacles','Three of Pentacles','Four of Pentacles','Five of Pentacles', 'Six of Pentacles', 'Seven of Pentacles', 'Eight of Pentacles', 'Nine of Pentacles','Ten of Pentacles','Page of Pentacles','Queen of Pentacles','King of Pentacles']

#majorArcana = ['The Fool', 'The Magician', 'The High Priestess', 'The Empress', 'The Emperor', 'The Hierophant', 'The Lovers', 'The Chariot','The Strength','The Hermit', 'The Wheel of Fortune', 'Justice', 'The Hanged Man', 'Death', 'Temperance', 'The Devil', 'The Tower', 'The Star', 'The Moon', 'The Sun', 'Judgment', 'The World']
#minorArcana = ['Ace of Wands', 'Two of Wands', 'Three of Wands', 'Four of Wands', 'Five of Wands', 'Six of Wands', 'Seven of Wands', 'Eights of Wands', 'Nine of Wands', 'Ten of Wands', 'Page of Wands', 'Queen of Wands', 'King of Wands', 'One of Cups', 'Two of Cups', 'Three of Cups', 'Four of Cups','Five of Cups','Six of Cups','Seven of Cups','Eight of Cups','Nine of Cups','Ten of Cups', 'Page of Cups', 'Queen of Cups','King of Cups','One of Swords', 'Two of Swords','Three of Swords', 'Four of Swords', 'Five of Swords','Six of Swords', 'Seven of Swords','Eight of Swords','Nine of Swords','Ten of Swords','Page of Swords', 'Queen of Swords','King of Swords','One of Pentacles','Two of Pentacles','Three of Pentacles','Four of Pentacles','Five of Pentacles', 'Six of Pentacles', 'Seven of Pentacles', 'Eight of Pentacles', 'Nine of Pentacles','Ten of Pentacles','Page of Pentacles','Queen of Pentacles','King of Pentacles']
#deck = majorArcana + minorArcana

question1 = "What do you call yourself?\n"
for character in question1:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.04)
name = input('> ')

response = "Of course "+name+", I felt sure that today I would be visited by somebody whose name starts with a "+name[0]+" and the spirits are seldom wrong about such things.\n"

for character in response:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.04)


wantReading = "Would you be interested in a tarot reading?\n"
for character in wantReading:
	sys.stdout.write(character)
	sys.stdout.flush()
	time.sleep(0.04)
wantReadingAnswer = input('> ')
if wantReadingAnswer.lower() in ['yes', 'yeah', 'y','sure', 'yup', 'yuppers', 'yas', 'yea', 'okay', 'si']:
	readingBegin = "Let's begin\n"
	for character in readingBegin:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.04)
	tarotReading()
else:
	readingDeclined = "Maybe next time.  May the spirits bring you good fortune!\n"
	for character in readingDeclined:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.04)


endText = "Farewell.  Remember, if you refer a friend, you get 50%"+" off a future session!"
for character in endText:
	sys.stdout.write(character)
	sys.stdout.flush()
	time.sleep(0.04)