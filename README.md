## Topic : Live chat analytics
### Video Overview : [Youtube](https://youtu.be/OBHS47BvNMQ).
###### Present By : ภูวดล ศรีธรรม 6420422026, ขนิษฐา ปะอันทัง 6420422019
### Dataset
###### Youtube Chanel : MONEY HERO (@moneyheroschool)
###### [หุ้นเด่นรอบวัน ประจำวันที่ 9 มกราคม 2566](https://www.youtube.com/watch?v=T54j0ujWN9o&t=341s).
###### [หุ้นเด่นรอบวัน ประจำวันที่ 10 มกราคม 2566](https://www.youtube.com/watch?v=brE8_gE014w&t=11s).
###### [หุ้นเด่นรอบวัน ประจำวันที่ 11 มกราคม 2566](https://www.youtube.com/watch?v=BiFSgJThu_c&t=96s).
###### [หุ้นเด่นรอบวัน ประจำวันที่ 12 มกราคม 2566](https://www.youtube.com/watch?v=RWKLlk9g3ss&t=16s).
###### [หุ้นเด่นรอบวัน ประจำวันที่ 13 มกราคม 2566](https://www.youtube.com/watch?v=cAqJiaSUw2Y&t=125s).
### Library
```python
import csv
import pandas as pd
import pymongo
import pytchat
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import dash
from dash import Input, Output, dcc, html, dash_table, Dash 
import plotly.graph_objs as go
import plotly.express as px
import dash_bootstrap_components as dbc
```

### Analytics Process
######   1.  Run file YoutubeLive.py เพื่อดึงข้อมูลจาก live chat บน youtube เก็บข้อมูลลง MongoDB
```command
python YoutubeLive.py
```
![image](https://user-images.githubusercontent.com/114323892/212961248-a4003bed-bee7-4ad6-8d83-8e25d8e83a5e.png)

######   2.  Run file YoutubeAnalytics.py เพื่อดึงรายชื่อหุ้นออกจาก text message แล้วทำการ count จำนวนชื่อหุ้นที่เกิดขึ้นเก็บใน MongoDB
```command
python YoutubeAnalytics.py
```

######   3.  Run file main.py เพื่อแสดงหน้า web app ดูการ plot grahp ในมิติต่าง ๆ
```command
python main.py
```
- ตัวอย่างการแสดงผล
  - วิเคราะห์หุ้นที่ได้รับความสนใจหรือถูกพูดถึงมากที่ในการ live ช่วงวันที่ 9-13 ม.ค. 66 จัดเรียงด้วย bar graph 10 อันดับ

![image](https://user-images.githubusercontent.com/114323892/212961962-527c2500-98f9-46f5-a8e9-0f33bf6568c2.png)

- วิเคราะห์หุ้นที่ถูกพูดถึงทุกตัวจากการ live ช่วงวันที่ 9-13 ม.ค. 66 จัดเรียงด้วย bar graph 
![image](https://user-images.githubusercontent.com/114323892/212963550-2e9b4bf2-f4f2-4866-b9d6-229719737cdf.png)

- วิเคราะห์ติดตาม live และจำนวนคนดู ณ ขณะ live ช่วงวันที่ 9-13 ม.ค. 66 จัดเรียงด้วย bar graph 
![image](https://user-images.githubusercontent.com/114323892/212964065-f680e173-560b-42f5-8415-fb12393f7118.png)

- วิเคราะห์คนดู ที่มีการเข้าชมมากที่สุดขณะ live ช่วงวันที่ 9-13 ม.ค. 66 จัดเรียงด้วย bar graph 
![image](https://user-images.githubusercontent.com/114323892/212964403-31a103d0-5fd5-4a4c-a6fe-5f29335739bd.png)


