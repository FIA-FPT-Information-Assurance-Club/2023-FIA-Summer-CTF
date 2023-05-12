<?php
	if(isset($_SERVER['REMOTE_ADDR'])){
		$rm_ad = $_SERVER['REMOTE_ADDR'];
		// echo "REMOTE_ADDR is:$rm_ad";
		if($rm_ad == "127.0.0.1"){
			die("Flag is : FIA{th3_d!ff3r3nc3_b3tvv3n_curl_@nd_parse_url}");
		}
	}
?>
Must be accessed from localhost!!!!!