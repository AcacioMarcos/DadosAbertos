import scrapy


class DadosgovSpider(scrapy.Spider):
    name = 'dadosgov_sp'

    start_urls = [f'http://catalogo.governoaberto.sp.gov.br/dataset?page={i}' for i in range (1, 26)]


    def parse(self, response, **kwargs):
        for i in response.xpath('//div[@class="row"]'):
            dataset = i.xpath('.//h2').get()
            responsavel = i.xpath('.//h3').get()
            link = i.xpath('.//h2[@class="dataset-heading"]').get()
            descricao = i.xpath('.//p/text()').get()

            yield{
            'dataset' : dataset,
            'responsavel' : responsavel,
            'link' : link,
            'descricao' : descricao
            }





