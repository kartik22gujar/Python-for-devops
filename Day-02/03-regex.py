
import re
#findall

txt="The quick brown fox"
ptr="brown"

search=re.search(ptr,txt)
if search:
    print("pattern Found",search.group())
else:
    print("pattern not found")

    