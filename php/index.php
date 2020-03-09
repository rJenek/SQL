
<head>
<meta charset="utf-8">
<link rel="stylesheet" href="style.css">

</head>
<body> 
<?php 
  if($_COOKIE['user'] == ''):
?>
<div class="form-wrap">
    <div class="profile">
      <h1>Регистрация</h1>
    </div>
    
    <form method="post" action="file.php">
      <div>
        <label for="name">Логин</label>
        <input type="text" name="login" id="login" >
      </div>
      <div class="name">
        <label for="name">Пароль</label>
        <input type="text" name="password" id= "password">
      </div>
      <div>
        <label for="email">E-mail</label>
        <input type="email" name="email" id="email" >
      </div>
      <button type="submit">Регистрация</button> 
    </form> 
  </div>
  <div class="form-wrap">
    <div class="profile">
      <h1>Авторизация</h1>
    </div>
    <form method="post" action="login.php">
      <div>
        <label for="name">Логин</label>
        <input type="text" name="login" id="login" >
      </div>
      <div class="name">
        <label for="name">Пароль</label>
        <input type="text" name="password" id= "password">
      </div>
      <button type="submit">Авторизоваться</button> 
    </form> 
  </div>


  



<?php else: ?>
      <p> Привет <?=$_COOKIE['user']?>. Чтобы выйти нажмите <a href="/exit.php"> здесь</a>. </p>
<?php endif; ?></body>