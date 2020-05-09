from flask import Flask
from flask import render_template
from random import choice


app = Flask(__name__)


# главное окно сайта
@app.route('/')
@app.route('/main')
def main():
    return """<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Главная</title>
    <style>
      a {
       color: #000000
       }

      .thumb img  {
       border: 2px solid #ffbdd3; /* Рамка вокруг фотографии */
       padding: 0px; 
       margin-right: 15px; /* Отступ справа */
       margin-bottom: 15px; /* Отступ снизу */
       }

      figcaption { 
       text-align: center;
       max-width: 350px;
       }

      .layer2 {
       padding-left: 100%;
      }

      .layer2 {
       padding-left: 100%;
      }

      .layer3 {
       padding-left: 100%;
      }
      #left { position: absolute; left: 0; top: 15%; width: 20%; }
      #right { position: absolute; right: 0; top: 15%; width: 80%; }

    </style>
  </head>

  <body>
    <big><big><center><h1><b>BioWikki</b></h1></center></big></big>  
    <hr></hr> 

    <div id="left">
      <center><h2>Разделы:</h2></center>
      <ul id="navbar">
        <li><a href="registration">Вход/Регистрация</a></li>
        <li><a href="main">Главная</a></li>
        <li><a href="random">О животном</a></li>
        <li><a href="random_fact">Факты</a></li>
        <li><a href="tests">Тестик</a></li>
      </ul>
    </div>

    <div id="right"> 
      <center><h1><b>Главная</b></h1></center>
      <center><h2>Животные Красной Книги:</h2></center>
      <div class="thumb"> 
        <img src="static/img/Белый медведь.png" alt="упсcc..." width="350" height="250" title="Белый медведь">
        <img src="static/img/сивуч.jpg" alt="упсcc..." width="350" height="250" title="Сивуч">
        <img src="static/img/Розовый фламинго.jpg" alt="упсcc..." width="350" height="250" title="Розовый фламинго">
        <img src="static/img/Кондор.jpg" alt="упсcc..." width="350" height="250" title="Кондор">
        <img src="static/img/Северный гладкий кит.jpg" alt="упсcc..." width="350" height="250" title="Северный гладкий кит">
        <img src="static/img/Гренландский кит.jpg" alt="упсcc..." width="350" height="250" title="Гренландский кит">
        <img src="static/img/Ararajuba.jpg" alt="упсcc..." width="350" height="250" title="Ararajuba">
        <img src="static/img/Желтая хвостатая обезьяна.jpg" alt="упсcc..." width="350" height="250" title="Желтая хвостатая обезьяна">
        <img src="static/img/Южный туко-туко.jpg" alt="упсcc..." width="350" height="250" title="Южный туко-туко">
        <img src="static/img/Красный волк.jpg" alt="упсcc..." width="350" height="250" title="Красный волк">
        <img src="static/img/Белый лев.jpg" alt="упсcc..." width="350" height="250" title="Белый лев">
        <img src="static/img/Белая цапля.jpg" alt="упсcc..." width="350" height="250" title="Белая цапля">
        <img src="static/img/Соня-полчок.jpg" alt="упсcc..." width="350" height="250" title="Соня-полчок">
        <img src="static/img/Снежный барс.jpg" alt="упсcc..." width="350" height="250" title="Снежный барс">
        <img src="static/img/Филин.jpg" alt="упсcc..." width="350" height="250" title="Филин">
        <img src="static/img/Белка летяга.jpg" alt="упсcc..." width="350" height="250" title="Белка летяга">
        <img src="static/img/Ринопитек.jpg" alt="упсcc..." width="350" height="250" title="Ринопитек">
        <img src="static/img/Кабарага.jpg" alt="упсcc..." width="350" height="250" title="Кабарага">
        <img src="static/img/Индийская гигантская белка.jpg" alt="упсcc..." width="350" height="250" title="Индийская гигантская белка">
        <img src="static/img/Манул.jpg" alt="упсcc..." width="350" height="250" title="Манул">
        <img src="static/img/Удода.jpg" alt="упсcc..." width="350" height="250" title="Удода">
        <img src="static/img/Ангорский кролик.jpg" alt="упсcc..." width="350" height="250" title="Ангорский кролик">
        <img src="static/img/Сенегальские галаго.jpg" alt="упсcc..." width="350" height="250" title="Сенегальские галаго">
        <img src="static/img/Малоротая макропинна (Бочкоглаз).jpg" alt="упсcc..." width="350" height="250" title="Малоротая макропинна (Бочкоглаз)">
        <img src="static/img/Бархатный кот.jpg" alt="упсcc..." width="350" height="250" title="Бархатный кот">
        <img src="static/img/Глубоководный удильщик.jpg" alt="упсcc..." width="350" height="250" title="Глубоководный удильщик">
        <img src="static/img/Медоед.jpg" alt="упсcc..." width="350" height="250" title="Медоед">
        <img src="static/img/Пятнистохвостая сумчатая куница.jpg" alt="упсcc..." width="350" height="250" title="Пятнистохвостая сумчатая куница">
        
      </div>
    </div>

  </body>
</html>"""


# окно с фактами
@app.route('/random_fact')
def random_fact():
    # животные?, которые появятся в фактах
    names = ["белый медведь", "фламинго", "филин", "Удода", "сивуч", "манул", "кондор", 'Бархатный кот', 'Белая цапля',
             'Белый лев', 'Желтая обезьяна', 'Чёрный носорог']
    # выбор животного
    a = choice(names) + ".html"
    return render_template(a)


# инфа
@app.route('/random')
def random_dinosaur():
    # животные, которые  будут в разделеЖ о животном
    names = ["Ангорский Кролик", "Белка Летяга", 'Медоед', 'Галаго', 'Гренландский кит', 'Кабарга', 'Куница',
             'Красный волк', "Антлантический морж", "Белый носорог", 'Снежный барс', 'Соня-полчок']
    # выбор животного
    a = choice(names) + "_и.html"
    return render_template(a)


# окно с тестом
@app.route('/tests')
def tests():
    return """<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Главная</title>
    <style>
      a {
       color: #000000
       }

      #left { position: absolute; left: 0; top: 15%; width: 20%; }
      #right { position: absolute; right: 0; top: 15%; width: 80%; }

    </style>
  </head>

  <body>
    <big><big><center><h1><b>BioWikki</b></h1></center></big></big>
    <hr></hr> 

    <div id="left"> 
      <center><h2>Разделы:</h2></center>
      <ul id="navbar">
        <li><a href="registration">Вход/Регистрация</a></li>
        <li><a href="main">Главная</a></li>
        <li><a href="random">О животном</a></li>
        <li><a href="random_fact">Факты</a></li>
        <li><a href="tests">Тестик</a></li>
      </ul>
    </div>

    <div id="right"> 
      <center><h1><b>Тестик</b></h1></center>
      <p>Выполняем тестик, для проверки вашего уровня, знания животных из Красной Книги:</p>
<p>Эта птица занесена в Красную книгу. Это семейство включает 62 вида. Длина 40 см, в брачный период на голове появляется ярко-рыжий хохолок. Питается рыбой, насекомыми. Может даже сидеть на спинах домашних животных. Жила в Египте? <input type="text" id="t"></p>
<p>Листья падают с осин,
Мчится в небе острый клин. Это?! <input type="text" id="t2"></p>
<p>Вот так птица - какова!
И не спутаешь с другой,
Может это цифра два,
Шея выгнута дугой. <input type="text" id="t3"></p>
<p>Эта наука изучает организмы и окружающую среду? <input type="text" id="t4"></p>
<button onclick="proverit();">Проверить</button>
<div id="rezultat"></div>
<script>
function proverit(){
pr_otv_zadachi_1 = "Египетская цапля";
pr_otv_zadachi_2 = "Журавль";
pr_otv_zadachi_3 = "Лебедь";
pr_otv_zadachi_4 = "Экология";
otv_uch_1 = document.getElementById('t').value;
otv_uch_2 = document.getElementById('t2').value;
otv_uch_3 = document.getElementById('t3').value;
otv_uch_4 = document.getElementById('t4').value;
ball = 0;
if(otv_uch_1 == pr_otv_zadachi_1){
ball +=1;
}
if(otv_uch_2 == pr_otv_zadachi_2){
ball +=1;
}
if(otv_uch_3 == pr_otv_zadachi_3){
ball +=1;
}
if(otv_uch_4 == pr_otv_zadachi_4){
ball +=1;
}
vsego_zadach = 4;
procent_vip = ball/vsego_zadach * 100;
document.getElementById('rezultat').innerHTML = "Ответы верные на "+procent_vip+"%.";
}
</script>
      
    </div>

  </body>
</html>"""


# окно регистрации
@app.route('/registration')
def registration():
    return """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Главная</title>
  <style>
      a {
       color: #000000
       }

      #left { position: absolute; left: 0; top: 15%; width: 20%; }
      #right { position: absolute; right: 0; top: 15%; width: 80%; }

body {
    font-family: Arial, Helvetica, sans-serif;
    background-color: white;} {
    font-family: Arial, Helvetica, sans-serif;
    background-color: black;}

* {
    box-sizing: border-box;}

.container {
    padding: 16px;
    background-color: white;}

input[type=text], input[type=password] {
    width: 100%;
    padding: 15px;
    margin: 5px 0 22px 0;
    display: inline-block;
    border: none;
    background: #a8a8a8;}

input[type=text]:focus, input[type=password]:focus {
    background-color: #ddd;
    outline: none;}

hr {
    border: 1px solid #a8a8a8;
    margin-bottom: 25px;}

.registerbtn {
    background-color: #9400d3;
    color: white;
    padding: 16px 20px;
    margin: 8px 0;
    border: none;
    cursor: pointer;
    width: 100%;
    opacity: 0.9;}

.registerbtn:hover {
    opacity: 1;}

a { 
      color: #000000
}
d {
       color: #8affff
}

.signin {
    background-color: #a8a8a8;
    text-align: center;}
</style>
</head>
<body>
<big><big><center><h1><b>BioWikki</b></h1></center></big></big>
    <hr></hr>

    <div id="left">
      <center><h2>Разделы:</h2></center>
      <ul id="navbar">
        <li><a href="registration">Вход/Регистрация</a></li>
        <li><a href="main">Главная</a></li>
        <li><a href="random">О животном</a></li>
        <li><a href="random_fact">Факты</a></li>
        <li><a href="tests">Тестик</a></li>
      </ul>
    </div>

    <div id="right">
<form action="/action.py" method="GET">
  <div class="container">
    <h1>Регистрация</h1>
    <p>Заполните все эти поля чтобы создать аккаунт.</p>
    <hr>

    <label for="email"><b>Email</b></label>
    <input type="text" placeholder="Введите Email" name="email" required>

    <label for="psw"><b>Password</b></label>
    <input type="password" placeholder="Введите пароль" name="psw" required>

    <label for="psw-repeat"><b>Repeat Password</b></label>
    <input type="password" placeholder="Повторите пароль" name="psw-repeat" required>
    <hr>
    <p>Создавая аккаунт вы соглашаетесь с нашими <d href="polite">Условиями и Конфиденциальностью</d>.</p>

    <button type="submit" class="registerbtn">Зарегистрироваться</button>
  </div>

  <div class="container signin">
    <p>Уже есть аккаунт? <d href="enter">Вход</d>.</p>
  </div>
</form>
    </div>
</body>
</html>

"""


# окно входа
@app.route('/enter')
def enter():
    return """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Главная</title>
  <style>
      a {
       color: #000000
       }

      #left { position: absolute; left: 0; top: 15%; width: 20%; }
      #right { position: absolute; right: 0; top: 15%; width: 80%; }

body {
    font-family: Arial, Helvetica, sans-serif;
    background-color: white;}

* {
    box-sizing: border-box;}

.container {
    padding: 16px;
    background-color: white;}

input[type=text], input[type=password] {
    width: 100%;
    padding: 15px;
    margin: 5px 0 22px 0;
    display: inline-block;
    border: none;
    background: #a8a8a8;}

input[type=text]:focus, input[type=password]:focus {
    background-color: #ddd;
    outline: none;}

hr {
    border: 1px solid #a8a8a8;
    margin-bottom: 25px;}

.registerbtn {
    background-color: #9400d3;
    color: white;
    padding: 16px 20px;
    margin: 8px 0;
    border: none;
    cursor: pointer;
    width: 100%;
    opacity: 0.9;}

.registerbtn:hover {
    opacity: 1;}

a { 
      color: #000000
}
d {
       color: #8affff
}

.signin {
    background-color: #a8a8a8;
    text-align: center;}
</style>
</head>
<body>
<big><big><center><h1><b>BioWikki</b></h1></center></big></big>
    <hr></hr>

    <div id="left">
      <center><h2>Разделы:</h2></center>
      <ul id="navbar">
        <li><a href="registration">Вход/Регистрация</a></li>
        <li><a href="main">Главная</a></li>
        <li><a href="random_dinosaur">Случайное Животные</a></li>
        <li><a href="random_fact">Рандомный факт</a></li>
        <li><a href="tests">Тестик</a></li>
      </ul>
    </div>

    <div id="right">

<form action="/action_page.php">
  <div class="container">
    <h1>Вход</h1>
    <p>Заполните все эти поля чтобы войти в аккаунт.</p>
    <hr>

    <label for="email"><b>Email</b></label>
    <input type="text" placeholder="Введите Email" name="email" required>

    <label for="psw"><b>Password</b></label>
    <input type="password" placeholder="Введите пароль" name="psw" required>

    <hr>

    <button type="submit" class="registerbtn">Войти</button>
  </div>

  <div class="container signin">
    <p>Еще нет аккаунта? <d href="registration">Регистрация</d>.</p>
  </div>
</form>
    </div>>

</body>
</html>

"""


# окно политики конфедициальности
@app.route('/polite')
def polite():
    return """<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Главная</title>
    <style>
      a { 
      color: #000000
      }
      d {
       color: #8affff
       }

      #left { position: absolute; left: 0; top: 15%; width: 20%; }
      #right { position: absolute; right: 0; top: 15%; width: 80%; }

    </style>
  </head>

  <body>
    <big><big><center><h1><b>BioWikki</b></h1></center></big></big>
    <hr></hr> 

    <div id="left"> 
      <center><h2>Разделы:</h2></center>
      <ul id="navbar">
        <li><a href="registration">Вход/Регистрация</a></li>
        <li><a href="main">Главная</a></li>
        <li><a href="random">О животном</a></li>
        <li><a href="random_fact">Факты</a></li>
        <li><a href="tests">Тестик</a></li>
      </ul>
    </div>


    </div>>

  </body>
</html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
