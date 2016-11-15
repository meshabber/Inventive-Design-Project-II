from pptx import Presentation
from bs4 import BeautifulSoup
import mistune

# read md2 file 
md_text = open("md2ppt.md", 'r').read()
md = mistune.markdown(md_text)
bs = BeautifulSoup(md, 'html.parser')

prs = Presentation()
# Title
title_slide_layout = prs.slide_layouts[0]
slide = prs.slides.add_slide(title_slide_layout)
title = slide.shapes.title
subtitle = slide.placeholders[1]

title.text = bs.h1.text
#subtitle.text = "hello, world"

def recursive_list(bs, depth):
    for child in bs.descendants:
        print(child, depth)

slide_title = bs.h2
while slide_title: 
    bullet_slide_layout = prs.slide_layouts[1]
    slide = prs.slides.add_slide(bullet_slide_layout)
    title = slide.shapes.title
    body = slide.shapes.placeholders[1]

    title.text = slide_title.text

    tf = body.text_frame

    text_contents = slide_title.find_next('ul')
    recursive_list(text_contents, 0)
#    for text in text_contents.findAll('li'):
#        p = tf.add_paragraph()
#        p.text = text.text

    slide_title = slide_title.find_next('h2')
    

prs.save('out.pptx')
