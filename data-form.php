<?php
// Datos de conexión a la BD
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

// Consultar la tabla "County" para obtener todos los registros de "codeCounty"
$queryCounty = "SELECT codeCounty FROM County";
$resultCounty = $mysqli->query($queryCounty);

// Verificar si se obtuvieron resultados
if ($resultCounty->num_rows > 0) {
    // Crear un array para almacenar los valores de "codeCounty"
    $codeCountyOptions = array();

    // Recorrer los resultados y agregar cada valor a $codeCountyOptions
    while ($row = $resultCounty->fetch_assoc()) {
        $codeCountyOptions[] = $row["codeCounty"];
    }
} else {
    echo "No se encontraron registros en la tabla County";
}

// Verificar si se enviaron los datos por el formulario
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $year = $_POST["year"];
    $voteCount = $_POST["voteCount"];
    $politicalParty = $_POST["politicalParty"];
    $codeCounty = $_POST["codeCounty"];

    // Insertar datos en la tabla "Election"
    $queryElection = "INSERT INTO mydb.Election (year, voteCount, politicalParty, codeCounty) VALUES ($year, $voteCount, '$politicalParty', '$codeCounty')";
    if ($mysqli->query($queryElection)) {
        echo "Los datos se han insertado correctamente en la tabla Election.";
    } else {
        echo "Error al insertar los datos: " . $mysqli->error;
    }
}

// Cerrar conexión a la base de datos
$mysqli->close();
?>

<!DOCTYPE html>
<html>
<head>
    <title>Data form</title>
    <!-- Enlaces a los archivos CSS de Bootstrap y ADMINLTE -->
    <link
        rel="stylesheet"
        href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
    />
    <link
        rel="stylesheet"
        href="https://adminlte.io/themes/v3/dist/css/adminlte.min.css"
    />
    <link rel="stylesheet" href="styles.css" />
</head>
<body class="hold-transition login-page">
    <div class="login-box">
        <div class="card">
            <div class="card-header bg-primary text-white">
                <h3 class="card-title">Election</h3>
            </div>
            <div class="card-body">
                <form id="dataForm" action="data-form.php" method="post">
                    <div class="form-group">
                        <label for="year">Year</label>
                        <input
                            type="text"
                            class="form-control"
                            id="year"
                            placeholder="Enter year"
                            name="year"
                        />
                    </div>
                    <div class="form-group">
                        <label for="party">Political Party</label>
                        <select
                            class="form-control"
                            id="politicalParty"
                            name="politicalParty"
                        >
                            <option value="democrat">Democrat</option>
                            <option value="republic">Republican</option>
                            <option value="other">Other</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="county">County</label>
                        <select
                            class="form-control"
                            id="codeCounty"
                            name="codeCounty"
                        >
                            <?php
                            // Generar las opciones del select con los valores de codeCountyOptions
                            foreach ($codeCountyOptions as $option) {
                                echo "<option value=\"$option\">$option</option>";
                            }
                            ?>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="votes">Vote Count</label>
                        <input
                            type="text"
                            class="form-control"
                            id="voteCount"
                            placeholder="Enter number"
                            name="voteCount"
                        />
                    </div>
                    <button type="submit" class="btn btn-primary btn-lock">
                        Submit
                    </button>
                </form>
            </div>
        </div>
    </div>

    <!-- Enlaces a los archivos JS de jQuery, Bootstrap y ADMINLTE -->
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    <script src="https://adminlte.io/themes/v3/dist/js/adminlte.min.js"></script>

    <script>
        // Validación del formulario de ingreso de datos
        $(document).ready(function () {
            $("#dataForm").submit(function (event) {
                event.preventDefault();

                // Realiza las validaciones necesarias
                var year = $("#year").val();
                var party = $("#politicalParty").val();
                var county = $("#codeCounty").val();
                var votes = $("#voteCount").val();

                if (year === "") {
                    alert("Please, enter a year.");
                } else if (party === "") {
                    alert("Please, select a political party.");
                } else if (county === "") {
                    alert("Please, enter a county.");
                } else if (votes === "") {
                    alert("Please, enter the vote count.");
                } else {
                    this.submit();
                }
            });
        });
    </script>
</body>
</html>
