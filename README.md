# Resulta

the api access as I understood it as 1 link with all data in the given range of dates:
 - I tried an async approach to using the 2 api calls to my advantage but since I have not done it via python I just did 2 synchronous calls which is a lot slower. I have left the code I tried to use but I didn't understand properly how to use it.
 - I used 1 view for the api and a helper to find data in the other dict
 

## Use
```python
pip install requirements.txt
py manage.py runserver 5000
```

example address: api/scoreboard/NFL/<YYYY-MM-DD>/<YYYY-MM-DD>.json?api_key=74db8efa2a6db279393b433d97c2bc843f8e32b0
