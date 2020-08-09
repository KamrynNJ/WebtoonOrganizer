
function clickAddButton(form){
  event.preventDefault()


  var formLink=form.linkGiven.value;
  var formPic=form.picGiven.value;
  var formTitle=form.titleGiven.value;
  alert("you typed:"+ formTitle );

  var title=document.createElement("div");
  var node=document.createTextNode(formTitle);
  title.appendChild(node);
  var element = document.getElementById("webtoons");
  element.appendChild(title);

  var pic=document.createElement("div");
  var picNode=document.createElement("img");
  pic.appendChild(picNode);
  picNode.setAttribute('src',formPic);
  picNode.onclick = function() {
    window.location.href = formLink;
  };
  var element = document.getElementById("webtoons");
  element.appendChild(pic);



}
