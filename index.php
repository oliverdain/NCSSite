<?php

require_once 'vendor/twig/twig/lib/Twig/Autoloader.php';
Twig_Autoloader::register();

$loader = new Twig_Loader_Filesystem('templates/');
$twig = new Twig_Environment($loader, array(
    'cache' => 'template_cache',
));

$template = $twig->loadTemplate('index.html');
echo $template->render(array('name' => 'Network Charter School'));

?>

