function print_pdf(){
	window.print();
}



function signWithSignature(){
	var signature = $("#signature").jSignature({'UndoButton' : true});


	$('#clear').click(function () {
		// $("#signature").value = '';
		$('#signature').jSignature("reset");
	});


	$("#preview").click(function(){
		var data = signature.jSignature("getData", "image");
		$("#signaturePreview").attr('src', 'data: ' + data);
	});

	$("#download").click(function(){
		var image = $("#signaturePreview")[0];
		this.href = image.src;
	});

}

signWithSignature();