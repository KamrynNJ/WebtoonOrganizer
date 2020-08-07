const addButton=document.getElementById("addbutton")
function clickAddButton(){
  //var newDiv=document.createElement("div");
var newDiv=document.createElement('div');
var newCon=document.createTextNode(document.getElementById("titleGiven"));
newDiv.appendChild(newCon);
var currDiv= document.getElementById("addForm");
document.body.insertBefore(newDiv,currDiv);
}
  addButton.addEventListener("click",clickAddButton);
