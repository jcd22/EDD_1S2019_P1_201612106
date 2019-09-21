$(document).ready(function(){
	//var num = 256;
	for(var i = 1; i<=16; i++){//fila
		for(var j = 1; j<=16; j++){//columna
			$('#bodyart').append('<div id ="a'+i+'-'+j+'"></div>')
		}
	}
});