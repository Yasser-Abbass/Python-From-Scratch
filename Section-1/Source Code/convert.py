def get_parts(num):
    if len(str(num)) > 2:
        hun = num // 100
        tens = num % 100
        if tens < 20:
            units = tens
            tens = 0
        else:
            units = num % 100 % 10
            tens = num % 100 - units
    else:
        hun = 0
        if num < 20:
            tens = 0
            units = num
        else:
            tens = num // 10
            units = num % 10

    return hun, tens, units


numbers = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousands',
    1000000: 'million'
}
num = int(input('Please enter a number: '))
#num = 354564321

mil_part = num // 1000000
ths_part = num % 1000000 // 1000
hun_part = num % 1000000 % 1000


text = ""
hun, tens, units = get_parts(mil_part)
if hun:
    text += numbers[hun] + " " + numbers[100] + " "
if tens:
    text += numbers[tens] + " "
if units:
    text += numbers[units] + " "
if mil_part:
    text += 'Millions, '
hun, tens, units = get_parts(ths_part)
if hun:
    text += numbers[hun] + " " + numbers[100] + " "
if tens:
    text += numbers[tens] + " "
if units:
    text += numbers[units] + " "
if mil_part:
    text += 'Thousands, '
hun, tens, units = get_parts(hun_part)
if hun:
    text += numbers[hun] + " " + numbers[100] + " "
if tens:
    text += numbers[tens] + " "
if units:
    text += numbers[units] + " "

print(text)

