function clickEditButtonSubmit(form, name){
  event.preventDefault()
  var val;
  // get list of radio buttons with specified name
  var radios = form.elements[name];

  // loop through list of radio buttons
  for (var i=0, len=radios.length; i<len; i++) {
      if ( radios[i].checked ) { // radio checked?
          val = radios[i].value; // if so, hold its value in val
          break; // and break out of for loop
      }
  }
  return val;
}
document.getElementById('editForm').onsubmit = function() {
    // this (keyword) refers to form to which onsubmit attached
    // 'ship' is name of radio button group
    var val = clickEditButtonSubmit(this, 'update_it');
    // display value obtained
    if(val=="NewPic"){
      // Create a form synamically
      var form = document.createElement("form");
      form.setAttribute("method", "post");
      form.setAttribute("action", "/");

      // Create an input element for Full Name
      var FN = document.createElement("input");
      FN.setAttribute("type", "text");
      FN.setAttribute("name", "newPicForWeb");
      FN.setAttribute("placeholder", "Picture Link");

      // create a submit button
      var s = document.createElement("input");
      s.setAttribute("type", "submit");
      s.setAttribute("value", "Submit");

      form.appendChild(FN);
      form.appendChild(s);
      var element = document.getElementById("addEditForm");
      element.appendChild(form);
    }
    else if(val=="NewLink"){
      var form = document.createElement("form");
      form.setAttribute("method", "post");
      form.setAttribute("action", "/");

      // Create an input element for Full Name
      var FN = document.createElement("input");
      FN.setAttribute("type", "text");
      FN.setAttribute("name", "newLinkForWeb");
      FN.setAttribute("placeholder", "Link");

      var hv = document.createElement("input");
      hv.setAttribute("type", "text");
      hv.setAttribute("name", "hidden");
      hv.setAttribute("value", "{{The_entitity_chosen.title_class}}");

      // create a submit button
      var s = document.createElement("input");
      s.setAttribute("type", "submit");
      s.setAttribute("value", "Submit");

      form.appendChild(FN);
      form.appendChild(hv);
      form.appendChild(s);
      var element = document.getElementById("addEditForm");
      element.appendChild(form);
    }
    else{
      var form = document.createElement("form");
      form.setAttribute("method", "post");
      form.setAttribute("action", "/");

      // Create an input element for Full Name
      var FN = document.createElement("input");
      FN.setAttribute("type", "text");
      FN.setAttribute("name", "newTitleForWeb");
      FN.setAttribute("placeholder", "Title");

      // create a submit button
      var s = document.createElement("input");
      s.setAttribute("type", "submit");
      s.setAttribute("value", "Submit");

      form.appendChild(FN);
      form.appendChild(s);
      var element = document.getElementById("addEditForm");
      element.appendChild(form);
    }
}
