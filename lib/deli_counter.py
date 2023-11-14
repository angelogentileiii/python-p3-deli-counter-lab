katz_deli = []

def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.")
    else:
        sentence = "The line is currently:"
        for i in range(len(katz_deli)):
            sentence += f' {i+1}. {katz_deli[i]}'
        print(sentence)

def take_a_number(katz_deli, person_name):
    katz_deli.append(person_name)
    print(f"Welcome, {person_name}. You are number {len(katz_deli)} in line.")
    pass

def now_serving(katz_deli):
    if len(katz_deli) > 0:
        print(f"Currently serving {katz_deli[0]}.")
        katz_deli.pop(0)
    else:
        print("There is nobody waiting to be served!")
    pass