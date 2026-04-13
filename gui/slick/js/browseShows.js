// to show the hide view set to true
var iso_show_hidden_filter = false;
var iso_showcards = null;
var iso_tag_container = null;

// filter function, if there is any class starting with hide- the item is hidden
var iso_filter_func = function(){
        if (iso_show_hidden_filter) {
            return $(this).hasClass('to-hide');
        } else {
            let classes = $(this).attr('class').split(' ');
            let hidden = false;
            for (let cl in classes) {
                if (0 === classes[cl].trim().indexOf('hide-')) {hidden = true; break;}
            }
            return !hidden;
        }
    };

function updateTagCount() {
    $(iso_tag_container).each(function () {
        let target = $(this).data('target');
        let cur_count = $(iso_showcards).filter($('.' + target)).length;
        $(this).children('.count:first').text(' (' + cur_count + ')');
    });
}

$(document).ready(function(){
    iso_showcards = $('.show-card');
    checkbox2button('#tags-container');
    if (-1 !== saved_showsort_view.indexOf('.hide')) {
		iso_show_hidden_filter = true;
		$('#tags').hide();
	}
    if (-1 != saved_showsort_view.indexOf('library')) {
        if (-1 === saved_showsort_view.indexOf('not')) {
            $('.notinlibrary').addClass('hide-notinlibrary');
        } else {
            $('.inlibrary').addClass('hide-inlibrary');
        }
    }
    let = tag_el = $('#tag-self, #tag-acting');
    if (tag_el) {
        $(tag_el).change(function() {
            let tag_target = $(this).data('target');
            if(this.checked) {
                $('.' + tag_target).removeClass('hide-' + tag_target);
            } else {
                $('.' + tag_target).addClass('hide-' + tag_target);
            }
            $.iso.off('layoutComplete');
            $.iso.on('revealComplete', llUpdate);
            $.iso.on('hideComplete', llUpdate);
            $.iso.isotope({ filter: iso_filter_func });
        });
    }

    function checkbox2button(selector) {
        const button = $('<button type="button"></button>')
        $(selector).children('input[type="checkbox"]').each(function (){
            let cur_checkbox = $(this);
            let cur_checkbox_id = $(cur_checkbox).attr('id');
            let cur_target = $(cur_checkbox).data('target');
            let cur_checked = $(cur_checkbox).is(':checked');
            let label_for_checkbox = $("label[for='"+cur_checkbox_id+"']");
            let label_text = $(label_for_checkbox).text();
            let new_button = $(button).clone();
            $(selector).append(new_button);
            $(cur_checkbox).remove();
            $(label_for_checkbox).remove();
            let new_ico = $('<i></i>');
            let count_el = $('<span class="count"> (0)</span>');
            $(new_ico).addClass(cur_checked ? 'yes' : 'no');
            $(new_button).attr('id', cur_checkbox_id).addClass('btn-toggle').addClass(cur_checked ? 'btn-on' : 'btn-off').attr('data-target', cur_target).text(label_text).prepend(new_ico).append(count_el);
            $(new_button).click(function (){
                if ($(this).hasClass('btn-on')) {
                    $(this).removeClass('btn-on checked').addClass('btn-off').children('i').removeClass('yes').addClass('no');
                    $(this).prop('checked', false);
                } else {
                    $(this).removeClass('btn-off').addClass('btn-on checked').children('i').removeClass('no').addClass('yes');
                    $(this).prop('checked', true);
                }
                $(this).trigger("change");
            });

        });
    }
    iso_tag_container = $('#tags-container .btn-toggle');
    updateTagCount();
});


