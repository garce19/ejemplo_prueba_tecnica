<?php
//Datos de conexión a la BD
$host = 'localhost';
$user = 'root';
$password = 'www..germanrojas123.,';
$database = 'mydb';

// Conexión a la BD
$mysqli = new mysqli($host, $user, $password, $database);

// Verificar si hubo error en la conexión
if ($mysqli->connect_errno) {
    die("Error al conectar a la base de datos: " . $mysqli->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = $_POST["email"];
    $password = $_POST["password"];

    // Consulta SQL para buscar el email y la contraseña en la BD
    $query = "SELECT * FROM Coordinator WHERE email = '$email' AND password = '$password'";
    $result = $mysqli->query($query);

    // Verificar si se encontró una coincidencia
    if ($result->num_rows==1) {
        // Credenciales válidas, redireccionamos al usuario a data-form.php
        header("Location: data-form.php");
        exit;
    } else {
        // Credenciales inválidas, mostramos mensaje de error
        echo "Invalid credentials. Please try again";
    }

    // Liberamos recursos
    $result->close();
}

// Cerramos conexión con la BD
$mysqli->close();
?>
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <?php include 'login.html'; ?>
</body>
</html>