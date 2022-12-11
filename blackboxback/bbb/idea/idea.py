import random
def get_idea():
    try:
        with open('texts_generated.txt', 'r') as f:
            text = []
            lines = f.readlines()
            for line in lines:
                text.append(line.strip())

        with open('cost_predicted.txt', 'r') as f:
            cost = []
            lines = f.readlines()
            for line in lines:
                cost.append(line.strip())

        with open('emp_predicted.txt', 'r') as f:
            emp = []
            lines = f.readlines()
            for line in lines:
                emp.append(line.strip())

        a = random.randint(0, 206)
        b = [text[a], cost[a], emp[a]]

        return b
    except:
        return '[eq'

print(get_idea())


