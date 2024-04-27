#imports
from docx import Document
from docx.shared import pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
#create new document
doc = Document()
#add title
title = doc.add_heading ("my new documet sample1", level=2)
title.alignment = WD_ALIGN_PARAGRAPH.LEFT




