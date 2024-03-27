#setup new ubuntu server with nginx

exec { 'update system':
	command => '/usr/bin/apt-get update',
}

package {'nginx':
	ensure => 'installed',
	require => Exec['updae system']
}

file {'/var/www/html/index.html':
	content => 'Hello World!'
}

service {'nginx':
	ensure => running,
	require => Package['nginx']
}
