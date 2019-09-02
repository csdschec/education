# Exercise 1
x = "HEC Montréal est un établissement universitaire québécois situé à Montréal (Canada)."
print('Exercise 1 a)', x)
x = x.replace('(', '').replace(')', '').replace('.', '')
print('Exercise 1 b)', x)
x = x.lower()
print('Exercise 1 c)', x)
x_list = x.split()
print('Exercise 1 d)', x_list)

# Exercise 2
x_list.pop(-1)
print('Exercise 2 a)', x_list)
x_list.append('québec')
print('Exercise 2 b)', x_list)
x_sub_list = x_list[0:6]
print('Exercise 2 c)', x_sub_list)

# Exercise 3
x_uplet = (x_sub_list[0], x_sub_list[1])
print('Exercise 3 a)', x_uplet)

# Exercise 4
x_dict = {'ecole' : x_uplet[0], 'ville' : x_uplet[1]}
print('Exercise 4 a)', x_dict)
x_dict['ecole'] = 'polytechnique'
print('Exercise 4 b)', x_dict)

# Exercise 5
import numpy as np
A = np.arange(4).reshape(2, 2)
print('Exercise 5 a)\n', A)
A = A + 1
print('Exercise 5 b)\n', A)
A[0, 0] = 0
print('Exercise 5 c)\n', A)

# Exercise 6
import pandas as pd
df = pd.DataFrame(
        {'produit' : ['croustilles', 'biscuit'],
        'prix' : [2, 1.50],
        'ventes' : [1000, 1750]
        })
print('Exercise 6 a)\n', df)
df.loc[2, :] = 'salade', 5, 500
print('Exercise 6 b)\n', df)
df['profit'] = df['prix'] * df['ventes']
print('Exercise 6 c)\n', df)
resultat = df[['prix', 'ventes', 'profit']].median()
print('Exercise 6 d)\n', resultat)

# Exercise 7
données = np.loadtxt('data/matrice.txt')
np.savetxt(fname = 'data/matrice_2.txt', X = données)
print('Exercise 7 a)\n', 'Les données ont été enregistrées en chiffres décimaux plutôt qu\'entiers!')

# Exercise 8
bost_df = pd.read_excel('data/boston_crime_august_2018.xlsx', index_col = 'INCIDENT_NUMBER')
print('Exercise 8 a)\n', bost_df.head())

############################
### FIN DU PREMIER COURS ###
############################

# Exercise 1
def longueur(chaine):
    x = len(chaine)
    if x >= 5:
        print('La chaîne comporte 5 lettres ou plus.')
    elif x == 0:
        print('La chaîne est vide.')
    else:
        print('La chaîne comporte moins de 5 lettres.')

print('Exercise 1 b)')
longueur('chat')
print('Exercise 1 c)')
longueur('')
print('Exercise 1 d)')
longueur('Stella')

# Exercise 2
y = (1, 2, 3)
def essaie(function):
    try:
        if function == 1:
            print(y[3])
        elif function ==2:
            y[2] = 0
    except IndexError as e:
        print(e)
    except TypeError as e:
        print(e)

print('Exercise 2 b)')
essaie(1)
print('Exercise 2 c)')
essaie(2)

# Exercise 3
print('Exercise 3 a)')
chaine = 'Stella'
for lettre in chaine:
    print(lettre)

print('Exercise 3 b)')
for élément in ma_liste[0]:
    print(élément)

# Exercise 4
print('Exercise 4 a)')
chaine = 'miaou'
while len(chaine) < 8:
    chaine = chaine + 'u'
    print (chaine)
