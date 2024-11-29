# После недавнего сбоя в операционной системе от компании «Oursoft» у Гвидо сбилась кодировка на компьютере.
# Теперь все буквы русского алфавита отображаются в некорректном виде:
# [u-<номер символа в таблице Unicode>]
# Гвидо еще не научился читать символы в таком формате, поэтому просит вас написать программу,
# которая будет "расшифровывать" для него все тексты на компьютере.
# На вход программе подается строка текста. Расшифруйте текст, заменив все конструкции
# [u-<номер символа в таблице Unicode>] на соответствующие буквы русского алфавита, и выведите его.
# Формат входных данных
# На вход программе подается строка текста, в которой могут быть зашифрованы символы русского алфавита.
# Формат выходных данных
# Программа должна вывести строку текста, расшифровав символы русского алфавита.
# Примечание. Будем считать, что буквы Ё нет в русском алфавите. 🤫


text = input()
for i in range(64):
    unicode = ord("А") + i
    if str(unicode) in text:
        text = text.replace(f'[u-{unicode}]', chr(unicode))
print(text)