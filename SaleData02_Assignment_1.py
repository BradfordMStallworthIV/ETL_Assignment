# program to read XML File
# and store it as a CSV File

import xml.etree.ElementTree as ET
import pandas

#load the XML data and get the ROOT
xtree = ET.parse('SaleData02.xml')
xroot = xtree.getroot()

#extract data on each node as one record
#and append it to a list of records
records = []
for node in xroot:
    sid = node.find('id').text
    sdate = node.find('transdate').text
    cust_first = node.find('name/first').text
    cust_last = node.find('name/last').text                      
    street = node.find('street').text
    state  = node.find('state').text
    Zipcode = node.find('zip').text
    phone = node.find('phone').text
    email = node.find('email').text
    product = node.find('prodtype').text
    itemcount = node.find('qty').text
    unitprice = node.find('price').text
    total = node.find('total').text
    records.append([sid, sdate, cust_first, cust_last, street, state, Zipcode, phone, email, product, itemcount, unitprice, total])
print(records)
#successful

# Transform the list of records into a datafram column

df = pandas.DataFrame(records, columns =['id','transdate','first','last','street','state','zip','phone','email','prodtype','qty','price','total'])
print(df)

# save data frame to file

df.to_csv('SaleData02.csv', index=False)
