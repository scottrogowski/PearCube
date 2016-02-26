function is_mobile() {
    return window.innerWidth < 600;
}

function show_lightbox(lightbox_id) {
    console.log(lightbox_id)
    console.log($(lightbox_id))
    $('.lightbox-overlay').css('display','flex');
    $(lightbox_id).css('display','block');
}

function hide_lightbox() {
    $('.lightbox-overlay').hide();
    $('.lightbox-content').hide();
}

function show_examples() {
    if (is_mobile()) {
        window.location.replace('/Example-Emails/Small-Cheap-Photo-Scanner');
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
            alert(error)
        }
    });
    event.preventDefault()
}
