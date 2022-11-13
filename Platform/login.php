<?php session_start();?>
<?php
$servername = "localhost:3306";
$username = "";
$password = "";
$dbname = "";
$pwd = $_REQUEST['pwd'];
$salt = '';
$hash = $salt . $pwd;
$safe_pwd =hash('sha256', $hash);
$gebruikersnaam = $_REQUEST['gebruikersnaam'];

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT gebruikersnaam, wachtwoord FROM gebruiker WHERE gebruikersnaam='$gebruikersnaam' AND approved='1'";
$result = $conn->query($sql);
$user_data = mysqli_fetch_assoc($result);

if ($user_data['gebruikersnaam'] == $gebruikersnaam && $user_data['wachtwoord'] == $safe_pwd){
		$_SESSION["user"] = $gebruikersnaam;
		echo "<meta http-equiv='refresh' content='0; URL=index.php'/>";
}
?>
<!DOCTYPE html>
<html>
    <head>
		<link rel="stylesheet" href="styles.css">
		<title>Inloggen</title>
    </head>
<div>
  <form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">
            <h1>Log je hier in:</h1>
			<br>
	        <label for="fname">Gebruikersnaam:</label>
            <br><br>
	        <input type="text" id="gebruikersnaam" name="gebruikersnaam"value=<?php $gebruikersnaam;?>>
            <br><br>
	        <label for="lname">Wachtwoord:</label>
            <br><br>
	        <input type="password" id="pwd" name="pwd" value=<?php $pwd;?>>
            <br><br>
	        <input type="submit" value="Submit">
            <br><br>
            <a href="register.php">
                <p>Nog geen login gegevens? Registreer hier.</p>
            </a>
	</form>
</div>
