# Zelos Microservice Specification

### GET [ec2-54-162-114-102.compute-1.amazonaws.com/zelos/placement](ec2-54-162-114-102.compute-1.amazonaws.com/zelos/placement)

Headers
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Authorization - Welcome2018!

Return
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;200 - all Shift resources
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4** - Client error with helpful message
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;500 - Server error

Behavior
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Queries Mongo running as docker container on EC2 for all Placement documents. Serializes returned documents through marshmallow schema. Returns JSON API formatted resource objects.

### GET [ec2-54-162-114-102.compute-1.amazonaws.com/zelos/placement/1](ec2-54-162-114-102.compute-1.amazonaws.com/zelos/placement//<placement_id>)

Headers
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Authorization - Welcome2018!

Return
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;200 - Placement resource with resource shift_id = url <placement_id>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4** - Client error with helpful message
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;500 - Server error
Behavior
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Queries Mongo running as docker container on EC2 for Placement document matching url <placement_id>. Serializes returned document through marshmallow schemas. Returns JSON API formatted resource object.


### GET [ec2-54-162-114-102.compute-1.amazonaws.com/zelos/placement?q=2a](ec2-54-162-114-102.compute-1.amazonaws.com/zelos/placement?q=2a)

Headers
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Authorization - Welcome2018!

Returns
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;200 - Centro exercise 2a resource
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4** - Client error with helpful message
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;500 - Server error

Behavior
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Queries Mongo running as docker container on EC2 for Centro exercise 2a resources. Serializes returned resources through marshmallow schemas. Returns JSON API formatted resource object.