text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at,' \
       ' dignissim vitae libero'

new_text = text.split()
ing_text = ''
print(new_text)
for word in new_text:
    if word[-1] == ',':
        ing_text += word.replace(',', 'ing,')
    elif word[-1] == '.':
        ing_text += word.replace('.', 'ing.')
    else:
        ing_text += f"{word}ing "

print(ing_text)








