<?php
// Path to the Python interpreter
$python = 'C:\Users\Spare\AppData\Local\Programs\Python\Python312\python.exe'; // Adjust this path based on your system

// Path to the Python script
$pythonScript = 'index.py';

// Execute the Python script
$output = [];
$returnValue = 0;

exec("$python $pythonScript 2>&1", $output, $returnValue);

// Output results
if ($returnValue === 0) {
    echo "Python script executed successfully:<br>";
    echo implode("<br>", $output);
} else {
    echo "Python script failed with return code $returnValue:<br>";
    echo implode("<br>", $output);
}
?>
