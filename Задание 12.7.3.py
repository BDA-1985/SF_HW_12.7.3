money = int(input("Введите сумму депозита: "))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
value_list = list(per_cent.values())
new_list = [i * money for i in value_list]
deposite_list = [int(i) for i in new_list]
print(f'deposit = {deposite_list}')
print(f'Максимальная сумма, которую вы можете заработать — {max(deposite_list)}')
