#!/usr/bin/python

from __future__ import print_function
import json
import sys

# Edit this to change the seperator
SASSC_SEPERATOR = " "

def main():
    if len(sys.argv) != 3:
        print_usage()
    choices = ["ipa", "xsampa", "sassc"]
    source = sys.argv[1]
    sink = sys.argv[2]

    # Validate params
    try:
        choice1 = choices.index(sys.argv[1])
        choice2 = choices.index(sys.argv[2])
        if choice1 == choice2:
            print_usage()
    except ValueError:
        print_usage()

    # Mappings from disk
    # some may not be used if source or sink is already IPA
    source_to_ipa = {}
    ipa_to_sink = {}

    ipa_xsampa = []
    sassc_ipa = []

    with open("./ipa_xsampa_map.json") as f:
        ipa_xsampa = json.load(f)

    sassc_active = source == "sassc" or sink == "sassc"
    if sassc_active:
        with open("./sassc_ipa.json") as f:
            sassc_ipa = json.load(f)

    if source == "xsampa":
        for pair in ipa_xsampa:
            source_to_ipa[pair[1]] = pair[0]
    elif source == "sassc":
        for pair in sassc_ipa:
            source_to_ipa[pair[0]] = pair[1]

    if sink == "xsampa":
        for pair in ipa_xsampa:
            ipa_to_sink[pair[0]] = pair[1]
    elif sink == "sassc":
        for pair in sassc_ipa:
            ipa_to_sink[pair[1]] = pair[0]

    # Combine them into a single mapping
    mapping = {}
    if source == "ipa":
        mapping = ipa_to_sink
    elif sink == "ipa":
        mapping = source_to_ipa
    else:
        for k, ipas in source_to_ipa.iteritems():
            map_out = ""
            failed = False
            for ipa in ipas:
                val = ipa_to_sink.get(ipa)
                if not val:
                    failed = True
                    break
                map_out += val
            mapping[k] = map_out if not failed else None

    line = sys.stdin.readline()
    seperator = SASSC_SEPERATOR if sassc_active else ""
    # Do the conversion now
    while line:
        line = unicode(line.strip())
        output = []
        if sassc_active:
            tokens = line.split(SASSC_SEPERATOR)
        else:
            tokens = line
        for token in tokens:
            mapped = mapping.get(token)
            if not mapped:
                print("WARNING: could not map token ", token, file=sys.stderr)
            else:
                output.append(mapped)
        output = seperator.join(output)
        print(output)
        line = sys.stdin.readline()
    
def print_usage():
    print("Usage: python sassc_converter.py ipa xsampa")
    print("Choices: ipa xsampa sassc")
    print("The example command reads STDIN ipa and pipes xsampa to STDOUT")
    print("Tokens must be seperated, by default the seperator is whitespace")
    print("Edit the script to change the seperator.")
    exit(1)

if __name__ == "__main__":
    main()
