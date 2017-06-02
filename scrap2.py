from scrapy import Field, Spider, Item, Selector


class Post(Item):
	title = Field()
	score = Field()

class FotogramaSpider(Spider):

	def nombre():
		#obtengo pelicula de dropbox (aun no implementado)
		return "Troya"

	film = nombre()
	name, start_urls = 'FotogramaSpider', ['http://www.fotogramas.es/Peliculas?pelicula=' + film + '&genero=0&anio=0']

	def parse(self, response):

		sel = Selector(response)

		title = response.xpath('//div[@class="teaser_text"]');
		score = response.xpath('//div[@class="star list5"]/span').extract()

		items = []
		p = []

		i = 0
		pos = -1
		
		while i < len(title):
			p.append(title[i].xpath('/a/p[@class="encabezado1"]/text()').extract())
			print(title[i])
			if p[i] == FotogramaSpider.film:
				pos = i
				titulo = title[i]
				if (score[i].find('20%') != -1):
					puntuacion = '1.0'
				elif (score[i].find('40%') != -1):
					puntuacion = '2.0'
				elif (score[i].find('60%') != -1):
					puntuacion = '3.0'
				elif (score[i].find('80%') != -1):
					puntuacion = '4.0'
				else:
					puntuacion = '5.0'
			i = i + 1

		if pos != -1:
			post = Post()
			post['title'] = titulo
			post['score'] = puntuacion
			items.append(post)

		return items
