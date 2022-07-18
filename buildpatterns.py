import re
import json
import sys

# working as of https://github.com/gamma-delta/HexMod/blob/c00815b7b9d90593dc33e3a7539ce87c2ece4fc9/Common/src/main/java/at/petrak/hexcasting/common/casting/RegisterPatterns.java
# - go to https://github.com/gamma-delta/HexMod/blob/main/Common/src/main/java/at/petrak/hexcasting/common/casting/RegisterPatterns.java
# - right click the "Raw" button, click "Save Link As", and save it with the name "RegisterPatterns.java" to the same folder as this script
#   - note: you'll have to do this again after each update, if new patterns are added or old patterns are changed

registry = re.compile(r"PatternRegistry\s*\.\s*mapPattern\s*\(\s*HexPattern\s*\.\s*fromAngles\s*\(\s*\"([aqwed]+)\"\s*,\s*HexDir\s*\.\s*\w+\s*\)\s*,\s*modLoc\s*\(\s*\"([\w/]+)\"\s*\)", re.M)

# parse the pattern definitions
pattern_lookup = {}
for filename in sys.argv[1:]:
    with open(filename, "r", encoding="utf-8") as file:
        for match in registry.finditer(file.read()):
            (pattern, name) = match.groups()
            pattern_lookup[pattern] = name

json.dump(pattern_lookup, sys.stdout)