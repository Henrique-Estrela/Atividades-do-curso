<?php include "head.php"; ?>

<div class="wrapper flex_box">
    <form>
     <hr><label for="resultado" class="text-center"><h1>Resultado!</h1></label><hr><br>

     <label for="resultado" class="text-center"><h2>Sua media:</h2><br></label>
     <h2 class="text-center"><?php print_r(media($n1,$n2,$n3,$n4,$n5));?></h2>

     <label for="resultado" class="text-center"><h2>Sua media ponderada:</h2></label>
     <h2 class="text-center"><?php print_r(mediaP($n1,$n2,$n3,$n4,$n5,$p1,$p2,$p3,$p4,$p5));?></h2>

     <label for="resultado" class="text-center"><h2>Sua maior media:</h2></label>
     <h2 class="text-center"><?php print_r(maior($n1,$n2,$n3,$n4,$n5));?></h2>

     <label for="resultado" class="text-center"><h2>Sua menor media:</h2></label>
     <h2 class="text-center"><?php print_r(menor($n1,$n2,$n3,$n4,$n5));?></h2>

    </form>
  </div>
  
  <div class="back">
        <button type="button" value="Voltar" onclick="history.go(-1)">Voltar</button>
  </div>

  

  <div class="sign">
    by Henrique <a>Estrela</a>
  </div>

  


<?php include "js.php"; ?>
<?php include "footer.php"; ?>



