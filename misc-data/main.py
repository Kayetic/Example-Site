def convert(number):
    result = ''
    if number % 3 == 0 and number % 5 == 0 and number % 7 == 0:
        result += 'PlingPlangPlong'
    elif number % 5 == 0 and number % 7 == 0:
        result += 'PlangPlong'
    elif number % 3 == 0 and number % 7 == 0:
        result += 'PlingPlong'
    elif number % 3 == 0 and number % 5 == 0:
        result += 'PlingPlang'
    elif number % 7 == 0:
        result += 'Plong'
    elif number % 5 == 0:
        result += 'Plang'
    elif number % 3 == 0:
        result += 'Pling'
    else:
        result = str(number)
    return result