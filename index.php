<?php

require_once 'vendor/twig/twig/lib/Twig/Autoloader.php';
require_once 'menu.php';

Twig_Autoloader::register();

$loader = new Twig_Loader_Filesystem('templates/');
$twig = new Twig_Environment($loader, array(
    'cache' => 'template_cache',
    'auto_reload' => true
));


$template = $twig->loadTemplate('index.html');
echo $template->render(array('menu' => $menu));

?>

