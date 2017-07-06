$(document).ready(function() {
	$('#dockNumber').focus()
  $(window).keydown(function(event){
    if(event.keyCode == 13) {
      event.preventDefault();
      if($('#sealNumberForm').is(':hidden') && $('#inputFileForm').is(':hidden')) {
      	$('#sealNumberForm').show()
      	$('#dockNumberForm').hide()
      	$('#sealNumber').focus()
      } else if($('#dockNumberForm').is(':hidden') && $('#inputFileForm').is(':hidden')) {
      	$('#inputFileForm').show()
      	$('#sealNumberForm').hide()
      	$('#inputFile').focus()
      } else if($('#dockNumberForm').is(':hidden') && $('#sealNumberForm').is(':hidden')) {
      		$('#enterForm').submit()
      }
      return false;
    }
  });
});