# with open("result.txt") as f:
#     content = f.readlines()
# # you may also want to remove whitespace characters like `\n` at the end of each line
# content = [x.strip() for x in content]
# 
# content[:] = [''.join(content[:])]
# print(len(content))


from ABBYY import CloudOCR
ocr_engine = CloudOCR(application_id='twoocrtext', password='DANuhfXhuuwyXuvjW/cWbmpt')
pdf = open('locol1.png', 'rb')
ok = open("good","w")
file = {ok:ok}
result = ocr_engine.processImage(file, exportFormat='txt', language='English')
