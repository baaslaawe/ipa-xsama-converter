# ipa-xsama-converter

Includes a converter between IPA and X-Sama, mappings taken from:
https://github.com/dohliam/xsampa

Also includes a converter between IPA and the Arabic SASSC phone mapping as seen here:
http://ssw8.talp.cat/papers/ssw8_PS3-1_Almosallam.pdf

## Usage

You must cd into this project directory, or at least have the \*.json files available
at your current working directory. 

```
python ipa xsampa
```

It reads from STDIN and writes to STDOUT, and the tokens it takes must be seperated,
by default the seperator is a whitespace but this can be changed by editing
converter.py.

You could use it with standard unix pipes as such:

```
cat input.txt | python ipa xsampa > output.txt
```

Mappings available: ipa xsampa sassc
