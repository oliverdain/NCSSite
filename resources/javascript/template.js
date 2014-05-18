var setup = function() {
    var hideAllSubMenus = function() {
      $('.visible-dropdown-list').removeClass('visible-dropdown-list');
    };

    // If the browser window is small a media query will be activated and there
    // will be a 'visible-nav-menu' class so we simply remove that class and, if
    // and only if we're on small screen, that will hide the menu.
    var hideMenuOnSmallScreens = function() {
      $('.visible-nav-menu').removeClass('visible-nav-menu');
    };

    var hideAllMenuItems = function() {
      hideMenuOnSmallScreens();
      hideAllSubMenus();
    };

    // This is called when the menu button (which is only visible on small
    // screens) is clicked.
    var toggleMenuVisibility = function() {
      // Either way, clicking the menu button should hide all the submenus.
      hideAllSubMenus();
      $('#nav-menu').toggleClass('visible-nav-menu');
    }

    // Handles displaying and hiding sub-menus. Note that we're grabbing all
    // click events as we want a click anywhere on the page besides a menu to
    // hide all open menus.
    $('body').on('click', function(e) {
      var $target = $(e.target);
      if ($target.attr('id') === 'menu-button') {
        toggleMenuVisibility();
      } else if ($target.hasClass('dropdown-button')) {
        var $list = $target.children('.dropdown-list');
        // If the list isn't currently visible it should become visible,
        // otherwise we just hide it.
        var display = ! $list.hasClass('visible-dropdown-list');
        // Either way, we don't want hide any currently visible sub-menus
        // (either because it was a different sub-menu or because we're now
        // hiding one that was visible).
        hideAllSubMenus();
        if (display) {
          $list.addClass('visible-dropdown-list');
        }
      } else {
        hideAllMenuItems();
      }
    });
};

$(document).ready(setup);
