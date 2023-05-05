from requests import session

url = "https://pdisk.pro/xjy91c1v7er9"

def pdisk(url):
   client = session()
   r = client.get(url).text
   x = r.split("</center>")[-1]
   y = x.split("</script>")[1]
   z = y.split("-->")[0]
   p = z.split("<!-- ")[-1]
   return p
   
print(pdisk(url))
