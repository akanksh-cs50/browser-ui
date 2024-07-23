document.querySelector('input').addEventListener('keypress', function(){
	item_elements = document.querySelectorAll('a')
	items = []

	for(i = 0; i < item_elements.length; i++) {
		items.push(item_elements[i].textContent.replace(' ', ''))
	}

	for(i = 0; i < item_elements.length; i++) {
		if (items[i].includes(
			document.querySelector('input').value)
		){
			item_elements[i].style.display = "block"
		}else{
			item_elements[i].style.display = "none"
		}
	}

})
