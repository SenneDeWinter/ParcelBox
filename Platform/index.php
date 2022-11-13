<?php session_start(); ?>
<?php
if (!isset($_SESSION["user"])){
  echo "<meta http-equiv='refresh' content='0; URL=login.php'/>";
}
?>
<?php
if($_SERVER['REQUEST_METHOD']=="POST"){
	$provider = $_REQUEST['provider'];
	$barcode = $_REQUEST['barcode'];

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
	$sql = "INSERT INTO parcels (provider_, barcode) VALUES ('$provider', '$barcode')";

	if ($conn->query($sql) === TRUE) {
    echo "<script>location.href='bevestiging.php';</script>";
		// echo "New record created successfully";
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
		<title>Pakjes toevoegen</title>
        <body>
            <div>
				<form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">
					<h1>Geef hier je pakket in</h1>
					<br>
					<label for="provider">Provider:</label><br>
					<input required type="text" id="provider" name="provider"value=<?php $provider;?>><br>
					<br><br>
					<label for="barcode">Barcode:</label><br>
					<input required type="text" id="barcode" name="barcode" value=<?php $barcode;?>><br>
					<br><br>
					<input type="submit" value="Submit">
					<br><br>
					<p>*voeg O toe voor de barcode (PostNL)</p>
            		<a href="table.php">
                	<p>Bekijk de leverstatus van de pakjes</p>
            		</a>
				</form>
			</div>
        </body>
    </head>
</html>