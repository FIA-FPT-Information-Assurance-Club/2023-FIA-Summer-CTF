<?php
error_reporting(0);

function curl_get($url){
	$ch = curl_init();
	curl_setopt($ch,CURLOPT_URL,$url);
	curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
	curl_setopt($ch,CURLOPT_HEADER,0);
	$output = curl_exec($ch);
	if($output === FALSE ){
		echo "CURL Error:".curl_error($ch);
	}
	curl_close($ch);
	echo $output;
}

$disable_url_hosts = array("127.0.0.1", "localhost");
if(isset($_GET['urls'])){
	$urls = $_GET['urls'];
	$url_host = parse_url($urls,PHP_URL_HOST);
	if (in_array($url_host, $disable_url_hosts)) {
		die("Access local resources is not allowed!!!<a>$url_host</a>");
	}elseif (strpos($url_host,"127.0.") === 0) {
		die("Access local resources is not allowed!!!<a>$url_host</a>");
	}

	curl_get($urls);
}
?>

<html>
<head>
<style>
body {
  font-family: Arial, sans-serif;
  background-color: #f5f5f5;
}

blockquote {
background-color: #eeeeee;
padding: 10px;
margin: 0;
border-left: solid black 4px;
}

h1 {
font-size: 36px;
font-weight: bold;
border-bottom: solid black 2px;
margin-top: 30px;
margin-bottom: 20px;
text-align: center;
}

h2 {
font-size: 24px;
font-weight: bold;
border-bottom: solid black 1px;
margin-top: 25px;
margin-bottom: 15px;
}

.comment {
color: darkgreen;
}

.lastmod {
font-size: 14px;
color: #666;
}

a {
color: #000;
text-decoration: none;
border-bottom: solid 2px #000;
}

a:hover {
background-color: #000;
color: #fff;
}

footer {
font-size: 14px;
color: #666;
text-align: center;
margin-top: 50px;
margin-bottom: 20px;
}
</style>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<title>Where is the Flag?!</title>
</head>
<body>
<h1>Where is the Flag?!</h1>
<blockquote>
  <p>Flag?!<br>
  Try <a href="flag.php" title="Flag">this</a></p>
</blockquote>
<h2>Comments:</h2>
<blockquote class="comment">
  <p>This is a really interesting puzzle!</p>
</blockquote>
<hr noshade>
<footer>Flag CMS~~~~ | Last Modified: <?php echo date(DATE_RFC822);?></footer>
</body>
</html> 

<!--
if(isset($_GET['urls'])){
	$urls = $_GET['urls'];
	$url_host = parse_url($urls,PHP_URL_HOST);
	//Do something~~~~
	curl_get($urls);
}
-->