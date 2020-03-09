<?php

$login= filter_var(trim($_POST['login']),
FILTER_SANITIZE_SPECIAL_CHARS,FILTER_SANITIZE_STRING); // присваивает значение переменной полученной из index.html и фильрует спец символы
$password= filter_var(trim($_POST['password']),
FILTER_SANITIZE_SPECIAL_CHARS,FILTER_SANITIZE_STRING);





$password = md5($password."olfkrtiucopsk345ltopsi40"); //хеширование пароля

$mysql = new mysqli('localhost', 'root', 'root', 'user');
$result = $mysql->query("SELECT * FROM `users` WHERE `login` = '$login' AND `password` = '$password'");
$user = $result->fetch_assoc();
if(count($user) == 0){
    echo "Логин или пароль неправильный";
    echo($result);
    print_r($user);
    exit();
} 
setcookie('user', $user['login'], time() + 3600, "/"); // куки 


$mysql->close();

header('location: /');

?>