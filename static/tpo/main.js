function checkMarks1()
{
  var Marks1 = document.forms["register"]["10percent"].value;
  var Marks2 = document.forms["register"]["12percent"].value;
  var Marks3 = document.forms["register"]["diplomapercent"].value;

  if ((Marks1.length != 0 && Marks1 < 50))
  {
    document.getElementById("Marks1").innerHTML = "* 10th Percentage cannot be less than 50";
    document.getElementById("Register").style.display = "none";
    return false;
  }
  else
  {
    document.getElementById("Marks1").innerHTML = "";
    document.getElementById("Register").style.display = "block";
  }

  if((Marks2.length != 0 && Marks2 < 50) || (Marks3.length != 0 && Marks3 < 60))
    {
        document.getElementById("Register").style.display = "none";
    }

  return true;
}


function checkMarks2()
{
  var Marks1 = document.forms["register"]["10percent"].value;
  var Marks2 = document.forms["register"]["12percent"].value;
  var Marks3 = document.forms["register"]["diplomapercent"].value;

  if (Marks2.length != 0 && Marks2 < 50)
  {
    document.getElementById("Marks2").innerHTML = "* 12th Percentage cannot be less than 50";
    document.getElementById("Register").style.display = "none";
    return false;
  }
  else
  {
    document.getElementById("Marks2").innerHTML = "";
    document.getElementById("Register").style.display = "block";
  }

  if((Marks1.length != 0 && Marks1 < 50) || (Marks3.length != 0 && Marks3 < 60))
    {
        document.getElementById("Register").style.display = "none";
    }

  return true;
}

function checkMarks3()
{
  var Marks1 = document.forms["register"]["10percent"].value;
  var Marks2 = document.forms["register"]["12percent"].value;
  var Marks3 = document.forms["register"]["diplomapercent"].value;

  if (Marks3.length != 0 && Marks3 < 60)
  {
    document.getElementById("Marks3").innerHTML = "* Diploma Percentage cannot be less than 60";
    document.getElementById("Register").style.display = "none";
    return false;
  }
  else
  {
    document.getElementById("Marks3").innerHTML = "";
    document.getElementById("Register").style.display = "block";
  }

  if((Marks1.length != 0 && Marks1 < 50) || (Marks2.length != 0 && Marks2 < 50))
    {
        document.getElementById("Register").style.display = "none";
    }

  return true;
}
