def corrector(string, wigth, symbol):
    string = {string}
    wigth = {wigth}
    symbol = {symbol}
    string = input('Введите предложение: ')
    wigth = input('Введите кол-во символов: ')
    symbol = input('Введите символ: ')
    print(f'{string:symbol^wigth}')
corrector('string', 'wigth', 'symbol')
