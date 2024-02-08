<!DOCTYPE html>
<html>
<head>
<title>HackerHotel Spaceapi</title>
</head>
<body>
This is the update script for the HackerHotel Spaceapi.json.
<pre>
<?php 
print("PHP: Hi NodeMCU. \n");

# You can use a temporary name for testing puroposes.
$spaceapi_filename = './spaceapi2.json';
$spacestate_filename = './spacestate.php';

$current_time = time();
print("Time: $current_time\n");

# Get the API_key from an file not controlled by Git.
include("secretsss.php"); 
if (empty($API_key)) {
	die("Secrets not loaded\n");
}

$_POST = json_decode(file_get_contents('php://input'), true);
#print_r($_POST);
$read_key = substr(trim($_POST['API_key']),0,128);
$sstate = substr(trim($_POST['sstate']),0,10) ;

if ($sstate == 'true') {
    $sstate = 'true';
    print("PHP: SSTATE is True\n");
    } else {
    $sstate = 'false';
    print("PHP: SSTATE is False\n");
    }

# print("read_key: $read_key\n");
# print("API_key: $API_key\n");

if ($read_key != $API_key) {
    die("Wrong key\n");
}

print("PHP: We got the right key\n");
print("PHP: Space state status: $sstate\n");
 
$spaceapi_json = <<<EOT
{
"api": "0.13",
"api_compatibility": ["14"],
"space": "Hacker Hotel",
"logo": "http://hackerhotel.tdvenlo.nl/img/HackerHotel_logo.png",
"url": "https://www.hackerhotel.nl",
"location": {
    "address": "Oud Millingseweg 62, 3886MJ, Garderen, The Netherlands",
    "lat": 52.2208671,
    "lon": 5.7208085
},
"contact": {
    "mastodon: "@hackerhotel@hsnl.social",
    "twitter": "@hotelhacker",
    "email": "info@hackerhotel.nl",
    "facebook": "https://www.facebook.com/hackerhotel/"
},
"issue_report_channels": [
    "email"
],
"state": {
    "open": $sstate,
    "lastchange": $current_time,
    "icon": {
        "open": "http://hackerhotel.tdvenlo.nl/img/HH_logo_open.png",
        "closed": "http://hackerhotel.tdvenlo.nl/img/HH_logo_closed.png"
     },
    "projects": [ "https://pretalx.hackerhotel.nl/hackerhotel-2024/schedule/" ]
    }
} 
EOT;

# Write the actual spaceapi.json
$spaceapi_file = fopen($spaceapi_filename, 'w') or die ("PHP: Unable to open $spaceapi_filename file!");
fwrite($spaceapi_file, $spaceapi_json);
fclose($spaceapi_file);
print("PHP: $spaceapi_filename written\n");

# Update the index.php with the actual state.
if ($sstate == 'true') {
    $space_access = "OPEN";
    $space_img = "./img/HH_logo_open.png";
    } else {
    $space_access = "CLOSED";
    $space_img = "./img/HH_logo_closed.png";
    }

$spacestate_html = <<< EOT
<!-- included spacestate file begin -->
        <p>The space is $space_access!</p>
        <p><img src=$space_img></p>
<!-- included spacestate file end-->

EOT;

# update the file for the index.html
print("PHP: write the spacestate file.\n");
$spacestate_file = fopen($spacestate_filename, 'w') or die ("PHP: Unable to $spacestate_filename open file!");
fwrite($spacestate_file, $spacestate_html);
fclose($spacestate_file);
print("PHP: $spacestate_filename written\n");

?>
</pre>
</body>
</html>
