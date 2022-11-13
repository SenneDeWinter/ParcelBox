<?php session_start(); ?>
<?php
    if (!isset($_SESSION["user"])){
    echo "<meta http-equiv='refresh' content='0; URL=login.php'/>";
    }
?>
<!DOCTYPE html>
<html>
    <head>
		<link rel="stylesheet" href="styles.css">
        <body>
            <div>
				<form>
                <?php
                    $con=mysqli_connect("localhost:3306","","","");
                    // Check connection
                    if (mysqli_connect_errno())
                    {
                    echo "Failed to connect to MySQL: " . mysqli_connect_error();
                    }

                    $result = mysqli_query($con,"SELECT * FROM parcels");

                    echo "<table border='1'>
                    <tr>
                    <th>Provider</th>
                    <th>Barcode</th>
                    <th>Delivery time</th>
                    </tr>";

                    while($row = mysqli_fetch_array($result))
                    {
                    echo "<tr>";
                    echo "<td>" . $row['provider_'] . "</td>";
                    echo "<td>" . $row['barcode'] . "</td>";
                    echo "<td>" . $row['delivery_time'] . "</td>";
                    echo "</tr>";
                    }
                    echo "</table>";

                    mysqli_close($con);
                ?>
				</form>
			</div>
        </body>
    </head>
</html>