document.addEventListener('DOMContentLoaded', () => {
	document.querySelector("button").addEventListener('click', () => {
		navigator.clipboard.writeText("g='';a=document.getElementsByClassName('word off');for(i=0;i<a.length;i++){g+=i>0?'|':'';g+=a[i].innerHTML.toLowerCase();}");
	}, false);
}, false);
