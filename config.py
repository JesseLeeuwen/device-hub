import tomli

with open( "config.toml", mode="rb" ) as fp:
    config = tomli.load( fp )