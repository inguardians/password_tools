#! /usr/bin/python

# passrulegen_casetoggle.py
# Written by Jarrod Frates (NetworkLlama) for InGuardians.
# 
# Generate alteration rules compatible with JtR and oclHashcat.
# Sets case change points for each character location.  A result of
# T7 switches the case of the 8th position, so 'password' becomes
# 'passworD', and T0T3 would set it to 'PasSword'.  Non-letter
# characters are ignored by the programs.

# Set up some variables. Change l for different maximum word length.
i = 0
l = 10
m = 2**l

# Preserve original password example
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
            p += 'T' + str(q)
        q += 1
    # Output to stdout.  With colon from before loop, uses original
    # password plus all mangled forms.
    print p
    i += 1
