<?php
define("DB_SERVER", "localhost");
define("DB_USERNAME", "aquaponics");
define("DB_PASSWORD", "somepassword1");
define("DB_DATABASE", "sensors");
$db = mysqli_connect(DB_SERVER,DB_USERNAME,DB_PASSWORD,DB_DATABASE);
?>
