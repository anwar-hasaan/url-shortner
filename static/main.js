let copy_btn = document.getElementById("copy-btn");

copy_btn.addEventListener("click", function(){
    let url = document.getElementById('url');
    let temp = document.createElement('input');
    temp.value = url.textContent;
    document.body.appendChild(temp);
    temp.select();
    document.execCommand("copy", false);
    temp.remove();

    copy_btn.innerHTML = "copied";
    // alert("Short URL copied to clipboard")
})