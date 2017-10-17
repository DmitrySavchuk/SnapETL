SnapETL:
���� ������ ��������� � ���������� SnapETL � ������� �� ���� ������: ��������������� ETL � data access API. 
ETL ��������� � ��������������� ����������, � API ������������ � ���� Flask end-point application, ������������� � ���������� End_point_API.
ETL
��������������� ��� ETL, ��� � �����������, ������� �� 3 ������:
1. Crawler
2. Extractor
3. Loader
Crawler
Crawler ��������� ��� ����������, ������� ��� ������ � �������, ������ � ��� ���������� � ������ �� ���������� �������. 
���� ����������� react.js � ��� ������������� ����� �������, ��� �������� html-response � ����������� � ��������� ���� ������ �������������. ������ �� ���� ������� � ����� ������� api, ������� �� ������� �� https://www.snap.com/api/jobs/ ����� json � ����������� ��� ���� ���������. � ����� ��� ������� ����� �������, ��� ��� �������� ������������� ������� � �������� html. ����� ����������� � ������� input-output ��������, � ��� ����� ���������, �������� ���� Crawler.py �� ��������� � ������� ��� ������ ���������� url, � ������ -- ����, � ������� ����� �������� �����. ��� ��������� ������ ������������ ���������� requests.
Input
python Crawler.py https://www.snap.com/api/jobs/ snap.html
Output
snap.html
Extractor
Extractor ��������� ���������� � input-output � ������������ � ��������. ��� �������������� json � ������� ������������ ������ json. ����� ���������� � ������ ������ �������� �� ������� � ������ ����� � ������������ � csv-����.
Input
python Extractor.py snap.html snap.csv
Output
snap.csv
Loader
� �������� �� ������������ SQLite, � ��� ������� � ��� ������������ ���������� ������ sqlite3.
Input
python Loader.py snap.csv
Output
a database store with jobs records
����� ���� ������ ������� � ����������� �������.
ETL.py
������� ������, ��������������� ����������� ��� ������ � ���������� �� ���������. ����������� �� ���������:
Input
python ETL.py https://www.snap.com/api/jobs/ snap.html snap.scv
Output
a database store with jobs records
End-point API
����������� �� flask.
Input
http://127.0.0.1:5000/jobs/London
Output
Clear jobs records fir this location, without html


