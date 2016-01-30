from DatumBox import DatumBox
API_KEY = "2a13913dda346761765020c1f66e34f8"
datum_box = DatumBox(API_KEY)
print datum_box.keyword_extract("I hate my cat and love my dog")

