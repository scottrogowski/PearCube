function show_examples() {
    if (is_mobile()) {
        window.location.assign('/Portable-And-Cheap-Photo-Scanner');
    }
    else {
        show_lightbox('#example-popup');
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
            show_lightbox("#clock-popup")
        },
        error: function(xhr, status, error) {
            console.log(xhr, status, error)
            alert("Sorry. There was a problem. Please try again later")
        }
    });
    event.preventDefault()
}
