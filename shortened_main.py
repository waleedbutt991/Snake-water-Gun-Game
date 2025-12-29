import random

computer = random.choice([1,-1,0])
youstr= (input('Enter Choice: '))
you_dict={'G': 1, 'S': -1, 'W': 0}
reverse_dict={1:'Gun', -1: 'Snake', 0 : 'Water'}

you = you_dict[youstr]

print(f'Computer choose {reverse_dict[computer]}\nYou Choose {reverse_dict[you]}' )

if (computer == you):
    print('Draw')
elif ((computer - you) == 2) or ((computer - you) == -1):
    print ('You Lost')
else:
    print('You win')

# elif (computer == 1 and you == -1): 2
#         print('you lost')

# elif (computer == 1 and you == 0): 1
#         print('you win')

# elif (computer == -1 and you == 1): -2
#         print('you win')

# elif (computer == -1 and you == 0): -1
#         print('you lost')

# elif (computer == 0 and you == 1): -1
#        print('You lost')

# elif (computer == 0 and you == -1): 1
#        print ('you win')

