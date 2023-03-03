
# importing required modules
import PyPDF2
import re
  
# creating a pdf file object
pdfFileObj = open('Orthodox_KJV.pdf', 'rb')
  
# creating a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)
  
# printing number of pages in pdf file
no_of_pages = len(pdfReader.pages)
print(no_of_pages)
  
# creating a page object
# lines = ['Readme', 'How to write text files in Python']
# with open('readme.txt', 'w', encoding='utf-8') as f:
#     for line in lines:
#         f.write(line)
#         f.write('\n')

# def convert_case(match_obj):
#   if match_obj.group(1) is not None:
#     return match_obj.group(1).lower()
#   if match_obj.group(2) is not None:
#     return match_obj.group(2).upper()

# str = "jOE kIM mAx ABY lIzA"
# print(re.sub(r"([A-Z]+) | ([a-z]+)", convert_case, str))

def convert_case(match_obj):
    response = "<sup>" + str(match_obj.group(0)) + "</sup>"
    return response

        


pages = pdfReader.pages
page_no = 1
with open('Orthodox_KJV.txt', 'w', encoding='utf-8') as f:
    for page in pages:
        # allocate text of page to variable
        text = page.extract_text()

        # replace quotation marks that don't play nicely
        text = text.replace("‘", "\'")
        text = text.replace("’", "\'")

        # reduce double spaces after periods to single
        text = text.replace('  ', ' ')
        text = text.replace(' ', ' ')
        text = text.replace('  ', ' ')
        text = text.replace('.  ', '. ')

        # superscript all numbers
        text = re.sub(r'\d+', convert_case, text)

        f.write(text)
        
        print(f'copied page {page_no} of {no_of_pages}')
        page_no += 1


# pageObj = pdfReader.pages[0]
  
# extracting text from page
# print(pageObj.extract_text())
  
# closing the pdf file object
pdfFileObj.close()