<?php

require_once 'vendor/twig/twig/lib/Twig/Autoloader.php';
require_once 'vendor/css-crush/css-crush/CssCrush.php';
require_once 'menu.php';

Twig_Autoloader::register();

$loader = new Twig_Loader_Filesystem('templates/');
$twig = new Twig_Environment($loader, array(
    'cache' => 'template_cache',
    'auto_reload' => true
));


function render_404($requested_page) {
   header($_SERVER["SERVER_PROTOCOL"] . " 404 Not Found"); 
   render_template('404.html', array('requested_page' => $requested_page));
}

// Sends the client a page based on the master.html template. This function 
// should *not* be used for templates that do not inherit from master.html.
// If extra_template_args is set they will be sent to the template along with 
// the normal stuff master.html needs (the menu, the <link> tag for the 
// generated CSS, etc.)
function render_template($page, $extra_template_args = NULL) {
   global $twig, $menu;
   $css_tag = csscrush_tag('/resources/template.css', array('minify' => false));
   $template_data = array('menu' => $menu, 'css_tag' => $css_tag);
   if (isset($extra_template_args)) {
      $template_data = array_merge($template_data, $extra_template_args);
   }
   $template = $twig->loadTemplate($page);
   echo $template->render($template_data);
}

if (isset($_GET['page'])) {
   $page = $_GET['page'];
} else {
   $page = 'index.html';
}

try {
   render_template($page);
} catch (Twig_Error_Loader $e) {
   render_404($page);
}

?>

