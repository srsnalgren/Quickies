import io
letters = { 'ق':'q', 'و':'w', 'ع':"'", 'ر':'r', 'ڑ':'R', 'ت':'t', 'ٹ':'T', 'ے':'e', 'ء':"'", 'ئ':"'", 'ی':'y', 'ي':'y', 'ہ':'h', 'ۃ':'at', 'پ':'p', 'ا':'a', 'آ':'A', 'س':'s', 'ص':'S', 'د':'d', 'ڈ':'D', 'ف':'f', 'گ':'g', 'غ':'G', 'ح':'H', 'ھ':'h', 'ج':'j', 'ض':'Z', 'ک':'k', 'خ':'KH', 'ل':'l', 'ز':'z', 'ذ':'Z', 'ش':'sh', 'ژ':'zh', 'چ':'ch', 'ث':'S', 'ط':'t', 'ظ':'Z', 'ب':'b', 'ن':'n', 'ں':'n~', 'م':'m', '،':',', '۔':'.', '؟':'?', '؛':';', '۰':'0', '۱':'1', '۲':'2', '۳':'3', '۴':'4', '۵':'5', '۶':'6', '۷':'7', '۸':'8', '۹':'9'}
transliterated = ''
rfile = input ('Enter filename: ')
with io.open (rfile, 'r', encoding = 'utf8') as f:
    text = f.read()
    transliterated = text

for key in letters.keys():
    transliterated = transliterated.replace(key, letters[key])

with io.open (rfile + '_TRANSLITERATED.txt', 'w', encoding = 'utf8') as f:
    f.write (transliterated)
