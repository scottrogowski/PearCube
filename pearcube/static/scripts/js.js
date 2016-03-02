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