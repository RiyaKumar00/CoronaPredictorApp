function validate() {
  var firstname = document.getElementById('fname');
  var lastname = document.getElementById('lname');
  var email = document.getElementById('email');
  var age = document.getElementById('age');
  var state = document.getElementById('inputState');
  var day = document.getElementById('inputDays');

  if(firstname.value == "") {
      alert("FIRST NAME FIELD SHOULD NOT BE EMPTY");
      return false;
  }
  if(lastname.value == "") {
      alert("LAST NAME FIELD SHOULD NOT BE EMPTY");
      return false;
  }
  if(email.value == "") {
      alert("EMAIL FIELD SHOULD NOT BE EMPTY");
      return false;
  }
  if(age.value == "") {
      alert("AGE FIELD SHOULD NOT BE EMPTY");
      return false;
  }
  if(state.value == "") {
      alert("STATE FIELD SHOULD NOT BE EMPTY");
      return false;
  }
  if(day.value == "") {
      alert("DAYS FIELD SHOULD NOT BE EMPTY");
      return false;
  }
  return true;
}
