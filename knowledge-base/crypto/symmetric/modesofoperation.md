modes of operation
===

![](modesofoperation_20260206160250299.png)

ecb:

![](modesofoperation_20260206161414217.png)

cbc:

![](modesofoperation_20260206161543984.png)

ofb:

![](modesofoperation_20260206161739517.png)

ctr:

![](modesofoperation_20260206161931394.png)

https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#/media/File:BlockCipherModesofOperation.svg

ECB oracle can be used to gather the key

```
guess abcdef:

000000000000000?: guessing area
000000000000000a: flag char
bcdef01020304050: flag+padding
```

if i can encrypt with CBC but decrypt with ECB:

![](modesofoperation_20260206162218700.png)