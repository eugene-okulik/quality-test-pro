with open('av.txt') as file:
    data = file.read()

lines = data.splitlines()
print(lines)

features = {}
new_category = True
current_categ = None
for line in lines:
    if not line:
        new_category = True
        current_categ = None
        continue
    if new_category:
        features[line] = []
        current_categ = line
        new_category = False
    elif line:
        features[current_categ].append(line)

print(features['Фары'])
