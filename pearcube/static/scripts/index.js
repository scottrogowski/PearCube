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

    return false;
}

function post(url, data, cb) {
    var req = new XMLHttpRequest();
    req.open('POST', url, true);
    req.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
    req.send(data);
    req.onload = function() {
        if (cb !== null) {
            cb(xhr);
        }
    }
}

function send_cs_email() {
    $.ajax({
        url: '/cs_request',
        type: 'POST',
        data : $('#cs-form').serialize(),
        success: function(resp) {
            alert("Thanks! We'll get back to you as soon as we can");
        },
        error: function(xhr, status, error) {
            alert(error)
        }
    });
    event.preventDefault()
}
