import re
text = "Hello, my email is ashishkumarsingh1234@gmail.com"
pattern = r'\b\w+@\w+\.\w+\b'
match = re.search(pattern, text)
if match:
    print("Found:", match.group())
else:
    print("Not Found")
    
import re

# A regular expression pattern is defined in the pattern variable. This pattern is used to match email addresses. Let's break down the components of the pattern:
# \b: This represents a word boundary, ensuring that the pattern matches only whole words.
# \w+: This matches one or more word characters (letters, digits, or underscores), which are typically present in the username part of an email address.
# @: This matches the literal "@" symbol.
# \w+: This again matches one or more word characters, which are typically present in the domain name part of an email address.
# \.: This matches the literal period (dot) character.
# \w+: This matches one or more word characters, which are typically present in the top-level domain (TLD) part of an email address.
# \b: Another word boundary to ensure a complete match.
# The r before the string indicates a raw string, allowing backslashes to be used without escaping.