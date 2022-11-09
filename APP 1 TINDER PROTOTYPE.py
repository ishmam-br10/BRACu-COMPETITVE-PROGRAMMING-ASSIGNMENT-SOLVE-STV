# APP 1A: TINDER PROTOTYPE
# DIFFICULTY : WALK IN THE PARK
dictionary = {}
for i in range(1,3):
    dictionary1 = {}
    print(f'Person {i} Details')
    dictionary[f'person {i}'] = dictionary1
    dictionary1['age'] = int(input("Age: "))
    dictionary1['state'] = input('State: ').strip().lower()
    dictionary1['music genre'] = input('Music Genre: ').strip().lower()
    dictionary1['hobby'] = input('Hobby: ').strip().lower()
    dictionary1['jobholder'] = input("Jobholder: ").strip().lower()
    dictionary1['food habit'] = input('Food Habit: ').strip().lower()
    dictionary1['language'] = input('First Language: ').strip().lower()
person1 = dictionary['person 1']
person2 = dictionary['person 2']
point = 0
if person1['age'] < 18 or person2['age'] < 18:
    point = 0
else:
    if abs(person1['age']-person2['age'])<=5:
        point = point + 1

    if person1['state'] == person2['state']:
        point = point + 1
    if person1['music genre'] == person2['music genre']:
        point = point + 2
    if person1['hobby'] == person2['hobby']:
        point = point + 1
    if person1['jobholder'] == 'yes' or person2['holder'] == 'yes':
        if person1['jobholder'] == 'yes' and person2['jobholder'] == 'yes':
            point = point + 2
        elif person1['jobholder'] == 'yes' or person2['jobholder'] == 'yes':
            point = point + 1
    if person1['jobholder'] == 'no' and person2['jobholder'] == 'no':
        point = point - 1
    if person1['food habit'] == person2['food habit']:
        point = point +2
    if person1['language'] == person2['language']:
        point = point + 1

if point >= 5:
    print('Swipe right')
else:
    print('Swipe left')