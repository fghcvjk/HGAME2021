import random
import string
import itertools
from secret import FLAG

key = ''.join(random.choices(string.ascii_letters + string.digits, k=16))

cipher = bytes([ord(m)^ord(k) for m, k in zip(FLAG, itertools.cycle(key))])

print(cipher)

#cipher=b'S\x19((82-A;N\x0c]e)\x1a9y#"e"?<]b\x1a\rVe-\x04(4/?1&w6Ubd\x04\x135)\x01#-#?"u8+\x13&\x1c\x04D,&\x0fm;+=$;4<\x13\'\x0f\x06[e\'\x1c%<8qO:"-\x1db:\rZ6h\x0b",&5e72yG*\x0bE\\\'"\r.-9q1=24@\'\x02\x13V6dHG;?%e<#yP#\x00ER);\x07m+/=$!2yG-N\x06\\)\'\x1a>y+?!u]6G*\x0b\x17\x13&\'\x05=6981<87R.N\x11V& \x06$(?46{]\x00\\7N\x08R<h\x06"-j# 4;0I\'N\x0cGih\n8-j(* %yQ0\x0f\x0c]eB\x01>y($6,w.\\0\x05\x0c]"h\n(1#?!u#1Vb\x1d\x06V+-\x1bm-%q6022\x13H\x01\x10Ge;\x11 4/%7,w.[\'\x00EJ*=H!6%:e4#yRb\x1e\x04Z+<\x01#>dqO\x01?<A\'N\x04A h\x1b(//#$9w+V#\x1d\n]6h\x0e"+j%-<$w\x13\x16\x06\x00\x13O.\x01?*>q,&w-[#\x1aED o\x1a(y"071z.Z0\x0b\x01\x131\'H!6%:e38+\x13H\x07\x11\x1de\x07\x1d?y+?&<27Gb\x0f\x0bP ;\x1c"+9q(4.y]-\x1aE[$>\rm1+5e_6y]#\x03\x00\x13#\'\x1am0>}e7"-\x136\x06\x00Je#\x06(.j%-4#yG*\x0b\x0cAeB\x07:7j3*1><@b\x19\x00A h\n,*#2$9; \x131\x17\x08^ <\x1a$:+=iu6*\x13H\x19\x00A h\x1c%694e:1yC-\x1a\x00]1!\t!y:# 16-\\0\x1dE\\7h\x18?<3\x7fe_\x031V0\x0b\x03\\7-Dm-"86u48^\'N\x0c]e \t#=3q2=2-[\'\x1cE9& \x07"*#?"u6y^#\x1a\x00\x1fe+\t9:"8+2w=Z,\x00\x00Ae\'\x1amS+\'*<30]%N\x07V,&\x0fm6$q1=2y^\'\x00\x10\x13*.H,y9?$\';0]%BE9-=\x06*+3q5442\x13-\x08ED*$\x1e(*j>7u5<R0\x1dD9\x11)\x03(y+q):82\x13#\x1aEJ*=\x1am?+2 u>7\x136\x06\x00\x13(!\x1a?68qO49=\x13+\x03\x04T,&\rm8j=,;2y@6\x1c\x04Z" \x1cm=%&+u#1Vbd\x08Z!,\x04(wj\x08* p5_b\x1d\x00Ve*\x0791j",12*\x13-\x08EJ*=\x1amS,0&0w8A\'N\x15A <\x1c4y9((82-A+\r\x04_kh<%09q,&wSX,\x01\x12]e)\x1bm;#=$!2+R.N\x16J(%\r9+3q$;3yZ6I\x16\x13O?\x00(+/q\':#1\x131\x07\x01V6h\r$-"47u$0W\'N\nUe<\x00$*j[!<!0W+\x00\x02\x13)!\x06(y+!506+\x13/\x01\x17Ve\'\x1am5/"6u#1Vb\x1d\x04^ fb\x1e6j9 \'2yZ1N\x11[ h\x0e!8-ke_?>R/\x0b\x1eku:7$lg0\x1a \x04jU\x17_N\x07+,L+\x0c\x04?<\n\x14hC\n]\x17NO'
