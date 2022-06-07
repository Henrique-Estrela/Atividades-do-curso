<?php include "head.php"; ?>
<?php include "menu.php"; ?>
<section id="cadastro">
  <div class="wrapper flex_box">
    <title class="name"><h3>Cadastro de Clientes</h3></title>
    
      <form class="row g-3" method="post" action="_scripts/salvar.php">
              <div class="personal-image">
                <label class="label">
                  <input type="file" />
                  <figure class="personal-figure">
                    <img id="img" src="https://cdn-icons-png.flaticon.com/512/1946/1946429.png">
                    <figcaption class="personal-figcaption">
                      <img src="https://raw.githubusercontent.com/ThiagoLuizNunes/angular-boilerplate/master/src/assets/imgs/camera-white.png">
                    </figcaption>
                  </figure>
                </label>
              </div>
              <div class="col-md-12">
                  <label for="nome" class="form-label">Nome</label>
                  <input type="text" placeholder="Digite seu Nome" class="form-control caixa" name="nome" id="nome" required>
              </div>
              

              <div class="col-md-12">
                <label for="inputCep" class="form-label">
                  CEP:
                </label>
                <input type="text" name="cep" id="cep" placeholder="Digite seu CEP" onblur="pesquisacep(this.value);"  maxlength="9" class="form-control caixa"  required>
              </div>

              <div class="col-md-12">
                <label for="inputRua" class="form-label">Rua:</label>
                <input type="text" placeholder="Digite o nome da Rua" name="rua" id="rua" class="form-control caixa" readonly>
              </div>

              <div class="col-md-12">
                <label for="inputCidade" class="form-label">Cidade:</label>
                <input type="text"placeholder="Digite o nome da sua Cidade" name="cidade" id="cidade" class="form-control caixa" readonly>
              </div>

              <div class="col-md-12">
                <label for="estado" class="form-label">Estado</label>
                <input name="estado" placeholder="Digite o nome do Estado" type="text" class="form-control caixa" required readonly id="estado" size="60" />
              </div>



              <div class=" button_wrapper ">
                <button type="submit">Cadastrar</button>
              </div>





      </form>

      
      

  </div>
  
</section>




<?php include "js.php"; ?>
<?php include "footer.php"; ?>