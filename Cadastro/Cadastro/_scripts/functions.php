<?php
  function cadastro_contato($email){
    include "config.php";
    $sql = "SELECT email FROM contato WHERE email='$email'";
    $query = $mysqli->query($sql);
    $total = mysqli_num_rows($query);
    return $total;
  }
?>