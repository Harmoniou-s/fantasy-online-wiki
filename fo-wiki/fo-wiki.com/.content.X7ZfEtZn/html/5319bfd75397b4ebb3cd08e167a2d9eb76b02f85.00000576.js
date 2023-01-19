// JavaScript Document
//<!--
	function hideshow(id){
	if (document.getElementById){
	obj = document.getElementById('x'+id);
	obj2 = document.getElementById(id);
	if (obj.style.display == "none"){
		obj.style.display = "";
		obj2.innerHTML = "&not;  hide";
		obj2.style.color = "#C30";
	} else {
		obj.style.display = "none";
		obj2.innerHTML = "show";
		obj2.style.color = "#069";
	}
	}
	}
-->