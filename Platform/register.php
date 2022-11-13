<?php session_start(); ?>
<?php
if($_SERVER['REQUEST_METHOD']=="POST"){
	$pwd =  $_REQUEST['pwd'];
	$gebruikersnaam = $_REQUEST['gebruikersnaam'];
	$salt = '';
	$hash = $salt . $pwd;
	$safe_pwd =hash('sha256', $hash);

	$servername = "localhost:3306";
	$username = "";
	$password = "";
	$dbname = "";

	// Create connection
	$conn = new mysqli($servername, $username, $password, $dbname);
	// Check connection
	if ($conn->connect_error) {
		die("Connection failed: " . $conn->connect_error);
	}
	$sql = "INSERT INTO gebruiker (gebruikersnaam, wachtwoord)
	VALUES ('$gebruikersnaam', '$safe_pwd')";

	if ($conn->query($sql) === TRUE) {
		echo "<script>location.href='login.php';</script>";
	} else {
		echo "Error: " . $sql . "<br>" . $conn->error;
	}

	$conn->close();
}
?>
<!DOCTYPE html>
<html>
    <head>
		<link rel="stylesheet" href="styles.css">
		<title>Registreren</title>
    </head>
<div>
      <form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">
        <h1>Registreer je hier:</h1>
		<br>
        <label for="rol">Gebruikersnaam:</label>
        <br><br>
        <input  required type="text" id="gebruikersnaam" name="gebruikersnaam" value=<?php $gebruikersnaam;?>>
        <br><br>
		<label for="pwd">Wachtwoord:</label>
        <br><br>
        <input required type="password" id="pwd" name="pwd" value=<?php $pwd?>>
        <br><br>
        <input type="submit" value="Submit">
      </form>
</div>