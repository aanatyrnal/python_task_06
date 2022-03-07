# 2 *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным
# файла логов из предыдущего задания.
# Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с
# файлами, размер которых превышает объем ОЗУ компьютера.

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    res_list = []
    spam_dict = {}
    for line in f:
        ln = line.split()
        res_list.append((ln[0], ln[5].replace('"', ''), ln[6]))
        spam_dict.setdefault(ln[0], 0)
        spam_dict[ln[0]] += 1

spam_dict = sorted(spam_dict.items(), key=lambda x: x[1], reverse=True)
print(spam_dict[0])
