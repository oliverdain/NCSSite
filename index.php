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


$template = $twig->loadTemplate('index.html');
$css_tag = csscrush_tag('resources/template.css');
echo $template->render(array('menu' => $menu, 'css_tag' => $css_tag));

?>

