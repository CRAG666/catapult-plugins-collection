# Catapult Plugins Collection

Plugin collection to integrate with catapult launcher

# Plugins available

## Translator

### Usage

Just write the word tr, then the base language and the
language to translate, finally just add what you want translate.

Remember that for the translation to be executed you must add a blank space at the end.

Format: tr <source language> <target language> <Text to translate>
Example: tr en ru Hello World

### Demo


https://user-images.githubusercontent.com/34254373/229009624-b953bbb4-e6bf-4859-8f52-fa73df8eec0b.mp4

Installation:

```bash
pip install aiohttp
curl https://raw.githubusercontent.com/CRAG666/catapult-plugins-collection/main/plugins/translator.py --output ~/.local/share/catapult/plugins/translator.py
```

## Hash

### Usage

Write the method with which you want to generate the hash.

Format: <method> <text>
Exaple: sha256 Hello World!!

### Available methods

 * blake2b
 * blake2s
 * md5
 * sha1
 * sha224
 * sha256
 * sha384
 * sha3224
 * sha3256
 * sha3384
 * sha3512
 * sha512
 * shake128
 * shake256

### Demo


https://user-images.githubusercontent.com/34254373/229009770-7513ff0e-ab34-4f72-8465-3186d7c695d8.mp4


Installation:

```bash
curl https://raw.githubusercontent.com/CRAG666/catapult-plugins-collection/main/plugins/hash.py --output ~/.local/share/catapult/plugins/hash.py
```
