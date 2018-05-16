# Minimalistic Route53 update script

A minimal-configuration script designed to support clusters with DNS failover.

## Requirements

This project requires [AWS
credentials](http://boto3.readthedocs.io/en/latest/guide/configuration.html) to
be configured.

## Usage

``` bash
sudo pip install r53-register
r53-register foo.example.com
```

## Optional configuration

|Environment variable|Default|Description|
|:-|:-|:-|
|`INTERFACE_PREFIX`|`en,eth,wl`|A comma-separated list of interface prefixes. Interfaces will be searched in order to find an IP address.|
|`INTERFACE_NAME`|`-`|A specific interface to grab the IP from.|
|`PUBLIC_IP`|`False`|Override interface search and use this machine’s public IP instead.|
