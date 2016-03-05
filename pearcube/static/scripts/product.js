$(document).ready(function() {
    add_tooltip_handlers()
});

function add_tooltip_handlers() {
    $('.fa').on('click', function () {
        var $el = $(this).parent()
        var question = $el.attr('data-question')
        var content = $el.attr('data-tip');
        $('#info-popup').find('.info-question').html(question);
        $('#info-popup').find('.info-content').html(content);
        show_lightbox('#info-popup');
    });
   $('.tip').tipr();
}

function rotate_image(el, direction) {
    var $parent = $(el).closest('.product_image_wrapper');
    var $visible_image = $parent.find('.visible_image');
    var $all_images = $parent.find('.product_image');
    var cur_idx = $visible_image.index();
    var num_images = $all_images.length;
    var new_idx = (num_images + cur_idx + direction) % num_images;
    rotate_image_to($parent, new_idx);
}

function rotate_image_to(el, index) {
    $parent = $(el).closest('.product_image_wrapper')
    var $all_images = $parent.find('.product_image');
    var $all_buttons = $parent.find('.product_image_button');
    $all_images.removeClass('visible_image');
    $all_images.eq(index).addClass('visible_image');
    $all_buttons.removeClass('selected_button');
    $all_buttons.eq(index).addClass('selected_button');

}
