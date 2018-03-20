<html>
	<?php
		echo "Variable Test <br>";
		if(isset($_GET['mID'])){
			$mID = $_GET['mID'];
			echo $mID;
			echo "<br>";
		} else {
			echo "mID not set! <br>";
		}
		if(isset($_GET['uID'])){
			$uID = $_GET['uID'];
			echo $uID;
			echo "<br>";
		} else {
			echo "uID not set! <br>";
		}
		
		session_start();
			try{	
			$db_connection = pg_connect("host = localhost dbname=groupg user=jasonmassimino password=SnekDaBest");
			
	
	?>
</html>