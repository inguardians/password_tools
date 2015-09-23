#! /usr/bin/python

# passrulegen_1337toggle.py
# Written by Jarrod Frates (NetworkLlama) for InGuardians.
# 
# Generate 1337ification rules compatible with JtR and oclHashcat.
# Within the array, it checks for the presence of each character
# (leading slash and following character) and, if present, swaps
# the given character for the next character.  For example, '/asa4'
# checks for the letter 'a' (/a) and then swaps out (s) 'a' for '4'.
#
# The character checks make this more efficient, but there are still
# inefficiencies were two letter swaps are in the same line, though
# this probably doesn't add very much overall overhead.  Output rules
# also doe not account for differing 1337 characters for the same
# letter in the same password (e.g., pa5$word).

# Define list with 1337 swaps
d = ['/asa4', '/asa@', '/ese3', '/gsg9', '/hsh#', '/isi!', '/lsl1', '/oso0', '/sss5', '/sss$', '/sst7', '/sst+']

# Set up other variables
i = 0
l = len(d)
m = 2**l

# Preserve original, unmangled password example
print ":"

# Create rules
while i < m:
    # Convert length of list to string representation of binary number,
    # stripping off leading '0x'
    n = bin(i)
    o = n[2:]
    # Pad for leading zeroes (Python returns first 1 as first visible
    # digit in binary strings)
    if len(o) < l:
        o = ((l - len(o)) * '0') + o
    # Create string to hold rule
    p = ''
    q = 0
    while q < l:
        # Only include the item if 1 is in location
        if o[q] != '0':
            p += d[q]
        q += 1
    # Output to stdout.  With colon from before loop, uses original
    # password plus all mangled forms.
    print p
    i += 1

