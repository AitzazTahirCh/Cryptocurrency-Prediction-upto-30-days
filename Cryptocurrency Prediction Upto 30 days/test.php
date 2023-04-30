<?php
$output = '';
session_start();
if(isset($_SESSION['user_id']))
{
$user_id = $_SESSION['user_id'];
if(isset($_POST['result'])){
    $command = escapeshellcmd('python index.py "');
    $output = shell_exec($command);
    echo "<img src='foo.png' >";
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>python</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">
<title>Portal</title>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <a class="navbar-brand">BTC</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="home.php">Home</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="predict.php">Predict</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="test.php">Test</a>
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="login.php">Log out<span class="sr-only"></span></a>
      </li>
    </ul>
  </div>
</nav>
    <center>
        <form method="POST">
            <label>Test:</label>
            <input class="w-100 btn btn-lg btn-primary" type="submit" name="result">
        </form>
    </center>
</body>
</html>
<?php
}
?>