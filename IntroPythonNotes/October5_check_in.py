""" Let's make a check_in_bot for mental health week """


def check_in_bot():
    #no arguments, it just runs the function itself.
    x = str(input('How are you feeling today?[g]ood/[b]ad'))
    # magic happens with if statements
    if x == 'g':
        print('Darn, thats really sick!')
    elif x == 'b':
        print('Darn, thats no good!')
    else:
        print('Darn, that didnt work, check your thumbs and try again')
        check_in_bot()
        # you can call a function inside of its own self!

            
