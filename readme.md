**Формулировка задачи:**

У нас есть правильный кубик и неправильный кубик, в котором смещен центр тяжести и грани 3 и 4 выпадают с 
вероятностями ![frac](http://latex.codecogs.com/gif.latex?%5Cfrac%7B1%7D%7B3%7D), а все остальные с вероятностями 
![frac](http://latex.codecogs.com/gif.latex?%5Cfrac%7B1%7D%7B12%7D). 
Пусть ![xi](http://latex.codecogs.com/gif.latex?%5Cxi) - ДСВ, которая соответствует числу, выпавшему на грани первого 
кубика, а ![mu](http://latex.codecogs.com/gif.latex?%5Cmu) - на втором кубике.

Запустив программу, написанную на Python 3.6 вы узнаете:

- медиану ![equation](http://latex.codecogs.com/gif.latex?%5Ctheta%20%3D%20%5Cxi%5E%5Cmu%20-%20%5Cmu%5E%5Cxi);
- среднеквадратичное отклонение ![theta](http://latex.codecogs.com/gif.latex?%5Ctheta);
- ковариацию и корреляцию ![equation](http://latex.codecogs.com/gif.latex?%20%5Cxi%5E%5Cmu%20-%20%5Cmu%5E%5Cxi) и ![equation](http://latex.codecogs.com/gif.latex?min%282%5E%7B%5Cxi%7D%2C%20%5Cmu%29). 

Перед запуском:

`pip install -r requirements.txt`

Чтобы запустить:

1.1:
`python first_task.py` *медиана и среднеквадратичное отклонение*

1.2:
`python part_two.py` *ковариация и корреляция*

