import requests

base='http://127.0.0.1:5000/'

resource=requests.put(base+'quotes/1',{"quote":"now or never", "author":"kobby briant"})
resource=requests.put(base+'quotes/2',{"quote":"the body is capable of everything it is the mind limiting", "author":"goggins "})



input()


resource=requests.get(base+'quotes/1')

print(resource.json())