<?

$submit=$_REQUEST['submit'];
$luck= $_REQUEST['luck'];
$feedback= $_REQUEST['feedback'];

$remote_address = $_SERVER['REMOTE_ADDR'];

$dateTime = Date("Y-m-d H:i:s");

?>
<!DOCTYPE html>
<html>
<body>
<form method=GET action='?'>
<input type=text name='luck' value='<?=$luck?>'>
<br/>
<input type=submit value='Try your luck'>
<br />
<?
if($luck)
{
	//open socket here 
	//echo "String = $str";

$fp = fsockopen("localhost", 8083, $errno, $errstr, 30);
if (!$fp) {
    echo "We don't have an answer for you right now. We aren't having any performance issues, really. Just a technical issue.<br />\n";
    file_put_contents("./error.log", "$errno, $errstr, $remote_address, $dateTime\n", FILE_APPEND);
    } 

else {
    $out = "$luck";
    fwrite($fp, $out);
    while (!feof($fp)) {

        $response=fgets($fp, 128);

        if($response=='True') 
        {

            echo "That's What She Said!<br />\n";
            
        }
        elseif($response=='False')
        {
            echo "That's Not What She Said.<br />\n";
        }
            file_put_contents("./access.log", "$dateTime, $remote_address, \"$luck\", $response, $feedback\n", FILE_APPEND);
        // Print feedback here: 
        echo "Does this sound right? 
            <br />
            <input type='radio' name='feedback' value='Positive' />Yes it does<br />
            <input type='radio' name='feedback' value='Negative' />No it does not<br />
            <input type=submit value='Submit Feedback'>";
         
        if($feedback)
        {
            echo "<br />Thanks for your feedback. Now go try your luck again.";
            // Add code here to log the feedback.
            file_put_contents("./feedback.log", "$feedback, $response, $luck, $remote_address, $dateTime\n", FILE_APPEND);
        }
    }
    fclose($fp);
}

}
?>
</form>
</body>
</html>
