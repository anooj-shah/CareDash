#!/bin/bash

curl -XPOST -H ‘Content-Type: application/json’ -d ‘{“name”:”Jane Doe”}’ http://localhost:3000/doctors

curl -XGET -H ‘Content-Type: application/json’ http://localhost:3000/doc:tors/1

curl -XPOST -H ‘Content-Type: application/json’ -d `{ "description": "Jane Doe is a great doctor. Review 1"}` http://localhost:3000/doctors/1/reviews

curl -XPOST -H ‘Content-Type: application/json’ -d `{ "description": "Jane Doe is really a great doctor. Review 2"}` http://localhost:3000/doctors/1/reviews

curl -XGET -H ‘Content-Type: application/json’ http://localhost:3000/doctors

curl -XGET -H ‘Content-Type: application/json’ http://localhost:3000/doctors/1

curl -XDELETE -H ‘Content-Type: application/json’ http://localhost:3000/doctors/1/reviews/2

curl -XDELETE -H ‘Content-Type: application/json’ http://localhost:3000/doctors/1
