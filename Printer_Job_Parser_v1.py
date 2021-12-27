import tabula
import json
def lambda_handler(event, context):
    print('Execution is start!!!!.....')
    tabula.read_pdf('https://github.com/tabulapdf/tabula-java/raw/master/src/test/resources/technology/tabula/arabic.pdf', pages='all')
