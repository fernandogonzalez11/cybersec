#!/bin/bash

# run in temp dir
KRP=/krypton/krypton6/
TMP=$(pwd)

plain="plain"
cipher="cipher"
amt=512

$(cat > mkplain.py <<EOF
from string import ascii_uppercase
print(''.join([(c * 30) for c in ascii_uppercase]), end='')
EOF
)

cd $TMP
python3 mkplain.py > $plain
touch $cipher

chmod 444 $plain
chmod 666 $cipher
chmod 777 .

echo "trying $amt 01010101 bytes..."

cd $KRP
./encrypt6 $TMP/$plain $TMP/$cipher

cd $TMP
xxd $cipher
cat $cipher | fold -w 30
