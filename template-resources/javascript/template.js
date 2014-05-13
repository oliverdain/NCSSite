var setup = function() {
    $('.dropdown-button').on('click', function(e) {
        var $list = $(e.currentTarget).children('.dropdown-list');
        var list = $list.get(0);
        $list.toggleClass('visible-dropdown-list');
    });
};

$(document).ready(setup);
