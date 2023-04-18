# Catapult Plugins Collection

Plugin collection to integrate with catapult launcher

# Plugins available

## Translator

### Usage

Just write the word tr, then the base language and the
language to translate, finally just add what you want translate.

Remember that for the translation to be executed you must add a trailing whitespace.

Format: tr <source language> <target language> <Text to translate><Add a trailing whitespace to translate>
Example: tr en ru Hello World

### Demo

![trans](https://user-images.githubusercontent.com/34254373/229021207-bafee2b3-d42a-485b-82d5-75e7789c215f.gif)

Installation:

```bash
curl https://raw.githubusercontent.com/CRAG666/catapult-plugins-collection/main/plugins/translator.py --output ~/.local/share/catapult/plugins/translator.py
```

## Hash

### Usage

Write the method with which you want to generate the hash.

Format: <method> <text>
Exaple: sha256 Hello World!!

### Available methods

- blake2b
- blake2s
- md5
- sha1
- sha224
- sha256
- sha384
- sha3224
- sha3256
- sha3384
- sha3512
- sha512
- shake128
- shake256

### Demo

![hash](https://user-images.githubusercontent.com/34254373/229021281-14cf928d-ccc1-48a2-96d9-c4f7b0cd22f3.gif)

Installation:

```bash
curl https://raw.githubusercontent.com/CRAG666/catapult-plugins-collection/main/plugins/hash.py --output ~/.local/share/catapult/plugins/hash.py
```
