<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $email = $_POST['email'];
    $phone = $_POST['phone'];
    $zipCode = $_POST['zip-code'];

    $to = 'leifgerchberg@gmail.com';
    $subject = 'New lead from landing page';
    $message = "Email: $email\nPhone: $phone\nZip Code: $zipCode";
    $headers = "From: $email";

    if (mail($to, $subject, $message, $headers)) {
        echo "<h1>Thanks for signing up!</h1>";
    } else {
        echo "<h1>Oops, something went wrong. Please try again later.</h1>";
    }
} else {
?>
<h1>Sign up for getting your mow lawned</h1>
<form action="" method="post">
  <label for="email">Email Address:</label>
  <input type="email" id="email" name="email" required><br><br>
  <label for="phone">Phone Number:</label>
  <input type="tel" id="phone" name="phone" pattern="[0-9]{10}" required><br><br>
  <label for="zip-code">Zip Code:</label>
  <input type="tel" id="zip-code" name="zip-code" pattern="[0-9]{5}" required><br><br>
  <input type="submit" value="Sign Up">
</form>
<?php
}
?>