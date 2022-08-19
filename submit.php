<?php

$First_name = $_POST['First_name'];
$Last_name = $_POST['Last_name'];


$host = "localhost";
$user = "root";
$password = "mynewpassword";
$db = "cust_details";

$conn = new mysqli($host, $username, $password, $db);

if ($conn->connect_error){
	die("Connection failed: ". $conn->connect_error);
}
		  
		  
$sql = "INSERT INTO customer (First_name, Last_name) VALUES ('$First_name', '$Last_name')";
         


if ($conn->query($sql) === TRUE) {
	echo "ADDED: ".$First_name.", ".$Last_name;
} else {
	echo "Error: ".$sql."<br>".$conn->error;
}

$conn->close();




?>
