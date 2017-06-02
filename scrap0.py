from scrapy import Field, Spider, Item, Selector 

class Post(Item):
    puntuacion = Field()
    title = Field()
    pagina = Field()

class FilmAffinitySpider(Spider):

	allowed_domains = ["https://www.filmaffinity.com/"]
	name = 'FilmAffinitySpider'
	peliculaName = 'Braveheart'
	start_urls = ["https://www.filmaffinity.com/es/advsearch.php?stext=" + peliculaName]

	def parse(self, response):
		sel = Selector(response)
		peliculasTitle = sel.xpath('//div[@class="mc-title"]')
		peliculasPuntuacion = sel.xpath('//div[@class="avgrat-box"]')

		items = []

		#Busca si alguna de las películas encontradas coincide con el nombre exacto
		#en caso de que coincida, se guarda su posición en pos.
		i = 0
		pos = -1
		encuentra = -1		
		while (i < len(peliculasTitle) and encuentra==-1):
			p = peliculasTitle[i].xpath('a/text()').extract()
			if p[0] == FilmAffinitySpider.peliculaName:
				pos = i
				encuentra = 0
			i = i + 1

		#Si pos es distinto de -1, significa que ha encontrado 1 película que se llama igual
		if pos != -1:
			post = Post()
			titulo = peliculasTitle[pos].xpath('a/text()').extract()
			post['title'] = titulo[0]
			puntuacion = peliculasPuntuacion[pos].xpath('text()').extract()
			post['puntuacion'] = puntuacion[0]
			post['pagina'] = 'filmaffinity'
			items.append(post)

		return items