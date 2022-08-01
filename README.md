# Serial Input


|              |                                                                                     |
| ------------ |-------------------------------------------------------------------------------------|
| name         | Serial Input                                                                      |
| version      | v1.0.0                                                                              |
| docker image | [weevenetwork/serial-input](https://hub.docker.com/r/weevenetwork/serial-input) |
| tags         | Python, Flask, Docker, Weeve                                                        |
| authors      | Ghassen Barbouchi                                                                   |

***
## Table of Content
- [Serial Input](#serial-input)
  - [Table of Content](#table-of-content)
  - [Description](#description)
    - [Features](#features)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)


***

## Description

This module reads data input from specified serial interface.

### Features
1. Open serial of a host machine
2. Read received serial data
3. Forward received serial data

## Environment Variables

### Module Specific
The following module configurations can be provided in a data service designer section on weeve platform:

| Name                | Environment Variables | Type    | Description               |Mandathory/Option|
|---------------------|-----------------------|---------|---------------------------|-----------------|
| Serial Port         | PORT                  | string  | eg: /dev/ttyUSB0          |   Mandathory    |
| Serial Baud_Rate    | BAUD_RATE             | integer | The data baud rate        |   Mandathory    |
| Number of data bits | DATA_BITS             | string  | Port number for tbe broker|    Option       |
| Parity              | PARITY                | string  | Enable parity checking    |    Option       |
| Stop bits           | STOP_BITS             | string  | Number of stop bits       |    Option       |

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

### Set by the weeve Agent on the edge-node

| Environment Variables | type   | Description                            |
|-----------------------| ------ | -------------------------------------- |
| EGRESS_URL            | string | HTTP ReST endpoint for the next module |
| MODULE_NAME           | string | Name of the module                     |


## Dependencies
```
requests
pyserial
```
