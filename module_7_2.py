
def custom_write(fname,str_):
    out_stream = open(fname,'w',encoding = 'utf-8')
    i = 1
    dict_ = {}
    for _str_ in str_:
        dict_[i,out_stream.tell()] = _str_
        out_stream.write(_str_ + '\n')
        i += 1
    out_stream.close()
    return dict_

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
