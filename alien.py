'''
Created on Dec 14, 2023

@author: apurs
'''
alien_O = {'color':'green', 'points':5}

print(alien_O['color'])
print(alien_O['points'])


new_points = alien_O['points']
print(f"You just earned {new_points} points!")
print(f"You just earned {alien_O['points']} points!")

alien_O['x_position'] = 0
alien_O['y_position'] = 25

print(alien_O)

alien_1 ={}
alien_1['color'] = 'green'
alien_1['points'] = 5

print(alien_1)
print('///////////////////////////////////\n')

print(f"The alien is {alien_1['color']}.")
alien_1['color'] = 'yellow'
print(f"The alien is {alien_1['color']}.")
print('///////////////////////////////////\n')

alien_2 = {'x_position':0, 'y_position':25, 'speed':'medium'}

#Move the alien the the right
#Determine how far to move the alien based on its current speed

print(f"Original position: {alien_2['x_position']}")

if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

#The new position is the old position plus the increment.
alien_2['x_position'] = alien_2['x_position'] + x_increment

print(f"New position: {alien_2['x_position']}")
print('///////////////////////////////////\n')

alien_3 = {'color':'green', 'points':5}
print(alien_3)

del alien_3['points']

print(alien_3)

