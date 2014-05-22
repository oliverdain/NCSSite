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
      new MenuItem('Introduction to NCS', '/intro.html'),
      new MenuItem('Our Charter', '/charter.html'),
      new MenuItem('Enrollment', '/enrollment.html')),
   'Students and Families' => array(
      new MenuItem('Calendar', '/calendar.html'),
      new MenuItem('Classes', '/classes.html')),
   'Our Partners' => array(
      new MenuItem('Le Petit Gourmet', '/lepetit.html'),
      new MenuItem('MECCA', '/mecca.html'),
      new MenuItem('Nearby Nature', '/nn.html'))
   );
?>
