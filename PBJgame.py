
#pbj txt based game

#start of the game
def start ():
    print ''' Welcome to PBJ Starvation Satisfaction Simulator 2016!
by Nina V'''
    print
    prompt_sta()

def prompt_sta ():
    prompt_0 = raw_input ('Type "commence the journey to begin": ')
    try:
        if prompt_0 == 'commence the journey':
            kitchen()
            prompt_sta()
        elif prompt_0 == 'start':
            kitchen()
        elif prompt_0 == 'commence':
            kitchen()
        else:
            print 'Sorry I dont speak Itanlian'
            print
            prompt_sta()
    except ValueError:
        print 'No! Type what I told you to like a good civilian'
        print
        prompt_sta()

#beginning part (in the kitchen)

#bread phase
def kitchen ():
    print '''Ok! So your just minding your own buisness and BOOM!
It hits you... Your hungry
As you look around the kitchen you realize you have nothing in the fridge
Except for: Bread, Peanut Butter, and Jelly
What do you do? Type in the steps to making a pbj'''
    print
    prompt_kitchen()

def prompt_kitchen ():
    prompt_1 = raw_input ('How many slices of bread should you bring out?: ')
    try:
        if prompt_1 == 'two' or '2': #closed sandwich
            closedS()
        elif prompt_1 == '1' or 'one': #open face sandwich
            openS()
        else:
            print 'What? How many bread slices of bread are you gonna bring out?'
            print
            prompt_kitchen()
    except ValueError:
        print 'What are you talking about? Try again and this time try to make sense'
        print
        prompt_kitchen() 

#closed sandwich route

#peanut or jelly phase
def closedS ():
    print '''So now you have your two slices of bread
Now whats next? "peanutbutter" or "jelly"?'''
    print
    prompt_closedS()
    
def prompt_closedS ():
    prompt_2 = raw_input ('Whats first? "peanutbutter" or "jelly"?: ')
    try:
        if prompt_2 == 'jelly':
            closed_j()
        elif prompt_2 == 'peanutbutter':
            closed_p()
        else:
            print 'I dont understand. "peanutbutter" or "jelly"?'
            print
            prompt_closedS()
    except ValueError:
        print 'Its a simple question. Whats first? "peanutbutter" or "jelly"?'
        print
        prompt_closedS()

#peanut butter choice for closed sandwich
def closed_p ():
    print '''You take the peanutbutter out of the cabinet and begin to spread it across the slices of bread
Will you continue to "add jelly" or "finish the sandwich" as is?'''
    print
    prompt_peanc

def prompt_peanc ():
    prompt_3 = raw_input ('What will you choose?: ')
    try:
        if prompt_3 == 'add jelly':
            jaclosed()
        elif prompt_3 == 'finish the sandwich':
            eatclosedP()
        else:
            print 'Do you wanna "add jelly" or "finish the sandwich"?'
            print
            prompt_peanc()
    except ValueError:
        print 'Do you wanna "add jelly" or "finish the sandwich"?'
        print
        prompt_peanc()

#jelly choice for closed sandwich
def closed_j():
    print '''You take the jelly and begin to spread it across the slices of bread
Will you "add peanutbutter" or "finish the sandwich" as is'''
    print
    prompt_jellc()

def prompt_jellc():
    prompt_4 = raw_input ('What will you choose?: ')
    try:
        if prompt_4 == 'add peanutbutter':
            paddclosed()
        elif prompt_4 == 'finish the sandwich':
            eatclosedJ()
        else:
            print 'Do you wanna "add peanutbutter" or "finish the sandwich"?'
            print
            prompt_jellc()
    except ValueError:
        print 'Do you wanna "add peanutbutter" or "finish the sandwich"?'
        print
        prompt_jellc()

#jellyAddclosed and peanutAddclosed end

#for jelly end
def eatclosedJ():
    print'''You eat the closed face sandwich without any peanutbutter
You feel satisfide!
Thanks for playing! :D'''
    print
    prompt_ecj()

def prompt_ecj():
    prompt_a = raw_input('Type "start over" or "play again" to play again: ')
    try:
        if prompt_a == 'start over':
            start()
        elif prompt_a == 'play again':
            start()
        else:
            print'Type "start over" or "play again" to play again'
            print
            prompt_ecj()
    except ValueError:
        print 'Type "start over" or "play again" to play again'
        print
        prompt_ecj()

#peanutAddclosed
def paddclosed():
    print '''You spread peanutbutter on to a slice of bread and smash it together with the side that has jelly on it
You eat the whole thing and feel very satisfide!
Thanks for playing! :D'''
    print
    prompt_pac()

def prompt_pac():
    prompt_5 = raw_input('Do you want to "play again"?: ')
    try:
        if prompt_5 == 'play again':
            start()
        elif prompt_5 == 'start over':
            start()
        else:
            print 'Thats it you finished the game... You can type "start over" if you want.'
            print
            prompt_pac()
    except ValueError:
        print 'You can type "start over" or "play again" to make a pbj one more time'
        print
        prompt_pac()
        
#jellyAddclosed
def jaclosed():
    print '''You spread the jelly on to a slice of bread and smash it together with the side that had peanutbutter on it
You eat the whole thing and feel satisfide!
Thanks for playing! :D '''
    print
    prompt_jac()

def prompt_jac():
    prompt_6 = raw_input('Do you want to "play again"?: ')
    try:
        if prompt_6 == 'play again':
            start()
        elif prompt_6 == 'start over':
            start()
        else:
            print 'Thats it you finished the game... You can type "start over" or "play again" if you want.'
            print
            prompt_jac()
    except ValueError:
        print 'Thats it you finished the game... You can type "start over" or "play again" if you want.'
        print
        prompt_jac()

#open faced sandwich route

#open faced sandwich (result of prompt_1)
def openS():
    print '''You take one slice of bread out of the fridge
I guess this is gonna be an open faced sandwich
What do you want to put on it first? "peanutbutter" or "jelly"?'''
    print
    prompt_opns()

def prompt_opns():
    prompt_7 = raw_input('What will you choose?: ')
    try:
        if prompt_7 == 'peanutbutter':
            opnsP()
        elif prompt_7 == 'jelly':
            opnsJ()
        else:
            print 'What? Do you wanna add "peanutbutter or "jelly"?'
            print
            prompt_opns()
    except ValueError:
        print 'What? Do you wanna add "peanutbutter or "jelly"?'
        print
        prompt_opns()

#open faced sandwich choices (result of prompt_7)

#open faced sandwich jelly choice
def opnsJ():
    print'''You take the jelly out of the cabinet
and begin to spread it across the slice of bread
Do you want to "add peanutbutter" or "finish the sandwich" as is'''
    print
    prompt_opnj()

def prompt_opnj():
    prompt_8 = raw_input('What will you choose?: ')
    try:
        if prompt_8 == 'add peanutbutter':
            addopnP()
        elif prompt_8 == 'finish the sandwich':
            eatopnJ()
        else:
            print'Do you want to "add peanutbutter" or "finish the sandwich"'
            print
            prompt_opnj()
    except ValueError:
        print 'Mmmm no. Try again'
        print
        prompt_opnj()

#open faced sandwich peanutbutter choice
def opnsP():
    print'''You take the peanutbutter out of the cabinet
and begin to spread it across the slice of bread
Do you want to "add jelly" or "finish the sandwich" as is'''
    print
    prompt_opnp()

def prompt_opnp():
    prompt_9 = raw_input == ('What will you choose?: ')
    try:
        if prompt_9 == 'add jelly':
            addopnJ()
        elif prompt_9 == 'finish the sandwich':
            eatopnP()
        else:
            print'Do you want to "add jelly" or "finish the sandwich"'
            print
            prompt_opnp()
    except ValueError:
        print'Do you want to "add jelly" or "finish the sandwich"'
        print
        prompt_opnp()

#endings

#open faced sandwich eat/end for jelly w/ peanutbutter and w/o peanutbutter
#open faced sandwich w/ peanutbutter
def addopnP():
    print'''You spread the peanutbutter on top of the jelly
and eat the whole open faced sandwich
You feel satisfide!
Thanks for playing! :D'''
    print
    prompt_aop()

def prompt_aop():
    prompt_c = raw_input('Type "start over" or "play again" to play again')
    try:
        if prompt_c == 'start over':
            start()
        elif prompt_c == 'play again':
            start()
        else:
            print 'Type "start over" or "play again" to play again'
            print
            prompt_aop()
    except ValueError:
        print 'Type "start over" or "play again" to play again'
        print
        prompt_aop()

#open faced sandwich w/o peanutbutter
def eatopnJ():
    print'''You eat the open faced sandwich without any peanutbutter
You feel satisfide!
Thanks for playing! :D'''
    print
    prompt_eoj()

def prompt_eoj():
    prompt_d = raw_input('Type "start over" or "play again" to play again')
    try:
        if prompt_d == 'start':
            start()
        elif prompt_d == 'play again':
            start()
        else:
            print'Type "start over" or "play again" to play again'
            print
            prompt_eoj()
    except ValueError:
        print'Type "start over" or "play again" to play again'
        print
        prompt_eoj()

#open faced sandwich eat/end for peanutbutter w/ jelly and w/o jelly
#w/ jelly
def addopnJ():
    print'''You spread the jelly on top of the peanutbutter
and begin to eat the whole open faced sandwich
You feel satisfide!
Thanks for playing!'''
    print
    prompt_adopj()

def prompt_adopj():
    prompt_10 = raw_input = ('Type "start over" or "play again" to play again: ')
    try:
        if prompt_10 == 'start over':
            star()
        elif prompt_10 == 'play again':
            start()
        else:
            print'Type "start over" or "play again" to play again'
            print
            prompt_adopj()
    except ValueError:
        print'Type "start over" or "play again" to play again'
        print
        prompt_adopj()

#w/o jelly
def eatopnP():
    print '''You eat the open faced sandwich without any jelly
You feel satisfide!
Thanks for playing! :D'''
    print
    prompt_eop()

def prompt_eop():
    prompt_b = raw_input('Type "start over" or "play again" to play again: ')
    try:
        if prompt_b == 'start over':
            start()
        elif prompt_b == 'play again':
            start()
        else:
            print'Type "start over" or "play again" to play again'
            print
            prompt_eop()
    except ValueError:
        print'Type "start over" or "play again" to play again'
        print
        prompt_eop()

#
start ()
