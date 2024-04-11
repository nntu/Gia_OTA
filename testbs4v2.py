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
    


tomorrow = datetime.today() + timedelta(1)
checkin = tomorrow.strftime('%Y-%m-%d')

date_next = tomorrow + timedelta(1)

checkout = date_next.strftime('%Y-%m-%d')

list_url =[
 
    ['Ks TTC',f'https://www.booking.com/hotel/vn/golf-can-tho.vi.html?aid=304142&label=gen173nr-1FCAso9AFCE211b25nLXRoYW5oLWNhbi10aG9IKlgEaPQBiAEBmAEquAEXyAEM2AEB6AEB-AECiAIBqAIDuALMud-wBsACAdICJDIxMDgzNThiLTA5MmUtNDM1ZS1hZjk0LWE2ZGI5MTcxMzhkNNgCBeACAQ&sid=df23a38e0f9f6fd596a1b9c15b92daee&all_sr_blocks=55062823_0_2_1_0;checkin={checkin};checkout={checkout};dest_id=-3709910;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=9;highlighted_blocks=55062823_0_2_1_0;hpos=9;matching_block_id=55062823_0_2_1_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=55062823_0_2_1_0__160200294;srepoch=1712841056;srpvid=fe435caef2b80098;type=total;ucfs=1&#hotelTmpl'],
    ['KS Muong thanh',f'https://www.booking.com/hotel/vn/muong-thanh-can-tho.vi.html?aid=304142&label=gen173nr-1FCAso9AFCE211b25nLXRoYW5oLWNhbi10aG9IKlgEaPQBiAEBmAEquAEXyAEM2AEB6AEB-AECiAIBqAIDuALMud-wBsACAdICJDIxMDgzNThiLTA5MmUtNDM1ZS1hZjk0LWE2ZGI5MTcxMzhkNNgCBeACAQ&sid=df23a38e0f9f6fd596a1b9c15b92daee&all_sr_blocks=0_0_2_1_0;checkin={checkin};checkout={checkout};dest_id=-3709910;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=0_0_2_1_0;hpos=1;matching_block_id=0_0_2_1_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=0_0_2_1_0__196784016;srepoch=1712845161;srpvid=fe435caef2b80098;type=total;ucfs=1&#hotelTmpl'],
    ['Nesta Hotel Can Tho',f'https://www.booking.com/hotel/vn/nesta.vi.html?aid=304142&label=gen173nr-1FCAso9AFCE211b25nLXRoYW5oLWNhbi10aG9IKlgEaPQBiAEBmAEquAEXyAEM2AEB6AEB-AECiAIBqAIDuALMud-wBsACAdICJDIxMDgzNThiLTA5MmUtNDM1ZS1hZjk0LWE2ZGI5MTcxMzhkNNgCBeACAQ&sid=df23a38e0f9f6fd596a1b9c15b92daee&all_sr_blocks=124809204_346804614_0_1_0;checkin={checkin};checkout={checkout};dest_id=-3709910;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=7;highlighted_blocks=124809204_346804614_0_1_0;hpos=7;matching_block_id=124809204_346804614_0_1_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=124809204_346804614_0_1_0__90931500;srepoch=1712845161;srpvid=fe435caef2b80098;type=total;ucfs=1&#hotelTmpl'],

    ['West Hotel',f'https://www.booking.com/hotel/vn/west.vi.html?aid=304142&label=gen173nr-1FCAso9AFCE211b25nLXRoYW5oLWNhbi10aG9IKlgEaPQBiAEBmAEquAEXyAEM2AEB6AEB-AECiAIBqAIDuALMud-wBsACAdICJDIxMDgzNThiLTA5MmUtNDM1ZS1hZjk0LWE2ZGI5MTcxMzhkNNgCBeACAQ&sid=df23a38e0f9f6fd596a1b9c15b92daee&all_sr_blocks=126810707_390572055_2_2_0;checkin={checkin};checkout={checkout};dest_id=-3709910;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=3;highlighted_blocks=126810707_390572055_2_2_0;hpos=3;matching_block_id=126810707_390572055_2_2_0;nflt=class%3D4;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=126810707_390572055_2_2_0__116415000;srepoch=1712845193;srpvid=fe435caef2b80098;type=total;ucfs=1&#hotelTmpl'],
    ['SOJO HOTEL CAN THO',f'https://www.booking.com/hotel/vn/sojo-can-tho.vi.html?aid=304142&label=gen173nr-1FCAso9AFCE211b25nLXRoYW5oLWNhbi10aG9IKlgEaPQBiAEBmAEquAEXyAEM2AEB6AEB-AECiAIBqAIDuALMud-wBsACAdICJDIxMDgzNThiLTA5MmUtNDM1ZS1hZjk0LWE2ZGI5MTcxMzhkNNgCBeACAQ&sid=df23a38e0f9f6fd596a1b9c15b92daee&all_sr_blocks=0_0_2_0_0;checkin={checkin};checkout={checkout};dest_id=-3709910;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=4;highlighted_blocks=0_0_2_0_0;hpos=4;matching_block_id=0_0_2_0_0;nflt=class%3D4;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=0_0_2_0_0__111222496;srepoch=1712845193;srpvid=fe435caef2b80098;type=total;ucfs=1&#hotelTmpl'],
    ['Van Phat Riverside Hotel',f'https://www.booking.com/hotel/vn/van-phat-riverside.vi.html?aid=304142&label=gen173nr-1FCAso9AFCE211b25nLXRoYW5oLWNhbi10aG9IKlgEaPQBiAEBmAEquAEXyAEM2AEB6AEB-AECiAIBqAIDuALMud-wBsACAdICJDIxMDgzNThiLTA5MmUtNDM1ZS1hZjk0LWE2ZGI5MTcxMzhkNNgCBeACAQ&sid=df23a38e0f9f6fd596a1b9c15b92daee&all_sr_blocks=59043707_0_2_1_0;checkin={checkin};checkout={checkout};dest_id=-3709910;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=5;highlighted_blocks=59043707_0_2_1_0;hpos=5;matching_block_id=59043707_0_2_1_0;nflt=class%3D4;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=59043707_0_2_1_0__406560616;srepoch=1712845193;srpvid=fe435caef2b80098;type=total;ucfs=1&#hotelTmpl'],

]
data = []
for i in list_url:
    print(i[1])
    data.append(getdata(i[0],i[1]))
    

workbook = xlsxwriter.Workbook('output.xlsx')    

worksheet = workbook.add_worksheet(checkin + '--'+ checkout )
worksheet.write(0, 0, 'Ten KS') 
worksheet.write(0, 1, 'Loai Phong')          
worksheet.write(0, 2, 'So Nguoi')   
worksheet.write(0, 3, 'gia')   
a = 0
for i in data:
    for b in i:
        worksheet.write(a+1, 0, b[0]) 
        worksheet.write(a+1, 1, b[1])          
        worksheet.write(a+1, 2, b[2])   
        worksheet.write(a+1, 3, b[3])   
        a = a + 1 
    
workbook.close()           