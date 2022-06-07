<?php include "head.php"; ?>
<?php include "menu.php"; ?>

<div class="wrapper flex_box">
    <form method="post" action="salvar.php">
        <label for="Matematica" class="text-center"><h4>Matematica</h4></label>
        <div class="flex-container">
            <div class="input">
                <label>
                Primeira nota:
                </label>
                <input class="name" placeholder="Digita a nota" type="number" name="nota1" required>
            </div>

            <div class="input">
                <label>
                peso:
                </label>
                <input placeholder="Digite o peso" class="name" type="number" name="peso1" required>
            </div>
        </div>

        <label for="Geografia" class="text-center"><h4>Geografia</h4></label>       
        <div class="flex-container">
            <div class="input">
                <label>
                Segunda nota:
                </label>
                <input class="name" placeholder="Digita a nota" type="number" name="nota2">
            </div>

            <div class="input">
                <label>
                peso:
                </label>
                <input placeholder="Digite o peso" class="name" type="number" name="peso2">
            </div>
        </div>

        <label for="Historia" class="text-center"><h4>Historia</h4></label>
        <div class="flex-container">
            <div class="input">
                <label>
                Terceira nota:
                </label>
                <input class="name" placeholder="Digita a nota" type="number" name="nota3">
            </div>

            <div class="input">
                <label>
                peso:
                </label>
                <input placeholder="Digite o peso" class="name" type="number" name="peso3">
            </div>
        </div>

        
        


      <div class="button_wrapper">
        <button type="submit">
          Enviar
        </button>
      </div>
     


    </form>
</div>
  
  

  <div class="sign">
    by Henrique <a>Estrela</a>
  </div>

<?php include "js.php"; ?>
<?php include "footer.php"; ?>