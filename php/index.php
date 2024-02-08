<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Spaceapi page for Hacker Hotel</title>
        <meta charset="UTF-8">
    </head>
    <body>
        <h1>Spaceapi page for Hacker Hotel</h1>
        <p>It works. More info on the Gitlab page: <a href="https://gitlab.com/jhaand/hacker-hotel-space-state">https://gitlab.com/jhaand/hacker-hotel-space-state</a></p>
        <p>You can find the current space state at: <a href="https://hackerhotel.tdvenlo.nl/spaceapi.json">https://hackerhotel.tdvenlo.nl/spaceapi.json</a></p>
<?php

$spacestate_filename = './spacestate.php';
if (file_exists($spacestate_filename)) {
include($spacestate_filename);
} else {
print("<p>No spacestate file found.</p>");
}

?>
    </body>
</html>
