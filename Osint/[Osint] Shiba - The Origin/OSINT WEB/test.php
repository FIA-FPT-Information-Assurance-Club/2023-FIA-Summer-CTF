<?php
ini_set('display_errors', 0);
ini_set('error_reporting', 0);

header('Content-Type: application/json');

$correct_flag = array(
    "flag" => "FIA{Th3_0rig1n_of_Shiba_1s_L4b0ratory}"
);

$wrong_flag = array(
    "flag" => "False"
);

try {
    if (isset($_GET["id"]) && is_string($_GET["id"]) && !empty($_GET["id"])) {
        $id = $_GET["id"];
        if (ctype_alnum($id) && strlen($id) < 50) {
            if ($id === "PerryTheDoof") {
                echo json_encode($correct_flag);
            } else {
                echo json_encode($wrong_flag);
            }
        } else {
            echo json_encode(array("error" => "Invalid id parameter"));
        }
    } else {
        echo json_encode(array("error" => "Missing or invalid id parameter"));
    }
} catch(Exception $e) {
    error_log("Error in test.php: " . $e->getMessage());
    echo json_encode(array("error" => "An error occurred"));
}
?>