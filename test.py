from bs4 import BeautifulSoup 


with open('output11111.html', 'r',encoding='utf-8') as f:

    fullTable = '<table class="wikitable">'
    contents = f.read()
    soup = BeautifulSoup(contents,'lxml')
    table = soup.find('table', attrs={'class':'hprt-table'})
    
    rows = table.findAll("tr")
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
        # worksheet.write(i+1, 0, tenks) 
        # worksheet.write(i+1, 1, tenloaiphong) 
         
        # worksheet.write(i+1, 2, songuoitoida.text)   
        # worksheet.write(i+1, 2, gia)    
        print([tenloaiphong,songuoi,gia])
        i = i +1
         
    