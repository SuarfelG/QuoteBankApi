import requests

base='http://127.0.0.1:5000/'

resource=requests.put(base+'quotes/1',{"quote":"now or never", "author":"kobby briant"})
resource=requests.put(base+'quotes/2',{"quote":"the body is capable of everything it is the mind limiting", "author":"goggins "})
resource=requests.put(base+'quotes/3',{"quote":"just do it", "author":"Nike "})
resource=requests.put(base+'quotes/25',{"quote":"If something is important enough you do it even if the odds are not in your favor", "author":"Elon Musk"})


print(resource.json())


input()


resource=requests.get(base+'quotes/25')
