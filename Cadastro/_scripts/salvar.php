<html lang="pt-br">
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" type="text/css">
        <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
    </head>
    <body>
    <?php
include "functions.php";
include "config.php";

$nome = $_POST['nome'];
$email = $_POST['email'];
$cpf = $_POST['cpf'];
$cep = $_POST['cep'];
$rua = $_POST['rua'];
$bairro = $_POST['bairro'];
$cidade = $_POST['cidade'];
$estado = $_POST['estado'];
$situacao = $_POST['situacao'];

if(cadastro_contato($email)==0){

  $sql = "INSERT INTO contato (nome,email,cpf,cep,rua,bairro,cidade,estado,situacao) VALUES ('$nome','$email','$cpf','$cep','$rua','$bairro','$cidade','$estado','$situacao')";
  $query = $mysqli->query($sql);
  
  ?>

  <script language='javascript'>
    Swal.fire({
    title: 'Salvo com sucesso meu patrão.',
    width: 600,
    padding: '3em',
    color: '#716add',
    background: '#fff url(/images/trees.png)',
    backdrop: `
      rgba(0,0,123,0.4)
      url("https://i.gifer.com/origin/51/518532f622d962be53e2e1f8989263a8_w200.gif")
      left top
      no-repeat
    `
    }).then((result) => {
      /* Read more about isConfirmed, isDenied below */
      if (result.isConfirmed) {
          window.location.href="../index.php";
      } else{
        window.location.href="../index.php";
      }
      })
  </script>
  <?php } else{?>
  
  <script language='javascript'>
    Swal.fire({
    icon: 'error',
    title: 'Oops...',
    text: 'Amigão, ce já fez o cadastro pae!',
    backdrop: `
      rgba(0,0,123,0.4)
      url("https://i.gifer.com/origin/51/518532f622d962be53e2e1f8989263a8_w200.gif")
      left top
      no-repeat
    `
  
  }).then((result) => {
    /* Read more about isConfirmed, isDenied below */
    if (result.isConfirmed) {
        window.location.href="../index.php";
    }
    })
  
  </script>
  <?php 
  }
?>

    </body>
</html>

