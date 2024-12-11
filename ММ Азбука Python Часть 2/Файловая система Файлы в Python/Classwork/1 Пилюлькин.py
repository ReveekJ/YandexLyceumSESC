
name = input()
dose = input()

with open('recipe.txt', 'w') as file:
    file.write(f'''Рецепт
Выписан {name}
Прописано: по {dose} касторки 3 раза в день.
Подпись: доктор Пилюлькин.''')
