document.getElementById('infile').onchange = function(e) {
    loadImage(
        e.target.files[0],
        function(canvas) {
            canvas.toBlob(function(blob){
                var url = URL.createObjectURL(blob);
                var downLink = document.createElement('a');
                downLink.setAttribute('href', url);
                downLink.src = url;
                downLink.innerHTML = "download";
                downLink.download="fixed.jpg";
                document.body.appendChild(downLink);
            }, 'image/jpeg', .95);
        },
        {orientation: true}
    );
};
