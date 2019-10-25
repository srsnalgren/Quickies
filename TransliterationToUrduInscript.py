import io
letters = { 'q':'ق', 'Q':'ْ', 'w':'و', 'W':'ّ', 'e':'ع', 'E':'ٰ', 'r':'ر', 'R':'ڑ', 't':'ت', 'T':'ٹ', 'y':'ے', 'Y':'َ', 'u':'ء', 'U':'ئ', 'i':'ی', 'I':'ِ', 'o':'ہ', 'O':'ۃ', 'p':'پ', 'P':'ُ', 'a':'ا', 'A':'آ', 's':'س', 'S':'ص', 'd':'د', 'D':'ڈ', 'f':'ف', 'g':'گ', 'G':'غ', 'h':'ح', 'H':'ھ', 'j':'ج', 'J':'ض', 'k':'ک', 'K':'خ', 'l':'ل', 'z':'ز', 'Z':'ذ', 'x':'ش', 'X':'ژ', 'c':'چ', 'C':'ث', 'v':'ط', 'V':'ظ', 'b':'ب', 'n':'ن', 'N':'ں', 'm':'م', 'M':'٘', '~':'ً', '0':'۰', '1':'۱', '2':'۲', '3':'۳', '4':'۴', '5':'۵', '6':'۶', '7':'۷', '8':'۸', '9':'۹', ',':'،', '.':'۔', '?':'؟', ';':'؛' }
transliterated = ''
rfile = input ('Enter filename: ')
with io.open (rfile, 'r', encoding = 'utf8') as f:
    text = f.read()
    transliterated = text

for key in letters.keys():
    transliterated = transliterated.replace(key, letters[key])

with io.open (rfile + '_URDU.txt', 'w', encoding = 'utf8') as f:
    f.write (transliterated)
