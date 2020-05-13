'''
Please write a program to generate 
all sentences where subject is in ["I", "You"] 
and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
'''

def Ex79():
    subject_list = ["I", "You"]
    verb_list = ["Play", "Love"]
    object_list = ["Hockey","Football"]

    for subject in subject_list:
        for verb in verb_list:
            for Object in object_list:
                print(subject, verb, Object)

if __name__ == "__main__":
    Ex79()
