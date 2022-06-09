<?php
$servidor = 'localhost';
$usuario = 'root';
$senha = '';
// $banco = '';criar banco

// String de conexão
$mysqli = new mysqli($servidor, $usuario, $senha, $banco);
if(mysqli_connect_errno()) trigger_error(mysqli_connect_error());
 
?>