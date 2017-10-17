SnapETL:
Весь проект находится в директории SnapETL и состоит из двух частей: непосредственно ETL и data access API. 
ETL находится в соответствующей директории, а API представлено в виде Flask end-point application, содержащегося в директории End_point_API.

ETL
Непосредственно сам ETL, как и требовалось, состоит из 3 частей:
1. Crawler
2. Extractor
3. Loader
Crawler
Crawler выполняет тот функционал, который был описан в задании, однако в его реализации я отошел от требований задания. 
Сайт использовал react.js и был спроектирован таким образом, что получить html-response с информацией о вакансиях было весьма проблематично. Видимо по этой причине у сайта имеется api, которое по запросу на https://www.snap.com/api/jobs/ отдаёт json с информацией обо всех вакансиях. Я нашел это гораздо более удобным, так как отпадала необходимость парсить и получать html. Также определённый в задании input-output работает, в чем можно убедиться, запустив файл Crawler.py из терминала и передав ему первым аргументом url, а вторым -- файл, в который будет сохранен ответ. Для получения ответа используется библиотека requests.
Input
python Crawler.py https://www.snap.com/api/jobs/ snap.html
Output
snap.html
Extractor
Extractor реализует функционал и input-output в соответствии с заданием. Для преобразования json в словарь используется модуль json. Затем информация о работе просто достаётся из словаря в список строк и записывается в csv-файл.
Input
python Extractor.py snap.html snap.csv
Output
snap.csv
Loader
В качестве БД используется SQLite, а для доступа к ней используется встроенный модуль sqlite3.
Input
python Loader.py snap.csv
Output
a database store with jobs records
Схема базы данных имеется в репозитории проекта.
ETL.py
Главный скрипт, последовательно запускающий три модуля и передающий им аргументы. Запускается из терминала:
Input
python ETL.py https://www.snap.com/api/jobs/ snap.html snap.scv
Output
a database store with jobs records

End-point API
Реализовано на flask.
Input
http://127.0.0.1:5000/jobs/London
Output
Clear jobs records fir this location, without html


