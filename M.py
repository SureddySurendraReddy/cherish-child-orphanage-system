  border: 0;
  padding: 0;
}

select option {
  background-color:azure;
}
.round-input {
  border: none;
  border-radius: 25px;
  padding: 10px;
  width: 530px;
  box-shadow: 0px 0px 5px rgba(0,0,0,0.1);
  background-color:azure;
}
label{
  transform: translateY(20%);
}
textarea {
  background-color: rgba(254, 254, 254, 0);
}
textarea {
  opacity: 6;
}
a{
  font-size:35px;
  text-decoration:none;
  text-align: center;
}

</style>
<body>
  <div>
    <div class="wave"></div>
    <div class="wave"></div>
    <div class="wave"></div>
  
  <div class="hi">
  <h1>DONATION DETAILS</h1>
  <form action="submit.php" method="post">
    <label for="donation_type"><b>DONOTION TYPE-</b></label>
    <select name="donation_type">
      <option value="rice">RICE</option>
      <option value="meals">MEALS</option>
      <option value="clothes">CLOTHES</option>
      <option value="curries">CURRIES</option>
      <option value="Medicines">MEDICINES</option>
      <option value="other">OTHER</option>
    </select>
    <br>

    <label for="quantity"><b>QUANTITY-</b></label>
    <input type="number" name="quantity" class="round-input">
<br>
    <label for="unit"><B>UNIT-</B></label>
    <select name="unit">
      <option value="cans">CANS</option>
      <option value="boxes">BOXES</option>
      <option value="bags">BAGS</option>
      <option value="pounds">POUNDS</option>
      <option value="stripes">NO OF STRIPES</option>
      <option value="other">OTHER</option>
    </select>
<br>

<label for="loc"><B>LOCATION-</B></label> <br>
<textarea name="hello" id="loc"  rows="6" cols="60"></textarea>
  </div>
</form>
  <div style="text-align:center; padding:15px;font-size:20px; font-family: cursive;">
    <a href="donate.html" style="color:rgb(25, 27, 25);"><B>DONATE--></B></a>
  </div>
  </div>
</body>
</html>
