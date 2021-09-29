from bs4 import BeautifulSoup

html_doc = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DENEME</title>
</head>
<body>
  <h1 id="header">
        Python
    </h1>

    <div class="group1">
        <h2>
            Programming
        </h2>

      <ul>
                <li>Menu1</li>
            <li>Menu2</li>
            <li>Menu3</li>
        </ul>

    </div>

    <div class="group2">
        <h2>
            Moduls
        </h2>

        <ol>
            <li>Menu1</li>
            <li>Menu2</li>
            <li>Menu3</li>
        </ol>
    </div>
</body>
</html>
'''

soup = BeautifulSoup(html_doc, "html.parser")

result = soup.prettify()
result = soup.title

result = soup.title.name
result = soup.title.string

result = soup.h1
result = soup.h1.name
result = soup.h1.string
result = soup.h2

result = soup.find_all('h2')
result = soup.find_all('h2')[1]

result = soup.find_all("div")[1].ol.find_all('li')[2].string

result = soup.div.findChildren()

print(result)

