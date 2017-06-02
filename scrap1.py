from scrapy import Field, Spider, Item, Selector

class Post(Item):
	puntuacion = Field()
	title = Field()
	pagina = Field()

class ImdbSpider(Spider):

	allowed_domains = ["http://www.imdb.com/"]
	name = 'ImdbSpider'
	peliculaName = ''
	start_urls = ["http://www.imdb.com/search/title?title=" + peliculaName]

	def parse(self, response):
		sel = Selector(response)
		peliculasTitle = sel.xpath('//div[@class="lister-item-content"]/h3[@class="lister-item-header"]/a/text()').extract()
		peliculasPuntuacion = sel.xpath('//div[@class="ratings-bar"]/div[@class="inline-block ratings-imdb-rating"]/strong/text()').extract()

		items = []
		titulo = ""
		#Busca si alguna de las peliculas encontradas coincide con el nombre exacto
		#en caso de que coincida, se guarda su posicion en pos.
		i = 0
		pos = -1
		encuentra = -1
		while (i < len(peliculasTitle) and encuentra==-1):
			if peliculasTitle[i] == ImdbSpider.peliculaName:
				pos = i
				encuentra = 0
			i = i + 1

		#Si pos es distinto de -1, significa que ha encontrado 1 pelicula que se llama igual
		if (pos != -1):
			post = Post()
			post['title'] = peliculasTitle[pos]
			post['puntuacion'] = peliculasPuntuacion[pos]
			post['pagina'] = 'imdb'
			items.append(post)

		return items