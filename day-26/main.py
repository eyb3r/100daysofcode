import pandas

codes = pandas.read_csv('nato_phonetic_alphabet.csv')
#Loop through rows of a data frame

phonetics = {row.letter: row.code for (_, row) in codes.iterrows()}
while True:
    try:
        result = [phonetics[letter.upper()] for letter in input('Enter a word: ')]
    except KeyError:
        print("Only letters please")
    else:
        print(result)
        break
