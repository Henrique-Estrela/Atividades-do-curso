<?php include "head.php"; ?>
<?php include "menu.php"; ?>
<section id="cadastro">
  <div class="wrapper flex_box">
    
    
      <form class="row g-3" method="post" action="_scripts/salvar.php">
              <label for="titulo" class="form-label" id="titulo"><h1>Cadastro de Envio</h1></label>
              <div class="col-md-12">
                  <label for="nome" class="form-label">Nome</label>
                  <input type="text" placeholder="Digite seu Nome" class="form-control caixa" name="nome" id="nome" required>
              </div>
              
              <div class="col-md-12">
                <label for="inputCep" class="form-label">
                  CEP:
                </label>
                <input type="text" name="cep" id="cep" placeholder="Digite seu CEP" onblur="pesquisacep(this.value);"  maxlength="9" class="form-control caixa"  required>
                <a class="ncep" href="https://buscacepinter.correios.com.br/app/endereco/index.php">Não sei meu CEP!</a>
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