# Install flask from pip3

package {'Flask':
    ensure   => '2.1.1',
    provider => 'pip3',
}
