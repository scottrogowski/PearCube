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

function validate_form() {
    var $cs_form_ta = $('#cs-form-ta');
    var $cs_form_in = $('#cs-form-in');
    var problems_exist = false;

    if ($cs_form_ta.val().length < 3) {
        $cs_form_ta.addClass('form-problems');
        $cs_form_ta.focus(function () {$cs_form_ta.removeClass('form-problems')});
        problems_exist = true;
    }

    if ($cs_form_in.val().length < 3 || !(/\S+@\S+\.\S+/.test($cs_form_in.val()))) {
        alert($cs_form_in.val());
        $cs_form_in.addClass('form-problems');
        $cs_form_in.focus(function () {$cs_form_in.removeClass('form-problems')});
        problems_exist = true;
    }

    if (problems_exist) {
        return false;
    }
    else {
        return true;
    }
}

var email_send_lock = false;
function send_cs_email() {
    if (email_send_lock)
        return false;
    email_send_lock = true;

    if (!validate_form()) {
        email_send_lock = false;
        return false;
    }

    var $clock_popup = $('#clock-popup');
    var $cs_form_ta = $('#cs-form-ta');
    var $cs_form_in = $('#cs-form-in');
    var $cs_form_button = $('#cs-form-btn');
    $cs_form_button.html('<i class="fa fa-cog spin"></i>');
    $.post({
        url: '/cs_request',
        data: $('#cs-form').serialize(),
        dataType: 'json',
        success: function(resp) {
            show_lightbox($clock_popup);
            $cs_form_button.text("Send");
            $cs_form_in.val('');
            $cs_form_ta.val('');
            if ('confirmation_body' in resp) {
                // For debugging
                $clock_popup.append('<iframe style="width:90%; height:400px;"></iframe>');
                $clock_popup.find('iframe')[0].contentDocument.write(resp['confirmation_body']);
            }
        },
        error: function(xhr, status, error) {
            console.log(xhr, status, error);
            $cs_form_button.text("Send");
            alert("Sorry. There was a problem. Please try again later");
        }
    });
    email_send_lock = false;
    return false;
}

var rotate_lock = false;
function rotate_carousel(direction) {
    if (rotate_lock)
        return
    rotate_lock = true;
    $product_image_wrappers = $('.product_image_wrapper');
    $fc = $('.product_image_wrapper:first-child');
    $lc = $('.product_image_wrapper:last-child');
    $carousel = $('#frontpage_carousel');
    width = $fc.outerWidth()

    // mobile for only one element
    if (width * 2 > $carousel.width()) {
        if (direction == -1) {
            $lc.insertBefore($fc);
        }
        else {
            $fc.insertAfter($lc)
        }
        rotate_lock = false
        return
    }

    // desktop for 2 or more
    if (direction == -1) {
        $product_image_wrappers.animate(
            {'left': width },
            150,
            function() {
                $product_image_wrappers.css({'left': '0px'})
                $lc.insertBefore($fc)
                rotate_lock = false
            })
    }
    else {
        $product_image_wrappers.animate(
            {'left': -1*width },
            150,
            function() {
                $product_image_wrappers.css({'left': '0px'})
                $fc.insertAfter($lc)
                rotate_lock = false
            })
    }
}

$(document).ready(function() {
    $('.product_image')
})
