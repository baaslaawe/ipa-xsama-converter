#!/bin/bash

# Checks that th other and converter files are working correctly
# espeak must be on the path

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

if [ $# -ne 2 ]; then
  echo "Usage: ./validator.sh word_to_test xsampa|sassc"
  exit 1
fi

if [ $2 != "xsampa" ] && [ $2 != "sassc" ]; then
  echo "Usage: ./validator.sh word_to_test xsampa|sassc"
  exit 1
fi

echo "Testing ipa and $2 for $1"
ipa=$(espeak -q --ipa=3 -v en "$1" | sed -r "s/^\s?(.+)\s?$/\1/g" | sed "s/_/ /g")
echo "ipa: $ipa"
other=$(echo "$ipa" | $DIR/converter.py ipa $2)
echo "$2: $other"

# Do a double conversion to strip out characters that aren't valid
# in sassc
if [ $2 == "sassc" ]; then
  ipa=$(echo "$other" | $DIR/converter.py $2 ipa)
  echo "new ipa: $ipa"
fi

diff <(echo "$other" | $DIR/converter.py $2 ipa) \
  <(echo "$ipa")

if [[ $? == 0 ]]; then
  echo "Success"
else
  echo "Failure!"
fi
