#!/bin/bash
rm -f $2
IFS=$'\n'
OUTPUT="{\n"
for LINE in $(cat $1)
do
    lineLength=${#LINE}
    if [[ "$LINE" = *"="* ]]; then
        JsonLine="\"${LINE/=/"\":\""}";
        JsonLine=$(sed "s/$/"\","/" <<< "${JsonLine}")
        OUTPUT=${OUTPUT}${JsonLine}"\n"
    fi
done
OUTPUT=${OUTPUT%???}
OUTPUT+="\n}"
touch $2
printf $OUTPUT >> $2