<html>
	<?php
		
		//compsci.adelphi.edu/~jasonmassimino?mID=1&uID=10
	
		//echo "Variable Test <br>";
		//Check Mail ID
		if(isset($_GET['mID'])){
			$mID = $_GET['mID'];
			$flag1 = true;
		} else {
			echo "mID not set! <br>";
			$flag1 = false;
		}
		//Check User ID
		if(isset($_GET['uID'])){
			$uID = $_GET['uID'];
			$flag2 = true;
		} else {
			echo "uID not set! <br>";
			$flag2 = false;
		}
		
		if($flag1&&$flag2){
			//Connect to DB
			session_start();
			try {
				$dbh = new PDO('pgsql:dbname=groupg');
			} catch (PDOException $e) {
				print "Error: ".$e->getMessage()."<br/>";
				die();
			}
			echo '<img src="Phishing_Explanation.png" alt="icon" />';
			$st = $dbh->prepare("
	UPDATE users 
	SET score = score + 1 
	WHERE id=?");
			$st->bindParam(1, $uID);
			$st->execute();
			echo $st->rowCount() . " records updated successfully";
			//$st = $dbh->prepare('SELECT * FROM userlist WHERE id=10;');
			/*
			
			//while
			while ($row = $st->fetch(PDO::FETCH_ASSOC)) {
				print "$row[id], $row[lastname], $row[firstname]<br/>";
				print "\n";
			}
			*/
		}
	?>
</html>
