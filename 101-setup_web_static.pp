# puppet setup 0 task
exec { 'update_packages':
  command  => 'sudo apt-get update',
  provider => shell,
}
-> package {'nginx':
    ensure => present,
}
-> exec { 'create directories':
  command  => 'sudo mkdir -p /data/web_static/shared/  /data/web_static/releases/test/',
  provider => shell,
}
-> exec { 'create fake html':
  command  => 'echo "Tests Nginx Static" | sudo tee /data/web_static/releases/test/index.html',
  provider => shell,
}
-> exec { 'create soft link':
  command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
  provider => shell,
}
-> exec { 'change permissions':
  command  => 'sudo chown -R ubuntu:ubuntu /data/',
  provider => shell,
}
-> exec { 'create alias page':
  command  => 'sudo sed -i "56i\\\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default',
  provider => shell,
}
-> exec { 'restart nginx':
  command  => 'sudo service nginx restart',
  provider => shell,
}
