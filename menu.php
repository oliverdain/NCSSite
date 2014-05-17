<?php

class MenuItem {
   public $menu_text;
   public $url;

   public function __construct($text, $url) {
      $this->menu_text = $text;
      $this->url = $url;
   }
}

$menu = array(
   'About NCS' => array(
      new MenuItem('Introduction to NCS', 'intro.php'),
      new MenuItem('Our Charter', 'charter.php')),
   'Students and Families' => array(
      new MenuItem('Calendar', 'calendar.php'),
      new MenuItem('Classes', 'classes.php'))
   );
?>
