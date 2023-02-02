CONV_TABLE = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))

def arab_to_roman( number ):
  if number <= 0: return ''

  ret = ''
  for arab, roman in CONV_TABLE:
    while number >= arab:
          ret += roman
          number -= arab

  return ret

def roman_to_arab( txt ):
    txt = txt.upper()
    ret = 0
    for arab, roman in CONV_TABLE:
        while txt.startswith( roman ):
            ret += arab
            txt = txt[ len( roman ): ]
    return ret


for i in ( 0, 4, 8, 9, 31, 46, 99, 583, 888, 1668, 1989, 2009, 2010, 2011, 3999 ):
    arab = arab_to_roman( i )
    roman = roman_to_arab( arab )
    print i, arab, roman