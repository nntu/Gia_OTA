from bs4 import BeautifulSoup 
from lxml import etree 
import requests 
import xlsxwriter
import re
from datetime import timedelta,datetime

def getdata(tenks, url):
 
    HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'}
    
    webpage = requests.get(url, headers=HEADERS) 
    soup = BeautifulSoup(webpage.text,'lxml')
    # data = []
    table = soup.find('table', attrs={'class':'hprt-table'})
    
    # file = open("output11111.html", "w",encoding='utf-8')
    # file.write(str(table))
    # file.close()
    data=[]
    
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
   
     
    row_lengths = [len(r.findAll(['th', 'td'])) for r in rows]
    ncols = max(row_lengths)
    nrows = len(rows)

    # rows and cols convert list of list
    for i in range(len(rows)):
        rows[i]=rows[i].findAll(['th', 'td'])


    # Header - colspan check in Header
    for i in range(len(rows[0])):
        col = rows[0][i]
        if (col.get('colspan')):
            cSpanLen = int(col.get('colspan'))
            del col['colspan']
            for k in range(1, cSpanLen):
                rows[0].insert(i,col)


    # rowspan check in full table
    for i in range(len(rows)):
        row = rows[i]
        for j in range(len(row)):
            col = row[j]
            del col['style']
            if (col.get('rowspan')):
                rSpanLen = int(col.get('rowspan'))
                del col['rowspan']
                for k in range(1, rSpanLen):
                    rows[i+k].insert(j,col)

    tenloaiphong = ''
    gia = ''
    songuoi = ''
    i =  0
    for i in range(len(rows)):
        row = rows[i]
      
        
        spans = row[0].find('span', attrs={'class':'hprt-roomtype-icon-link'})
        if spans != None:
            tenloaiphong = spans.text
      
        
        songuoitoida = row[1].find('span', attrs={'class':'bui-u-sr-only'})
        if songuoitoida != None:
            songuoi =  songuoitoida.text
        
        spans_gia = row[2].find('span', attrs={'class':'prco-valign-middle-helper'})
        
        if spans_gia != None:
            gia  = spans_gia.text
  
        
        print([tenks,tenloaiphong,songuoi,gia.replace("VND\xa0",'')])
        data.append([tenks,tenloaiphong.replace('\n' ,''),songuoi.replace('\n' ,''),gia.replace("VND\xa0",'').replace('\n' ,'').replace('.' ,'')]) 
        i = i +1
    return data


tomorrow = datetime.today() + timedelta(3)
checkin = tomorrow.strftime('%Y-%m-%d')

date_next = tomorrow + timedelta(1)

checkout = date_next.strftime('%Y-%m-%d')


url = f'https://www.booking.com/searchresults.html?label=gen173nr-1FCAEoggI46AdIM1gEaPQBiAEBmAExuAEXyAEM2AEB6AEB-AECiAIBqAIDuALegN6wBsACAdICJDdhNTYwNjQ0LTJjNjMtNGJmYi1hYjRiLWY3ZTU4MGQ3NzRkMtgCBeACAQ&sid=bf3f228a25efbe3ed0fa7286cf307660&aid=304142&ss=Can+Tho&ssne=Can+Tho&ssne_untouched=Can+Tho&lang=vi&src=searchresults&dest_id=-3709910&dest_type=city&checkin={checkin}&checkout={checkout}&group_adults=2&no_rooms=1&group_children=0&nflt=class%3D5%3Bclass%3D4'

HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'}
webpage = requests.get(url, headers=HEADERS) 
soup = BeautifulSoup(webpage.text,'lxml')
print(url)




table = soup.findAll('div', attrs={'class':'c066246e13 d8aec464ca'})
listlink =[]
for div in table:
    link = div.find('a',attrs={'class':'a78ca197d0'})
    if link != None:
        name = link.find('div',attrs={'data-testid':'title'})
        print(name)
        listlink.append([name.text,link['href']])


workbook = xlsxwriter.Workbook(f'output_{checkin}_{checkout}.xlsx')    

worksheet = workbook.add_worksheet(checkin + '--'+ checkout )
worksheet.write(0, 0, 'Ten KS') 
worksheet.write(0, 1, 'Loai Phong')          
worksheet.write(0, 2, 'So Nguoi')   
worksheet.write(0, 3, 'gia')   
a = 0
for i in listlink:
    print(i[1])
    data = getdata(i[0],i[1])
    for d in data:
        worksheet.write(a+1, 0, d[0]) 
        worksheet.write(a+1, 1, d[1])          
        worksheet.write(a+1, 2, d[2])   
        worksheet.write(a+1, 3, d[3])   
        a = a + 1 




workbook.close()   



