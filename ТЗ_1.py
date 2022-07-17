sourceTXT = input("Введите исходную строку: ");
print("Исходная строка - ", sourceTXT);
text = sourceTXT.lower();
res='';
for i in range (len(text)):
    if text.count(text[i]) >= 2:
        res += ')';
    else:
        res += '(';
print("Результат: ",res);
