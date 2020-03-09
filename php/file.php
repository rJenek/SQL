<?php

$login= filter_var(trim($_POST['login']),
FILTER_SANITIZE_SPECIAL_CHARS,FILTER_SANITIZE_STRING); // присваивает значение переменной полученной из index.html и фильрует спец символы
$password= filter_var(trim($_POST['password']),
FILTER_SANITIZE_SPECIAL_CHARS,FILTER_SANITIZE_STRING);
$email= filter_var(trim($_POST['email']),
FILTER_SANITIZE_EMAIL,FILTER_SANITIZE_STRING);

if(mb_strlen($login) < 5 || mb_strlen($login > 90)){ //проверка длины логина
    echo"Недопустимая длина логина";
    exit();
} else if(mb_strlen($password) < 8) { //проверка длины пароля
    echo"Пароль слишком короткий";
    exit();
} 
$password = md5($password."olfkrtiucopsk345ltopsi40"); //хеширование пароля

$mysql = new mysqli('localhost', 'root', 'root', 'user');
$mysql->query("INSERT INTO `users` (`login`, `password`, `email`) 
VALUES('$login', '$password', '$email')");

$mysql->close();

header('location: /');


?>