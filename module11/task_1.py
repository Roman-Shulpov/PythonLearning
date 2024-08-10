bet = int(input('сколько ставим? : '))
coefficient = float(input('Какой коэффициент? : '))

win = round(bet * coefficient, 2)

print('Потенциальный выйгрыш: ', win)
