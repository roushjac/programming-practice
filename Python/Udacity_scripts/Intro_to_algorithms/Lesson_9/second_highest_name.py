# read file
text = open(r'C:\Users\roush\OneDrive\Documents\Python\Udacity_scripts\Intro_to_algorithms\Lesson_9\yob1995.txt', 'r')
text = text.read().split('\n')
# split each list element into 3 elements
text_split = [x.split(',') for x in text]

def find_second_female(text):
    female_list = [['dummy','F','0'], ['dummy','F','0']]
    for one_person in text:
        if len(one_person) == 3 and one_person[1] == 'F' and int(one_person[2]) > int(female_list[0][2]):
            # if find a female that's older, push it to front of list
            female_list.insert(0, one_person)
            female_list.pop() # get rid of previous second-highest female
    return female_list[1][0]

print(find_second_female(text_split))
