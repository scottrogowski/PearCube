$(document).ready(function() {
    add_tooltip_handlers()
});

function add_tooltip_handlers() {
    if (is_touch_device()) {
        $('.fa').on('click', function () {
            var $el = $(this).parent()
            var question = $el.attr('data-question')
            var content = $el.attr('data-tip');
            $('#info-popup').find('.info-question').html(question);
            $('#info-popup').find('.info-content').html(content);
            show_lightbox('#info-popup');
        })
    }
    else {
       $('.tip').tipr();
    }    
}
