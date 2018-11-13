
	var bodyID = document.getElementsByTagName("body")[0];
	bodyID.setAttribute("onload", "showWhatsUp();");

	function showWhatsUp() {
		if ( window.location.hostname != "readthedocs.org")
		{ 
			document.getElementById("whatsup").innerHTML = 
			"-- <a href='' onclick='goWhatsUp()'>what's up?</a> --"; 
		}
	}

	function goWhatsUp() {
        window.open('/img/whats-up.html?name=' + objectName + 
        '&desc=' + objectDesc + '&image=' + objectImage, 
        'Whats-Up', 
        'fullscreen=1,toolbar=0,location=0,menubar=0,scrollbars=0,status=0,titlebar=0'); 
        return false;
	}
