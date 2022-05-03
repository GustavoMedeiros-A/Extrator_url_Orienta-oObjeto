# https://www.bytebank.com.br/cambio
import re


# Nesse caso, usa-se parênteses para dizer que é necessário que o padrão seja exatamente esse, exatamente nesse ordem

url = "www.bytebank.com.br/cambio"
padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padrao_url.match(url)

if not match:
    raise ValueError("The url is not valid")

print("The url is valid")