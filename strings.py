from typefunctions import basefuncs
from typefunctions import stringfuncs

# l = basefuncs.random_string()

s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr \
 ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

new_s = s.replace("k", "m")
new_s = new_s.replace("o", "q")
new_s = new_s.replace("e", "g")

print(new_s)
print(new_s.find("k"), new_s.find("o"), new_s.find("e"))