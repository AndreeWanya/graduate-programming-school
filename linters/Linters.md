##### Линтеры
###### Код из раздела "Обработка изображений"
![](https://github.com/AndreeWanya/graduate-programming-school/blob/master/linters/1.png)  
Pylint не нашел ошибок, но нашел 7 предупреждений (warnings) и 4 нарушения договора оформления кода (conventions):  
![](https://github.com/AndreeWanya/graduate-programming-school/blob/master/linters/2.png)  
Pylint рассматривает наш код как модуль, а согласно PEP8 в начале модуля нужно дать его описание (docstring). Также имя модуля должно соответствовать стилю snake_case:  
![](https://github.com/AndreeWanya/graduate-programming-school/blob/master/linters/3.png)  
На следующем скриншоте из библиотеки Pillow мы импортируем три модуля: Image, ImageDraw, ImageColor. Однако в коде используется только первый модуль, модули ImageDraw и ImageColor не используются:  
![](https://github.com/AndreeWanya/graduate-programming-school/blob/master/linters/4.png)  
Согласно PEP8 сразу за объявлением функции или метода должна следовать строка с описанием этой функции или метода:  
![](https://github.com/AndreeWanya/graduate-programming-school/blob/master/linters/5.png)  
В объявлении цикла Pylint нашел две переменные, которые дальше в коде не используются:  
![](https://github.com/AndreeWanya/graduate-programming-school/blob/master/linters/6.png)  
![](https://github.com/AndreeWanya/graduate-programming-school/blob/master/linters/7.png)  
Согласно PEP8 перед объявлением функции или метода нужно оставить 2 пустые строки:
![](https://github.com/AndreeWanya/graduate-programming-school/blob/master/linters/9.png)
