import 'nodes/*.pp'

node default {

}

$nova_config = hiera('nova_config')
create_resources('nova_config', $nova_config)
