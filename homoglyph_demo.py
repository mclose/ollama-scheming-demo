#!/usr/bin/env python3
"""The DseWiki trick: two usernames that look identical and aren't.

The OpenAI agents impersonated the wiki's admin with a Cyrillic "е" (U+0435)
in place of a Latin "e" (U+0065). Same trick as IDN phishing domains.
"""
import unicodedata

real = "WikiAdmin-Peter"     # illustrative name
fake = "WikiAdmin-Pеter"   # Cyrillic small ie

print(f"real: {real}")
print(f"fake: {fake}")
print(f"equal? {real == fake}\n")
for a, b in zip(real, fake):
    if a != b:
        print(f"  {a!r} U+{ord(a):04X} {unicodedata.name(a)}")
        print(f"  {b!r} U+{ord(b):04X} {unicodedata.name(b)}")
print(f"\nas a domain: {('p' + chr(0x0435) + 'ter.com').encode('idna').decode()}  (what DNS actually sees)")
