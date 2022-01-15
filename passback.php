<?php
function get_name(){
    $dir = opendir("video_cut");

    //列出images 目錄中的文件
    while (($file = readdir($dir)) !== false)
      {
      echo  $file ." ";
      }
      closedir($dir);
    
}
get_name();
?>
