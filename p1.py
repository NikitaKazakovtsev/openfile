import os
import __main__
cook_book = {}
with open('k.txt', 'rt', encoding='utf8') as f:
    for l in f:
        r1 = l.strip()
        rec1 = []
        r2 = f.readline()
        for i in range(int(r2)):
            e = f.readline()
            ingredient_name, quantity, measure = e.strip().split(' | ')
            rec1.append({"ingredient_name": ingredient_name, "quantity": quantity, "measure": measure})
        blank_line = f.readline()
        cook_book.update({r1:rec1})

#print(cook_book)

cook_book1 = {}
def get_shop_list_by_dishes(dishes, person_count):
    for i, p in cook_book.items():
        for s in dishes:
            if i == s:
                for p1 in p:
                    p2 = int(p1['quantity'])
                    p2 *= person_count
                    cook_book1.update({p1['ingredient_name']:{'measure':p1['measure'],'quantity':p2}})
get_shop_list_by_dishes(['Омлет','Запеченный картофель'], 4)
#print(cook_book1)


def n1(*f123):
    all_text = {}
    for file in f123:
        with open(file, 'rt', encoding='utf-8') as f:
            y = f.readlines()
            all_text[file] = y
    all_text1 = {k: all_text[k] for k in sorted(all_text,key=all_text.get, reverse=True)}
    for key1, value in all_text1.items():
        with open('file.txt', 'a', encoding='utf-8') as f123:
            r = len(value)
            f123.writelines(key1)
            f123.writelines(f'\n{r}\n')
            f123.writelines(value)
            f123.writelines('\n')
n1("p1\\1.txt",'p1\\2.txt',"p1\\3.txt")
