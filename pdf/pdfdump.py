#!/Library/Developer/CommandLineTools/usr/bin/python3

import sys
from pypdf import PdfReader
from pypdf.generic import DictionaryObject
from pypdf.generic import IndirectObject


# convert a DictionaryObject to nested dict
def expand_DictionaryObject(obj):
    if type(obj) != DictionaryObject:
        return obj
    return {k: expand_DictionaryObject(obj[k]) for k in obj.keys()}

def dump_annotations(pdf, simple_format):
    i = 1
    for page in pdf.pages:
        print("========= page %s annotation =============" % i)
        if "/Annots" in page:
            for annot in page["/Annots"]:
                obj = annot.get_object()
                if simple_format:
                    annotation = {"subtype": obj["/Subtype"],
                                  "widgettype": obj.get("/FT"),
                                  "location": obj["/Rect"],
                                  "fieldname": obj.get("/T"),
                                  "text": obj.get("/TU"),
                                  "value": obj.get("/V")}
                    print(annotation)
                else:
                    print(obj)
        i += 1

def dump_text(pdf):
    i = 1
    for page in pdf.pages:
        print("========= page %s text =============" % i)
        text = page.extract_text()
        print(text)
        i += 1



assert len(sys.argv) == 2, "please specify a pdf filename"
filename = sys.argv[1]
pdf = PdfReader(filename)
dump_text(pdf)
dump_annotations(pdf, simple_format=True)
