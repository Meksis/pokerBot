x = {'♣' : ['6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'], 
'♠' :['6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'],
'♥' : ['6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'],
'♦' : ['6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']}


for i in x:
	print(f'{i} - {x[i]}')

x['♥'] = ['ABOBA']
print('\n\n')

for i in x:
	print(f'{i} - {x[i]}')

# ['♠__Jack', '♦__Jack', '♣__King', '♣__Jack', '♦__Ace', '♥__Ace'], ['♥__Jack', '♠__King', '♠__Ace', '♣__Queen', '♣__Ace', '♦__King']

test_lst = ['♠__Jack', '♦__Jack', '♣__King', '♣__Jack', '♦__Ace', '♥__Ace']
counter = {}

for element in test_lst:
	if element not in counter:
		counter.update({element : test_lst.count(element)})

print(counter)