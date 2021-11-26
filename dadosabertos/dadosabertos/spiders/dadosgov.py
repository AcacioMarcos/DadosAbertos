import scrapy


class DadosgovSpider(scrapy.Spider):
    name = 'dadosgov'

    start_urls = [f'https://dados.gov.br/dataset?page={i}' for i in range (1, 531)]

    def parse(self, response, **kwargs):
        for i in response.xpath('//li[@class="dataset-item"]'):
            dataset = i.xpath('.//h3').get()
            link = i.xpath('.//h3/a/@href').get()
            descricao = i.xpath('.//div/text()').get()

            yield{
            'dataset' : dataset,
            'link' : link,
            'descricao' : descricao
            }
