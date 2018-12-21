import scrapy
import xlrd

#scrapy runspider distancia2.py -o dist2.json

class distancia2(scrapy.Spider):
    name = "distancias"
    # custom_settings = {
    # 'CONCURRENT_REQUESTS': 30,
    # 'CONCURRENT_REQUESTS_PER_DOMAIN': 30,
    # }
    workbook = xlrd.open_workbook('http://www.estivel.com.br/vetorcidades.xls.xls')
    worksheet = workbook.sheet_by_name('cidades')
    global origem, destino
    cidades=[]
    links=[]
    for i in range (5565): #array com os municipios, 5565
        cidades.append(worksheet.cell(i, 0).value)   
    origem = cidades[0] 
    destino = cidades[0] 
    cont = 0
    for origem in cidades:  
        origem = origem  
        for i in range(1+cont,5565):
            destino = cidades[i]
            links.append('http://www.distanciasentrecidades.com/pesquisa?from=' + origem + '&to=' + destino,)
        cont+=1
    start_urls=[]
    for i in range(100,200):
        start_urls.append(links[1],)  

    def parse(self, response):
        for distance in response.css('#web'):
            KM_SELECTOR = '#kmsruta::text'
            ORIGEM_SELECTOR = '.origenName::text'
            DESTINO_SELECTOR = '.destinoName::text'
            yield {
                'Origem' : distance.css(ORIGEM_SELECTOR).extract_first(),
                'Destino' : distance.css(DESTINO_SELECTOR).extract_first(),
                'km' : distance.css(KM_SELECTOR).extract(),
            }