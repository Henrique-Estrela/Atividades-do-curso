<?php

$n1 = $_POST['nota1'];
$n2 = $_POST['nota2'];
$n3 = $_POST['nota3'];
$n4 = $_POST['nota4'];
$n5 = $_POST['nota5'];

$p1 = $_POST['peso1'];
$p2 = $_POST['peso2'];
$p3 = $_POST['peso3'];
$p4 = $_POST['peso4'];
$p5 = $_POST['peso5'];


// function notas($n1,$n2,$n3,$n4,$n5,$p1,$p2,$p3,$p4,$p5){
   
//        $media = ($n1 + $n2 + $n3 + $n4 + $n5) / 5;
//        $maiorN = max($n1,$n2,$n3,$n4,$n5);
//        $menorN = min($n1,$n2,$n3,$n4,$n5);
//        $mediaP = ($n1*$p1 + $n2*$p2 + $n3*$p3 + $n4*$p4 + $n5*$p5) / $p1+$p2+$p3+$p4+$p5;
       
//        return array(number_format($media, 2, '.', ','),$maiorN,$menorN,number_format($mediaP, 2, '.', ','));  
  
// };
         //criado para interface//
function media($n1,$n2,$n3,$n4,$n5){
       $media = ($n1 + $n2 + $n3 + $n4 + $n5) / 5;
       return number_format($media, 2, '.', ',');
}

function maior($n1,$n2,$n3,$n4,$n5){
       $maiorN = max($n1,$n2,$n3,$n4,$n5);
       return $maiorN;
}

function menor($n1,$n2,$n3,$n4,$n5){
       $menorN = min($n1,$n2,$n3,$n4,$n5);
       return $menorN;
}
function mediaP($n1,$n2,$n3,$n4,$n5,$p1,$p2,$p3,$p4,$p5){
       $mediaP = ($n1*$p1 + $n2*$p2 + $n3*$p3 + $n4*$p4 + $n5*$p5) / $p1+$p2+$p3+$p4+$p5;
       return number_format($mediaP, 2, '.', ',');
}


include 'base.php';



?>