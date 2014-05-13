var setup = function() {
    $('.dropdown-button').on('click', function(e) {
        var $list = $(e.currentTarget).children('.dropdown-list');
        if ($list.hasClass('visible-dropdown-list')) {
          $list.removeClass('visible-dropdown-list');
        } else {
          // First hide whatever was visible before.
          $('.visible-dropdown-list').removeClass('visible-dropdown-list');
          $list.addClass('visible-dropdown-list');
        }
    });
};

$(document).ready(setup);
