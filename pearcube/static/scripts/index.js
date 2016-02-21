function is_mobile() {
    return window.innerWidth < 600;
}

function show_lightbox() {
     document.getElementById('lightbox-overlay').style.display='flex';
     document.getElementById('lightbox-content').style.display='block';
}

function hide_lightbox() {
     document.getElementById('lightbox-overlay').style.display='none';
     document.getElementById('lightbox-content').style.display='none';
}

function show_examples() {
    if (is_mobile()) {
        window.location.replace('/Example-Emails/Small-Cheap-Photo-Scanner');
    }
    else {
        show_lightbox();
    }
}
