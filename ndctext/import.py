import json

username = 'ADMIN'
password = 'bykjIp-huvxif-nigru9'

f1 = [ i.split('\t') for i in open('product.txt', 'r', encoding='ISO-8859-1').read().split('\n')[:-1] ]
f2 = [ i.split('\t') for i in open('package.txt', 'r', encoding='ISO-8859-1').read().split('\n')[:-1] ]

items = {}
for i in f1[1:]:
  items[i[0]] = {
    'PRODUCTID': i[0],
    'PRODUCTNDC': i[1],
    'PRODUCTTYPENAME': i[2],
    'PROPRIETARYNAME': i[3],
    'PROPRIETARYNAMESUFFIX': i[4],
    'NONPROPRIETARYNAME': i[5],
    'DOSAGEFORMNAME': i[6],
    'ROUTENAME': i[7],
    'STARTMARKETINGDATE': i[8],
    'ENDMARKETINGDATE': i[9],
    'MARKETINGCATEGORYNAME': i[10],
    'APPLICATIONNUMBER': i[11],
    'LABELERNAME': i[12],
    'SUBSTANCENAME': i[13],
    'ACTIVE_NUMERATOR_STRENGTH': i[14],
    'ACTIVE_INGRED_UNIT': i[15],
    'PHARM_CLASSES': i[16],
    'DEASCHEDULE': i[17],
    'NDC_EXCLUDE_FLAG': i[18],
    'LISTING_RECORD_CERTIFIED_THROUGH': i[19],
    'NDCS': [],
    'PACKAGES': [],
  }

for i in f2[1:]:
  items[i[0]]['PACKAGES'].append({
    'NDCPACKAGECODE': i[2],
    'PACKAGEDESCRIPTION': i[3],
    'STARTMARKETINGDATE': i[4],
    'ENDMARKETINGDATE': i[5],
    'NDC_EXCLUDE_FLAG': i[6],
    'SAMPLE_PACKAGE': i[7],
    })
  items[i[0]]['NDCS'].append(i[2].replace('-', ''))

for i in f2[1:]:
  if i[1] == items2[i[0]]['PRODUCTNDC'] and i[4] == items2[i[0]]['STARTMARKETINGDATE'] and i[5] == items2[i[0]]['ENDMARKETINGDATE'] and i[6] == items2[i[0]]['NDC_EXCLUDE_FLAG']:
    continue
  else:
    if not i[4] == items2[i[0]]['STARTMARKETINGDATE']: print('STARTMARKETINGDATE', i[4], items2[i[0]]['STARTMARKETINGDATE'])
    if not i[5] == items2[i[0]]['ENDMARKETINGDATE']: print('ENDMARKETINGDATE', i[5], items2[i[0]]['ENDMARKETINGDATE'])