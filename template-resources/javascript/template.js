var setup = function() {
    $('.dropdown-button').on('click', function(e) {
        var $list = $(e.currentTarget).children('.dropdown-list');
        var list = $list.get(0);
        var parentRect = list.parentElement.getBoundingClientRect();
        var top = parentRect.bottom + 10;
        list.style.top = '' + top + 'px';
        list.style.left = '' + parentRect.left + 'px';
        $list.toggleClass('visible-dropdown-list');
        console.dir(e);
    });
};

$(document).ready(setup);