# Super-Heroes Rest API

---

>This project is a rest API about super-heroes, it is written in Python with the Django framework and consumes the Marvel official API to get the names and information of the 1,561 super-heroes registered in Marvel's database.  
>
>This Rest API has two endpoints, one is just a hello-world message and the other one returns an aleatory super-hero:
>
>- http://localhost:8000/heroes-api/hello-world/  
>This endpoint returns a JSON object that has the text "Hello World!!" with the following fields:
>    * id
>    * text
>
>- http://localhost:8000/heroes-api/random-hero/  
>This endpoint consumes the Marvel API, gets randomly one of the 1,561 super-heroes, and returns a JSON object that has the relevant information of this super-hero with the following fields:
>    *  id
>    * name
>    * description
>    * pictureURL
>    * copyright

---

> ### How to run this project
>
> 1. Clone this Git repository
> 2. Install Python3 and all the necessary libraries in a clean environment (the libraries are listed in the next section)
> 3. Run in the main folder of this repository with your command line the command: `py manage.py runserver`
> 4. Access to the endpoints with your preferred web browser

---

> ### Libraries needed
>
>This project uses the Django framework (v4.0.4) for Python (v3.10.2) with the following libraries:
>
> - asgiref v3.5.0
> - certifi v2021.10.8
> - charset-normalizer v2.0.12
> - Django v4.0.4
> - idna v3.3
> - requests v2.27.1
> - sqlparse v0.4.2
> - tzdata v2022.1
> - urllib3 v1.26.9

---
