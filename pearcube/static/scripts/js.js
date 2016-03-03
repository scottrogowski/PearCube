function is_mobile() {
    return window.innerWidth < 600;
}

function is_touch_device() {
  return 'ontouchstart' in window        // works on most browsers 
      || navigator.maxTouchPoints;       // works on IE10/11 and Surface
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
