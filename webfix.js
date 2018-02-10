document.getElementById('infile').onchange = function(e) {
    loadImage(
        e.target.files[0],
        function(canvas) {
            console.log(canvas);
            canvas.toBlob(function(blob){
                var newImg = document.createElement('img');
                var url = URL.createObjectURL(blob);
                // newImg.onload = function() {
                //     URL.revokeObjectURL(url);
                // };
                var downLink = document.createElement('a');
                downLink.setAttribute('href', url);
                downLink.src = url;
                downLink.innerHTML = "download";
                downLink.download="fixed.jpg";
                document.body.appendChild(downLink);
                document.body.appendChild(newImg);
            }, 'image/jpeg', .95);
            //document.body.appendChild(canvas);
        },
        {orientation: true}
    );
};
