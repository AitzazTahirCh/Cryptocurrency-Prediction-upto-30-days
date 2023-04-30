<?php
$output = '';
session_start();
if(isset($_SESSION['user_id']))
{
$user_id = $_SESSION['user_id'];
if(isset($_POST['result'])){
    $a = $_POST['typ'];
    $command = escapeshellcmd('python index.py "');
    $output = shell_exec($command);
    //echo $output;
    
    //$retrieved_data=file_get_contents("readme.txt");
    $array = file("readme.txt");

    //echo $retrieved_data;
    //echo gettype($array);
        $i = 0;
        $j = 1;
        while ($i < $a)
        {
            echo "Prediction for day ".$j." : ".$array[$i]."<br />";
            $i++;
            $j++;
        }   
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
            <label>Choose number of days</label>
            <select class="form-select" name="typ">
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
            <option value="6">6</option>
            <option value="7">7</option>
            <option value="8">8</option>
            <option value="9">9</option>
            <option value="11">11</option>
            <option value="12">12</option>
            <option value="13">13</option>
            <option value="14">14</option>
            <option value="15">15</option>
            <option value="16">16</option>
            <option value="17">17</option>
            <option value="18">18</option>
            <option value="19">19</option>
            <option value="20">20</option>
            <option value="21">21</option>
            <option value="22">22</option>
            <option value="23">23</option>
            <option value="24">24</option>
            <option value="25">25</option>
            <option value="26">26</option>
            <option value="27">27</option>
            <option value="28">28</option>
            <option value="29">29</option>
            <option value="30">30</option>
            </select><br>
            <input class="w-100 btn btn-lg btn-primary" type="submit" name="result">
        </form>
    </center>
</body>
</html>
<?php
}
?>