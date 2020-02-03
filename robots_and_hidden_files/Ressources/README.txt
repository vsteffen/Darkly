In the exploit "robots_and_weak_passwd", i have used "Dirb" and i discovered the page "/.hidden" with robots.txt, let's jump into it.
We can see on this page a lot of directories each with a great depth. They each contain a "README" file with troll messages. There is surely a more interesting file between them than the others. So we will use a scraper to retrieve each of these files.
For this exercise, i have used "Scrapy". Scrapy is a python module used to scrap data. I think this is not necessarily the best choice for this excercise but I wanted to try this module. In our sources, we have to set the ip address in the file "./scrapy/darkly_find_readme/spiders/spider.py". Then we can use Scrapy with the following command:
scrapy crawl spider42
The main file in this project is "./scrapy/darkly_find_readme/spiders/spider.py". To explain it quickly, i crawl the website in the "parse" function, handle "README" files in parse_item and store in the dictionary "readme_dict" the md5 hash value of a "README" file as a key and as a value, i store a list containing the path of the file and the text inside it (i discard all similar files). Finally, when the spider is done (inside "spider_closed"), i print and write in "result.log" the results.
Which gives us :
{
	"0340f853e04efd01bd85489344d2bcb8": ["http://x.x.x.x/.hidden/ntyrhxjbtndcpjevzurlekwsxt/README", "Toujours pas tu vas craquer non ?\n"],
	"fa69fa10b5746be6c7d97b6b7233c021": ["http://x.x.x.x/.hidden/zzfzjvjsupgzinctxeqtzzdzll/lacqgphmpkmzjmaojyqnasjyvj/vpaznrumfdlwgbxuqnfmunthun/README", "Demande \u00c3\u00a0 ton voisin de gauche  \n"],
	"f09819cbed598e8093303d49ff82b56f": ["http://x.x.x.x/.hidden/zzfzjvjsupgzinctxeqtzzdzll/pyvqjseoycohylldbjajacgwgx/README", "Demande \u00c3\u00a0 ton voisin du dessous \n"],
	"09be0c62d97a138c4f64ae1d08869abb": ["http://x.x.x.x/.hidden/README", "Tu veux de l'aide ? Moi aussi !  \n"],
	"9f1ed3fdfd0423f1ab5961521a5e03ce": ["http://x.x.x.x/.hidden/zzfzjvjsupgzinctxeqtzzdzll/ttlemtrngbjvrxotdxihcbhdzu/README", "Non ce n'est toujours pas bon ...\n"],
	"565245faf0b3998ad6fd6429f2ef67bd": ["http://x.x.x.x/.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/lmpanswobhwcozdqixbowvbrhw/README", "99dde1d35d1fdd283924d84e6d9f1d820\n"],
	"0e114972cfa8cdcf9777bb9ff513ef36": ["http://x.x.x.x/.hidden/ntyrhxjbtndcpjevzurlekwsxt/zcgkxuyzzplsfnisngzlayvgee/README", "Demande \u00c3\u00a0 ton voisin du dessus  \n"],
	"b47df1febff005bc7fc9838b8bf53404": ["http://x.x.x.x/.hidden/amcbevgondgcrloowluziypjdh/README", "Demande \u00c3\u00a0 ton voisin de droite  \n"]
}
We can see in the results that we get the flag "99dde1d35d1fdd283924d84e6d9f1d820" in the path "http://x.x.x.x/.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/lmpanswobhwcozdqixbowvbrhw/README"
