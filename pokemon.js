$(function(){
	var picnum = '';
	var i;
	for(i = 1; i<=151; i++){
		picnum += '<img id="img'+i+'" src="http://pokeapi.co/media/img/'+i+'.png" title="img'+i+'">';
	}
	// console.log(picnum);
	$('.pokemon').append(picnum)
});