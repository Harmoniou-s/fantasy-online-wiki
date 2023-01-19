// JavaScript Document
//<!--
var cX = 0; var cY = 0; var rX = 0; var rY = 0;

function getPosition(element)
/* der Aufruf dieser Funktion ermittelt die absoluten Koordinaten
   des Objekts element */
{
  var elem=element,tagname="",x=0,y=0;
  
/* solange elem ein Objekt ist und die Eigenschaft offsetTop enthaelt
   wird diese Schleife fuer das Element und all seine Offset-Eltern ausgefuehrt */
  while ((typeof(elem)=="object")&&(typeof(elem.tagName)!="undefined"))
  {
    y+=elem.offsetTop;     /* Offset des jeweiligen Elements addieren */
    x+=elem.offsetLeft;    /* Offset des jeweiligen Elements addieren */
    tagname=elem.tagName.toUpperCase(); /* tag-Name ermitteln, Grossbuchstaben */

/* wenn beim Body-tag angekommen elem fuer Abbruch auf 0 setzen */
    if (tagname=="BODY")
      elem=0;

/* wenn elem ein Objekt ist und offsetParent enthaelt
   Offset-Elternelement ermitteln */
    if (typeof(elem)=="object")
      if (typeof(elem.offsetParent)=="object")
        elem=elem.offsetParent;
  }

/* Objekt mit x und y zurueckgeben */
  position=new Object();
  position.x=x;
  position.y=y;
  return position;
}

	var maporg1; var pos1;

function UpdateCursorPosition(e){ cX = e.pageX; cY = e.pageY;}
function UpdateCursorPositionDocAll(e){ cX = event.clientX; cY = event.clientY;}
if(document.all) { document.onmousemove = UpdateCursorPositionDocAll; }
else { document.onmousemove = UpdateCursorPosition; }

function AssignPosition(d) {
	if(self.pageYOffset) {
		rX = self.pageXOffset;
		rY = self.pageYOffset;
		}
	else if(document.documentElement && document.documentElement.scrollTop) {
		rX = document.documentElement.scrollLeft;
		rY = document.documentElement.scrollTop;
		}
	else if(document.body) {
		rX = document.body.scrollLeft;
		rY = document.body.scrollTop;
		}
	if (document.all) {
		cX += rX; 
		cY += rY;
		}
		
	d.style.left = (cX+10+5-window["pos1"].x+window.maporg1.scrollLeft) + "px";
	d.style.top = (cY+10-5-window["pos1"].y+window.maporg1.scrollTop) + "px";
}
function HideContent(d) {
	if(d.length < 1) { return; }
	document.getElementById(d).style.display = "none";
}
function ShowContent(d) {
	if(d.length < 1) { return; }
	var dd = document.getElementById(d);
	AssignPosition(dd);
	dd.style.display = "block";
}
function ReverseContentDisplay(d) {
	if(d.length < 1) { return; }
	var dd = document.getElementById(d);
	AssignPosition(dd);
	if(dd.style.display == "none") { dd.style.display = "block"; }
	else { dd.style.display = "none"; }
}

function SetContent(id,value) {
	document.getElementById(id).innerHTML=value;
		window.maporg1 = document.getElementById("maporg");
		window.pos1 = getPosition(window.maporg1);
}

function SetColor(id,value) {
	document.getElementById(id).style.backgroundColor=value;	
}
//-->
